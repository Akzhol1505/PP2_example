print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



def myFunction() :
  return True 

if myFunction():
  print("YES!")
else:
  print("NO!")   #return "YES!" if the function returns true


  x = 200
print(isinstance(x, int))    #check if the number is integer


q=10
w=20
print (q**w)


if (q is not w):
    print ('YES')  #if q != w print YES

