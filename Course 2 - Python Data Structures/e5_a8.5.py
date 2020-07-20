file = open(input('Enter file name: '))

count = 0

for line in file:
    if line.startswith('From '):
        print(line.split()[1])
        count += 1

print('There were', count, 'in the file with \'From \' as the first word')
