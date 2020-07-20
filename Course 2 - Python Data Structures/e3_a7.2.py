file = open(input('Enter file name: '))

count = 0
s = 0

for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        num = float(line[(line.find(':') + 1) : len(line)].strip())
        s += num
        count += 1

print('Avg spam confidence: ', s / count)
