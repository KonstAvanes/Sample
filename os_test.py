import os

# OS name
print(os.name)

# Current directory
print(os.getcwd())

# Create new path
new_path = os.path.join(os.getcwd(), 'new_f')

# Create directory
os.mkdir(new_path)

# Win32 sys command
os.system('msconfig')
