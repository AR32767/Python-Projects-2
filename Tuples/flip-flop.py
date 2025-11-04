tuple1 = (1,2,3,3,2,1)
tuple2 = slice(0,len(tuple1)/2+1)
tuple3 = slice(len(tuple1)/2+2,len(tuple1)+1)
mtuple3=slice(0,-len(tuple3)-1,-1)
if tuple2 == mtuple3:
    print("Palindrome")
else:
    print("No palindrome")
