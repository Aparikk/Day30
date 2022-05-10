# try:
#     file = open("text.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("text.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("Easy error")

height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("You are not that tall")

bmi = weight / height ** 2
print (bmi)

if bmi > 25:
    print ("You are a fat fuck. Stop eating")