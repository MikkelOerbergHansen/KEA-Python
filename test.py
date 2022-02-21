user_input = input("Enter the input ")

it_is = False

while it_is == False:
    try:
        int(user_input)
        it_is = True
    except ValueError:
        user_input = input("Enter the input ")

print(it_is)