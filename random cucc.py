##0.9 ig egészek list
##számok = []
##for i in range(10):
##    számok.append(i)
##print(számok)
##
##
##számok2 = [x for x in range(10)]
##print(számok2)
##
##
##lst = []
##for  x in range(3):
##    lst.append(int(input()))
##print(lst)
##
##
##lst2 = [int(x) for x in input().strip().split()][:3]
##print(lst2)
##
##
##lst3 = list(map(int,[x for x in input().strip().split()][:3]))             #map(tevlkenység , hol hajtjuk végre)
##print(lst3)
##
##
pelda = [1,2,3,4]
példa_négyzet = []
for elem in pelda:
    x= elem**2
    példa_négyzet.append(x)
print(példa_négyzet)


def negyzet(x):
    return x**2

pelda_negyzet = list(map(negyzet,pelda))                #lehet def es függvény vagy lamda
##print(pelda_negyzet)


pelda_negyzet2 = []
pelda_negyzet2 = list(map(lambda x : x+2,pelda)) 
##print(pelda_negyzet2)



adatok = [(2,1),(3,-1),(4,2),(5,0)]             #()-tuple-k nem módosítható az érték
lista = [2,3,4,5]

lista[1] = 100
##print(lista)

lista2 = (1,2,3,4,['a','b'])
print(lista2)
#lista2[1] = 100 kapcsold be ha nézed

lista2[4][1] = 100
##print (lista2)

adatok.sort(key=lambda x:x[1])             #második szám szerint szortíroz
print(adatok)


def masodik(x):
    return x[1]

adatok.sort(key=masodik)             #második szám szerint szortíroz
print(adatok)


spec = {'a':(10,11),'b':20,'c':30}               #dictionary
print(spec['a'][1]*spec['b'])



