# CI-CD_pipeline
CI/CD assignment

# HTML File
Task: 1
Created HTML file.
Initialised Git repo:

mkdir CI-CD_pipeline
cd CI-CD_pipeline
git init
echo "index.html" > .gitignore
git add .
git commit -m "Initial commit of simple HTML project"

git push -u origin main

# Task 2
Launch an AWS EC2 instance:
Choose an Amazon Linux 2 or Ubuntu 20.04 instance.
Configure security groups to allow HTTP (port 80) and SSH (port 22) access.

Connected EC2 console and Installed NGINX

sudo dnf install nginx -y

sudo systemctl start nginx

sudo systemctl enable nginx

sudo systemctl status nginx

Public IP: http://51.20.6.152/

# Task 3 Python Script to Check for New Commits

Installed dependencies:


