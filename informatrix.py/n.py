x=9
y=0
a=int(input())
brak=5
minute=a*45
while a!=0:
    a-=1
    if a%2==0:
        brak=15
    minute+=brak
    if a==0:
        break
hour=minute//60%24
min=minute%60
print(x+hour,':',y+min)