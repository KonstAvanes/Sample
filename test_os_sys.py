import sys, os

name = sys.platform

for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), f'{name}_{i}')
    os.mkdir(new_path)