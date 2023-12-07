""" Function With positional Arguments """

def power(x):

    if x == 1:
        return 1
    else:
        return (x ** 2)

num = int(input("enter any number : "))
print(f"The power of {num} is {power(num)}")