meanings = ['0', 's', '+', 'X', '=', '(', ')', '.', 'x', '1', '⊨', '^', '∃', '∀', '⇒']
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

if input("one do you want to encode or decode? ").lower() == "encode":
    encode = True
    expression = input("Please input an expression using only the characters: 0, s, +, X, =, (, ), ., x, 1, ⊨, ^, ∃, ∀, ⇒: ")
else:
    encode = False
    num = int(input("What is your godel number? "))

def expressionValid():
    for char in expression:
        if char not in meanings:
            return False
    return True

def encoder():
    num = 1
    i = 0
    for char in expression:
        num = num * (primes[i]**(meanings.index(char)+1))
        i += 1
    return num

def decoder(num):
    i=0
    j=0
    expression = ""
    while num != 1:
        if num%primes[i] == 0:
            print(f"T, num={num}, prime={primes[i]} i={i}, j={j}")
            num = num/primes[i]
            j += 1
        else:
            print(f"F, num={num}, prime={primes[i]} i={i}, j={j}, meaning={meanings[j-1]}")
            expression += meanings[j-1]
            i += 1 
            j=0
    expression += meanings[j-1]
    return expression

if encode:
    print(f"Your godel number is: {encoder()}")
elif not encode:
    print(decoder(num))
