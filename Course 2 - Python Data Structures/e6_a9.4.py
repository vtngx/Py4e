file = open(input('Enter file name: '))

words = dict()

for line in file:
    if line.startswith('From '):
        email = line.split()[1]
        words[email] = words.get(email, 0) + 1

max = None
maxMail = None

for email, count in words.items():
    if maxMail is None or count > max:
        maxMail = email
        max = count

print(maxMail, max)
