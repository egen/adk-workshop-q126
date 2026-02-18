#!/bin/bash

# 1. Stage all changes
git add .

# 2. Prompt for the commit message
echo "Enter your commit message:"
read -r commit_message

# Check if message is empty
if [ -z "$commit_message" ]; then
  echo "Commit message cannot be empty. Aborting."
  exit 1
fi

# Commit the changes
git commit -m "$commit_message"

# 3. Push to the specific branch
git push -u origin workshop/steve-hanks