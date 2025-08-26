#!/bin/bash

# Check if a commit message was provided
if [ -z "$1" ]; then
  echo "Usage: ./git_push.sh \"Your commit message\""
  exit 1
fi

# Add all changes
git add .

# Commit with your message
git commit -m "$1"

# Get current branch name
branch=$(git branch --show-current)

# Push to remote
git push origin "$branch"
