# A factorial is a reversing factor from a specific number (i.e. 5) until 1
# i.e. 5! = 5*4*3*2*1 = 
# This is an example about the recursive usage. 
def fact(x):
    if x == 1: # Base Case. This avoid infinite loops and it will be the end of Stack calls
        return 1
    else: # Recursive case. We multiply every previous number until to reach 1 (base case)
        return x * fact(x-1)

x = 5
factorial = fact(x)
print(str(x) + '! = ' + str(factorial))