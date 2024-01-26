print("-: Clothe shop :-")
gender = input("Please state gender : ")
if gender == 'male':
    print("What you like to were a jeans, t-shirt, shirt")
    clothe = input()
    if clothe == 'jeans':
        color = input("Which color blue or black : ")
        if color == 'blue':
            print("jeans with blue color selected.")
        elif color == 'black':
            print("black with blue color selected.")
        else:
            print("Selected color not found!!!")
    elif clothe == 't-shirt':
        color = input("Which color blue or black : ")
        if color == 'blue':
            print("t-shirt with blue color selected.")
        elif color == 'black':
            print("t-shirt with blue color selected.")
        else:
            print("Selected color not found!!!")
    elif clothe == 'shirt':
        color = input("Which color blue or black : ")
        if color == 'blue':
            print("shirt with blue color selected.")
        elif color == 'black':
            print("shirt with blue color selected.")
        else:
            print("Selected color not found!!!")
    else:
        print("Selected clothe not found!!!")
elif gender == 'female':
    print("What you like to were a saree, Kurta, skirt")
    clothe = input()
    if clothe == 'saree':
        color = input("Which color blue or black : ")
        if color == 'blue':
            print("saree with blue color selected.")
        elif color == 'black':
            print("saree with black color selected.")
        else:
            print("Selected color not found!!!")
    elif clothe == 'Kurta':
        color = input("Which color blue or black : ")
        if color == 'blue':
            print("Kurta with blue color selected.")
        elif color == 'black':
            print("Kurta with black color selected.")
        else:
            print("Selected color not found!!!")
    elif clothe == 'skirt':
        color = input("Which color blue or black : ")
        if color == 'blue':
            print("skirt with blue color selected.")
        elif color == 'black':
            print("skirt with black color selected.")
        else:
            print("Selected color not found!!!")
    else:
        print("Selected clothe not found!!!")
else:
    print("Error")