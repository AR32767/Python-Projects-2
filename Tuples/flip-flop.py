tuple1 = ()
for i in range(0,6):
    inp = int(input("Enter any numbers here... "))
    tuple1+(inp,)

if tuple1 == tuple1[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")