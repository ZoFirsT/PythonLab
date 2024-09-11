#!/bin/bash

branch="main"

# Fetch the latest changes from the remote repository
git fetch origin $branch

# Check if there are any changes to pull
if [ $(git rev-list HEAD..origin/$branch --count) -gt 0 ]; then
    echo "Changes detected on remote. Pulling updates..."
    git pull origin $branch
    if [ $? -ne 0 ]; then
        echo "Failed to pull changes. Please resolve conflicts manually."
        exit 1
    fi
fi

# Add all changes
git add .

# Commit changes
git commit -m "Automated commit by ZoFirsT Bot: $(date)"

# Push changes
git push origin $branch

if [ $? -ne 0 ]; then
    echo "Git push operation failed!"
    echo "Attempting to pull changes and push again..."
    git pull origin $branch
    git push origin $branch
    
    if [ $? -ne 0 ]; then
        echo "Git operation failed after attempting to pull. Please check and resolve manually."
        exit 1
    fi
fi

echo "Git operations completed successfully."