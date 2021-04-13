import sys
from random import random

if len(sys.argv) < 4:
    print("Too few arguments!\n")
    exit()

r = int(sys.argv[1])
c = int(sys.argv[2])
output_filename = sys.argv[3]

file = open(output_filename, "w")

file.write(f'{r}\n')
file.write(f'{c}\n')

for i in range(r * c):
    number = -100 + random() * 200
    file.write(f'{number}\n')

file.close()
