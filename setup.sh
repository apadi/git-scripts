#!/usr/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

echo "" >> ~/.bashrc
echo "###############################################################" >> ~/.bashrc
echo "# prompt customization" >> ~/.bashrc
echo "###############################################################" >> ~/.bashrc
echo "export PATH=$DIR:\$PATH" >> ~/.bashrc
