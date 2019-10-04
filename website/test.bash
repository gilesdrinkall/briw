#!/usr/bin/env sh
sudo get-apt update
sudo get-apt nginx
sudo cp -r ~/PycharmProjects/briw/website /var/www/html/
sudo sudo service nginx restart
