name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
file = open(name)

words = dict()
for line in file:
    if line.strip().startswith('From '):
        timeSubmitted = line.split()[5]
        hourSubmitted = timeSubmitted.split(':')[0]
        words[hourSubmitted] = words.get(hourSubmitted, 0) + 1

sort = sorted([k,v] for (k,v) in words.items())

for k,v in sort:
    print(k,v)
