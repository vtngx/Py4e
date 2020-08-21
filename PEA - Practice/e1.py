def convertNumber(n):
    return str(n).replace("0","5")

def main():
    n = int(input('Enter number: '))
    print('Converted number:',convertNumber(n))

main()

