def simpleFunction(number):
    number = eval(input("Enter The Number To Find It's Output of Sum Of Natural Number.:\t"))
    sum = 0
    for i in range(number+1):
        sum += i
    print(f"Sum Of Natural Number {number} Using Iteration Is:\t", sum)

def recursiveFunction(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return number + recursiveFunction(number-1)
    
def factorial(number):
    fact = 1
    for i in range(number):
        fact = fact * (i+1)
    print(f"Factorial Of Number {number} Using Iteratioin is:\t", fact)

def recFactorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * recFactorial(number-1)

def fibbonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibbonacci(number-1) + fibbonacci(number-2)

if __name__ == '__main__':
    number = eval
    while True:
        chce = int(input('''
            <---------------------------------------Sum, Fibonacci Series & Factorial Operations--------------------------------------->
            1 Sum Of Natural Number via Iteration
            2 Sum Of Natural Number via Recursion
            3 Factorial via Iteration
            4 Factorial via Recursion
            5 Fibbonacci Series Via Recursion
            6 Exit From Oerations
                    '''))

        if chce == 1:
            simpleFunction(number)            
        elif chce == 2:
            number = eval(input("Enter The Number To Find It's Output of Sum Of Natural Number.:\t"))
            print(f"Sum Of Natural Number {number} Using Recursion is:\t", recursiveFunction(number))
        elif chce == 3:
            number = eval(input("Enter The Number To Find It's Factorial.:\t"))
            factorial(number)
        elif chce == 4:
            number = eval(input("Enter The Number To Find It's Factorial via Recursion.:\t"))
            print(f"Factorial Of Number {number} Using Recursion is:\t", recFactorial(number))
        elif chce == 5:
            number = eval(input("Enter The Number To Find It's Output of fibbonacci Series Sum.:\t"))
            print(f"fibbonacci Series Sum Of Number {number} Using Recursion is:\t", fibbonacci(number))
        elif chce == 6:
            break
        else:
            print("Invalid Choice")