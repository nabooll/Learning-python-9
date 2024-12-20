# Make the function first
def password_controller(code):
    if len(code) > 8: # Len for check the string
        return True # We return it as a boolean
    else:
        return False
    return code
code = input("Your Password : ")
psw = password_controller(code)
print(psw)
