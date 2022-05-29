logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
def sum(first_number,second_number):
  return first_number+second_number
def sub(first_number,second_number):
  return first_number-second_number
def multiply(first_number,second_number):
  return first_number*second_number
def divide(first_number,second_number):
  return first_number/second_number
  

syombals={
  "+":sum,
  "-":sub,
  "*":multiply,
  "/":divide
}

first_number=float(input("enter a number\n"))
for i in syombals:
  print(i)
repeat=False
while repeat is not True:
  second_number=float(input("enter second number\n"))
  operation=input("enter any above operation\n")
  choose=syombals[operation]
  a=choose(first_number,second_number)
  print(f"{first_number} {operation} {second_number} = {a}")
  b=input("enter yes for continuation no to stop\n")
  if(b=="yes"):
    first_number=a
  else:
    print()
    repeat=True
    
 