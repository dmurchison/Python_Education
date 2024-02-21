n = 10


def tester(n):
    for i in range(n + 1):
        if i%3==0 and i%5==0:
            print(f"{i} is divisible by 3 and 5")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")

tester(n)
