#loop4
print("loop4")
print()

n = int(input("What is n?" ))
sum = 0
for i in range(1,n):
    sum = sum + i
sum2 = sum + n
print(n)
print("The total between", 1, "and", n-1, "is", sum)
print("The total between", 1, "and", n, "is", sum2)
