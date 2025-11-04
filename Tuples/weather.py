tuple1 = ()
for i in range(0,5):
    inp = int(input("Enter a 1 or a 0 here "))
    tuple1+(inp,)
weather = 0
sunny = 0 
for i in range (0,len(tuple1)+1):
    if i == 1:
        weather +=1
    else:
        sunny += 1

if weather > sunny:
    print("Cloudy")
elif sunny > weather:
    print("Sunny")
else:
    print("Equal chances of both")