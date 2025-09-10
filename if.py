age = 25
has_id = False
if age >= 18 and has_id:
    print("Can vote")
else:
    print("Cant vote")

is_raining = True
if not is_raining:
    print("Go outside")
else:
    print("Write code")

age = 60
is_member = True

if age >= 50:
    if is_member:
        print("Discount 50%")
    else:
        print("Discount 20%")
else:
    print("Regular price")

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or three")
    case _:
        print("Other number")