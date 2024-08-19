#!/bin/bash

# Specify the branch to use
branch="main"  # Replace with your desired branch

# Stage only changed files
git add -u

# Create a more informative commit message
git commit -m "Automated commit by ZoFirsT Bot: $(date)"

# Push to the specified branch
git push origin $branch

# Check for errors and provide feedback
if [ $? -ne 0 ]; then
  echo "Git operation failed!"
  exit 1
fi