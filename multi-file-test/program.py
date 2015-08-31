import random

filepath = 'files/'
files = []
data = []

for i in range(0, 10):
    files.append(filepath + str(random.randint(100000, 999999)) + '.txt')
    
for i in range(0, 100000):
    data.append(str(random.randint(0, 1000000)))
    
