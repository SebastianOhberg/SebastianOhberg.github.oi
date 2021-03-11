#Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
#A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if a one number is a factor of another is to use the modulo operation.
#When the number 3 'pling', 5 'plang' 7'plong'
x = int(input('write your number: '))

pling = x%3
plang = x%5
plong = x%7
 
if pling == 0:
    print('pling')
if plang == 0:
    print('plang')
if plong == 0:
    print('plong')

    