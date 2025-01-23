# Get the parentheses
input_str = input("Please enter any combination of parentheses without any white spaces among them: ")

# balance = 0 => balanced
balance = 0

# updating the counts of ( and )
for char in input_str:
    if char == '(':
        balance += 1
    else:
        balance -= 1

    # end the program if there are more ) than (
    if balance < 0:    
        print("Error: Missing '('")
        break
else:
    # condition to check if it balanced when balance is equal to zero, otherwise, there are missing ')'
    if balance == 0:
        print("The parentheses are balanced.")
    else:
        print("Error: Missing ')'")