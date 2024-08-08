# Create a virtual environment (called VENVs) and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

#I called my venv: venv_05_04 just to be more organized with all this VENVs lately :D

import os

environment = os.getenv('ENVIRONMENT')
secret = os.getenv('day')

print(f'ENVIRONMENT: {environment}')
print(f'SECRET: {secret}')