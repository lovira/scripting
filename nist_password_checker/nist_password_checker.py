#check is more than or equal to 8 
def checkLength(password):
    return len(password) >= 8

#check if there is a repetitive sequence of chars that of more than 3 such as "blaaaaa"
def checkRepetitiveChars(password):
    count = 1
    for char in range(len(password) - 1):
        if password[char] == password[char+1]:
            count += 1
            if count > 3 :
                return False
    return True
    
def checkSequentialChars(password):
    numericSequence = "0123456789"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(password) - 2):
        seq = password[i:i+3]
        if seq in numericSequence or seq[::-1] in numericSequence or seq in alphabet or seq[::-1] in alphabet:
            return False
            break  # Once a sequence is found, no need to keep checking
    return True

def checkCompromisedList(password):
    with open('500-worst-passwords.txt') as f:
        compromised_passwords = set(f.read().splitlines())
        if password in compromised_passwords:
            return False
    return True


def validate_password(password):
    # Initialize a list to hold error messages
    errors = []

    if  not checkLength(password):
        errors.append("Password must be at least 8 characters long.")
    if  not checkRepetitiveChars(password):
        errors.append("Password contains too many repetitive characters.")
    if  not checkSequentialChars(password):
        errors.append("Password contains sequential characters.")
    if  not checkCompromisedList(password):
        errors.append("Password is compromised and cannot be used.")

    # check if password does not meet any of the criteria, if not error flag is raised. 
    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid.")
    

password = input("Enter Your Password: ")
validate_password(password)
