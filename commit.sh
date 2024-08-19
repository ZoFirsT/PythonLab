#!/bin/bash

branch="main"

git add -u

git commit -m "Automated commit by ZoFirsT Bot: $(date)"

git push origin $branch

if [ $? -ne 0 ]; then
  echo "Git operation failed!"
  exit 1
fi