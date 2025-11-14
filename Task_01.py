def add(a,b):
  return float(a+b)
def subtract(a,b):
  return float(a-b)
def multiply(a,b):
  return float(a*b)
def divide(a,b):
  if(b == 0):
    print("We cannot divide the number by 0!")
    return None
  else:
    return float(a/b)
def power(a,b):
  return float(a**b)
def remainder(a,b):
  return float(a%b)
  
 

def select_op(choice):
  if choice == '#':
    return -1
  if choice == '$':
    return 0
  
  if choice == '+':
    result = add
  elif choice == '-':
    result = subtract
  elif choice == '*':
    result = multiply
  elif choice == '/':
    result = divide
  elif choice == '^':
    result = power
  elif choice == '%':
    result = remainder
  else:
    print("Unrecognized operation")
    return None

  while True:
        a = input("Enter first number: ")
        if a == '$':
            return 0
        try:
            a = float(a)
            break
        except:
            print("Not a valid number,please enter again")
  while True:
        b = input("Enter second number: ")
        if b == '$':
            return 0
        try:
            b = float(b)
            break
        except:
            print("Not a valid number,please enter again")
  
  answer = result(a,b)
  if answer is not None:
     print(f"{a} {choice} {b} = {answer}")
  return 1


while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    print("Done. Terminating...")
    exit()