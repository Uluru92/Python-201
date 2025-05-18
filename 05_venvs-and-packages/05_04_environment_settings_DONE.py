# Create a virtual environment (called VENVs) and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

#I called my venv: venv_05_04 just to be more organized with all these VENVs lately :D

# Solution: 
#   - Created a venv called venv_05_04
#   - Created a script activate_with_env.ps1
#   - activate the venv_05_04 through activate_with_venv.ps1
#   - While venv venv_05_04 running, py 05_04_environment_settings.py

import os

environment = os.getenv('ENVIRONMENT')
secret = os.getenv('SECRET')

print(f"ENVIRONMENT: {environment}")
print(f"SECRET: {secret}")