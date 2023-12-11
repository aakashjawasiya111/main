def info():
    n = int(input('enter number :-'))
    if n == 1:
        print("1 is not a prime number")
    else:
        for i in range(2,n):
            if i % 2 == 0:
                i += 1
                break
        if i % 2 != 0:
            print(i , end=" ")

local = info()
print(local)
