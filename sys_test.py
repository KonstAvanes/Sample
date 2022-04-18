import sys


# Path to interpretation
print(sys.executable)

# Information platform
print(sys.platform)

if sys.platform == 'win32':
    print('Oooo eee baby')


# Exit python
sys.exit()

print('It is not executable')
