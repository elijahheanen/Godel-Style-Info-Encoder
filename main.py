meanings = ['0', 's', '+', 'X', '=', '(', ')', '.', 'x', '1', '⊨', '^', '∃', '∀', '⇒']
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
expression = "0+s"

def expressionValid():
    for char in expression:
        if char not in meanings:
            return False
    return True

def convert():
    num = 1
    i = 0
    for char in expression:
        num = num * (primes[i]**(meanings.index(char)+1))
        i += 1
    return num

if expressionValid():
    print(convert())
