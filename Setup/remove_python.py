import os
import subprocess

def get_username():
    username = input("Enter the username: ")
    return username

def edit_remove_script(username):
    script_content = f'''#!/bin/bash

# Uninstall all versions of Python for the user {username}

# Uninstall all Python packages
pip freeze | xargs pip uninstall -y

# Uninstall Python (adjust the path if needed)
if [ -d "/home/{username}/.local/bin" ]; then
    rm -rf "/home/{username}/.local/bin"
fi

# Remove additional packages that might be installed with Python
pip uninstall -y package_name1 package_name2

# Optionally, remove Python from the system PATH
echo 'export PATH=$PATH:/usr/local/bin' >> /home/{username}/.bashrc
'''

    with open('remove_python.sh', 'w') as script_file:
        script_file.write(script_content)

def execute_remove_script():
    subprocess.run(['bash', 'remove_python.sh'])

def main():
    username = get_username()
    edit_remove_script(username)
    execute_remove_script()
    print("Python removal script executed successfully.")

if __name__ == "__main__":
    main()
