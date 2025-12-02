import art
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2



functions={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}

# mul=functions["*"]
# print(mul(4,8))

game_on=True
print(art.logo)
n1 = float(input("Enter the first number: "))

while game_on:
    for key in functions:
        print(key)
    operation = input("Pick an Operation: ")
    n2 = float(input("Enter the second number: "))
    sum = functions[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {sum}")
    go_on=input(f"Type 'y' to continue calculating with {sum}, or type 'n' to start a new calculation: ").lower()
    if go_on=="y":
        n1=sum
    elif go_on=="n":
        n1 = float(input("Enter the first number: "))
    else    :
        game_on=False
