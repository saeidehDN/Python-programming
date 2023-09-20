def characterchange(string):
    st = ""
    for i in range(0, len(string)):
        if string[i].islower() == True:
            st += string[i].upper()
        else:
            st += string[i].lower()

    return st
input1 = input("Enter a string")
print(characterchange(input1))