'''
INPUT: prints out numbers in a range of 1 to 100. Multiples 3("Fizz"), 5("Buzz"), 3*5("FizzBuzz")

OUTPUT: Once initalized program will print the range with "FizzBuzz" included.
'''

if __name__ == '__main__':
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
