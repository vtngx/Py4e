file = open(input('Enter file name: '))
fileWordsList = file.read().split()

lst = list()

for word in fileWordsList:
    if not word.strip() in lst:
        lst.append(word)

lst.sort()
print(lst)
