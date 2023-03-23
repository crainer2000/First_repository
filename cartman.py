# def say():
#     name = input("name: ")
#     if name == "david":
#         return say()
#     return "Welcome"
# say()

def ussd():
    uss = input("Enter the ussd code: ")
    if uss == "*123#":
        print(f"1 for Data")
    else:
        print("Invalid Entry\n Try Again!")
        ussd()
ussd()