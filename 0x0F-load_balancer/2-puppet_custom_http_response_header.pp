#!/usr/bin/env bash

# Define a class for configuring Nginx with custom HTTP header
class nginx_custom_header {

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Set up custom Nginx configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "# Custom Nginx configuration with custom HTTP header\n
                server {
                  listen 80 default_server;
                  listen [::]:80 default_server;

                  server_name _;

                  # Add custom HTTP header
                  add_header X-Served-By $::hostname;

                  root /var/www/html;
                  index index.html index.htm index.nginx-debian.html;

                  location / {
                      try_files $uri $uri/ =404;
                  }
                }",
    notify  => Service['nginx'],
  }

  # Ensure Nginx service is running
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

# Include the class to configure Nginx with custom HTTP header
include nginx_custom_header

