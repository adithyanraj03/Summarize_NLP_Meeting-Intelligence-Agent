#!/bin/bash

# Uninstall all versions of Python for the user Admin

# Uninstall all Python packages
pip freeze | xargs pip uninstall -y

# Remove additional packages that might be installed with Python
pip uninstall -y package_name1 package_name2

# Optionally, remove Python from the system PATH
echo 'export PATH=$PATH:/usr/local/bin' >> /home/Admin/.bashrc
