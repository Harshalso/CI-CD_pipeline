#!/bin/bash

# Define variables
REPO_URL="https://github.com/Harshalso/CI-CD_pipeline.git"
TARGET_DIR="/var/www/html"

# Clone the latest version of the repository
cd /tmp
rm -rf CI-CD_pipeline
git clone $REPO_URL

# Copy files to the Nginx root directory
sudo cp -r CI-CD_pipeline/* $TARGET_DIR

# Restart Nginx
sudo systemctl restart nginx

echo "Deployment complete."
