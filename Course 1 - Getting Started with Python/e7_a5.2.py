min = None
max = None

while True:
    num = input('Enter number:')    #input 7, 2, bob, 10, 4
    if num == 'done':   break

    try:
        num = int(num)
        if min is None:
            min = num
        elif min > num:
            min = num

        if max is None:
            max = num
        elif max < num:
            max = num

    except:
        print('<invalid?>')

print('Min', min)
print('Max', max)
