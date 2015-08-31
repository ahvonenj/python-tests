import random

filepath = 'files/'
towrite = []

for i in range(0, 100):
    tmp = {}
    tmp['file'] = filepath + str(random.randint(100000, 999999)) + '.txt'
    tmp["value"] = 'VALUE: ' + str(random.randint(0, 1000000))
    towrite.append(tmp)

print(towrite)