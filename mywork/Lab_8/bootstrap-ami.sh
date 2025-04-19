#!/bin/bash

# Update the package index
dnf update -y

# Install required packages
dnf install -y python3 git nginx

# Start the nginx service
systemctl enable nginx
systemctl start nginx

# Create a simple index.html page
echo "<h1>EC2 Bootstrapping Successful: python3, git, nginx installed</h1>" > /usr/share/nginx/html/index.html


# Update the system
sudo dnf update -y

# Install packages
sudo dnf install -y python3 git nginx

#!/bin/bash

dnf update -y
dnf install -y python3 git nginx

# Start nginx manually (no systemd)
nginx

# Write confirmation page
echo "<h1>EC2 Bootstrapping Successful: python3, git, nginx installed</h1>" > /usr/share/nginx/html/index.html


# Confirm it's working
curl http://localhost/
