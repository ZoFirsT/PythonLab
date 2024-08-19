#!/bin/bash

git add .

git commit -m "Automated commit by ZoFirsT Bot: $(date)"

git push

if [ $? -ne 0 ]; then
  echo "Git operation failed!"
  exit 1
fi