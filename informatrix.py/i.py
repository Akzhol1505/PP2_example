a=int(input())
print(a%10 + a//100 + ((a-a%10)/10)%10)