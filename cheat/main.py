import cv2
import numpy as np
import pyautogui
import os
import time
import logging
import signal
import threading
from collections import deque

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TemplateMatcher:
    def __init__(self, template_path):
        self.template_gray = self.load_template(template_path)
        self.target_queue = deque()
        self.lock = threading.Lock()
        self.running = True
        self.threshold = 0.3
        self.capture_interval = 0.05
        self.match_interval = 0.05
        self.screen_gray = None  # Initialize screen_gray
        self.capture_thread = threading.Thread(target=self.capture_screen_loop)
        self.match_thread = threading.Thread(target=self.match_template_loop)
        self.process_thread = threading.Thread(target=self.process_targets)

    def load_template(self, template_path):
        """Load and convert the template image to grayscale."""
        logging.info(f"Loading template from {template_path}")
        template = cv2.imread(template_path)
        if template is None:
            raise FileNotFoundError(f"Cannot load the template image at {template_path}. Please check the file path.")
        return cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    def capture_screen_loop(self):
        """Continuously capture the screen in a separate thread."""
        while self.running:
            screenshot = pyautogui.screenshot()
            screenshot_np = np.array(screenshot)
            screen_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
            with self.lock:
                self.screen_gray = screen_gray
            time.sleep(self.capture_interval)

    def find_template_location(self, screen_gray):
        """Find the template location in the screen image using template matching."""
        result = cv2.matchTemplate(screen_gray, self.template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        return max_loc, max_val

    def match_template_loop(self):
        """Continuously match the template in a separate thread."""
        while self.running:
            with self.lock:
                if self.screen_gray is not None:
                    max_loc, max_val = self.find_template_location(self.screen_gray)
                    if max_val >= self.threshold:
                        # Calculate target position
                        target_x, target_y = max_loc
                        target_x += self.template_gray.shape[1] // 2
                        target_y += self.template_gray.shape[0] // 2

                        # Get screen size for bounds checking
                        screen_width, screen_height = pyautogui.size()
                        logging.info(f"Screen size: {screen_width} x {screen_height}")

                        # Ensure the target position is within screen bounds
                        if 0 <= target_x <= screen_width and 0 <= target_y <= screen_height:
                            # Add to target queue
                            with self.lock:
                                self.target_queue.append((target_x, target_y))
            time.sleep(self.match_interval)

    def move_and_click(self, target_x, target_y):
        """Move the mouse to the target position and click."""
        logging.info(f"Moving mouse to ({target_x}, {target_y})")
        pyautogui.moveTo(target_x, target_y, duration=0.1)  # Smooth mouse movement
        pyautogui.click()  # Click at the target position
        logging.info("Clicked to collect points")

    def process_targets(self):
        """Process targets from the queue one at a time."""
        while self.running:
            if self.target_queue:
                with self.lock:
                    target_x, target_y = self.target_queue.popleft()  # Get the first target in the queue
                self.move_and_click(target_x, target_y)
                # Sleep to ensure there's a small delay between processing targets
                time.sleep(0.2)

    def signal_handler(self, signal, frame):
        """Handle signals to stop the script gracefully."""
        logging.info("Stopping script.")
        self.running = False
        self.capture_thread.join()
        self.match_thread.join()
        self.process_thread.join()

    def run(self):
        """Start capturing, matching, and processing threads."""
        logging.info("Starting template matcher")
        self.capture_thread.start()
        self.match_thread.start()
        self.process_thread.start()

if __name__ == "__main__":
    # Setup signal handling for graceful shutdown
    matcher = TemplateMatcher(template_path=os.path.join(os.path.dirname(__file__), 'template.png'))
    signal.signal(signal.SIGINT, matcher.signal_handler)
    signal.signal(signal.SIGTERM, matcher.signal_handler)
    
    matcher.run()
