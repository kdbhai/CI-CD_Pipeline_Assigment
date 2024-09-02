#!/bin/bash

# Define variables
REPO_URL="https://github.com/kdbhai/CI-CD_Pipeline_Assigment.git"
DEPLOY_DIR="/var/www/html"
NGINX_SERVICE="nginx"

# Clone latest code from GitHub repository
echo "Cloning latest code from GitHub repository..."
mkdir temprepo
git clone --depth 1 $REPO_URL temprepo
rm -rf $DEPLOY_DIR/*
cp -r temprepo/* $DEPLOY_DIR/
rm -rf temprepo
# Copy HTML files to Nginx's web root
echo "Copying HTML files to Nginx's web root..."
cp $DEPLOY_DIR/*.html /usr/share/nginx/html/

# Restart Nginx to apply changes
echo "Restarting Nginx to apply changes..."
systemctl restart $NGINX_SERVICE

echo "Deployment successful!"
