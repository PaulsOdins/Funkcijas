from nedeldiena import diena_vardos
import romb
print(diena_vardos(int(input('Ievadi nedēļas dienas numuru: '))))
print('8.uzd')
x1,y1 = input('Ievadi pirmā punkta koordinātas(x,y) atdalot tās ar komatu: ').split(',')
x2,y2 = input('Ievadi otrā punkta koordinātas(x,y) atdalot tās ar komatu: ').split(',')
x3,y3 = input('Ievadi trešā punkta koordinātas(x,y) atdalot tās ar komatu: ').split(',')
x4,y4 = input('Ievadi ceturtā punkta koordinātas(x,y) atdalot tās ar komatu: ').split(',')
print(romb.lauk(romb.diagn(int(x1),int(y1),int(x2),int(y2)), romb.diagn(int(x3),int(y3),int(x4),int(y4))))