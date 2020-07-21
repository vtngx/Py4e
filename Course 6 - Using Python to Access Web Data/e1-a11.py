import re

file = open('regex-sum.txt')
lst = list()

for line in file:
    lst += re.findall('[0-9]+', line)

sum = 0
for num in lst:
    sum += int(num)

print('Sum:',sum)
