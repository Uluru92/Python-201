# Create a virtual environment (called VENVs) and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

import os

def print_VENVs_variables():
    environment = os.getenv('ENVIRONMENT')
    secret = os.getenv('SECRET')
    
    print(f'ENVIRONMENT: {environment}')
    print(f'SECRET: {secret}')

print_VENVs_variables()