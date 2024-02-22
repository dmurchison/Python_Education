n = 10


def tester(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(f"The number {i} is not divisible by 3 or 5.")

tester(n)

def single_thread_cpu_bound(n):
    for i in range(n):
        print(i**2)

single_thread_cpu_bound(n)
