feet_inches = input("Enter feet and inches: ")

# def convert(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])

#     meters = feet * .3048 + inches * 0.0254
#     #return f"{feet} feet and {inches} inches is equal to {meters} meters."
#     return meters

def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * .3048 + inches * 0.0254
    return meters    

f, i = parse(feet_inches)
print("fi", f, i)
result = convert(f,i)


# print(convert(feet_inches))
# result = convert(feet_inches)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide.")