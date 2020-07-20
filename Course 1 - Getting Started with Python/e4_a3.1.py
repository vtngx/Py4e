hours =  float(input('Hours: '))    #input 45
rate = float(input('Rate: '))       #input 10.50
if(hours <= 40):
    pay = rate * hours
else:
    pay = (rate * 40) + ((1.5 * rate) * (hours - 40))
print('Pay:',pay)
