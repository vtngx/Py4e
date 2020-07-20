def computerpay(h, r):
    if hours <= 40:
        return rate * hours
    else:
        return (rate * 40) + ((1.5 * rate) * (hours - 40))


hours = float(input('Hours: '))     # input 45
rate = float(input('Rate: '))       # input 10.50
pay = computerpay(hours, rate)
print('Pay:', pay)
