fname = input('Enter file name: ')
file = open(fname)

print(file.read().upper().strip())
