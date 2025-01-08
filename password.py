password = input("Enter new password: ")

#result = []
result = {}

if len(password) >= 8:
    #result.append(True)
    result["lenght"] = True
else:
    #result.append(False)
    result["lenght"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
#result.append(digit)
result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
#result.append(uppercase)
result["upper-case"] = uppercase

print(result)
print(all(result)) # if all contents are true then return true
#if all(result) == True:
#if all(result):
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")