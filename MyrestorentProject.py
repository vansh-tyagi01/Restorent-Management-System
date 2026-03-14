print("*.....WELCOME TO XYZ RESTORENT.....*")
print(" ")
menu={
    1:("pasta",20),
    2:("momos",50),
    3:("noodels",40),
    4:("paalak paneer",120),
    5:("paneer",80),
    6:("aloo tickey",30),
    7:("matar plao",60),
    8:("pizza",150),
    9:("samosa",10),
    10:("aloo pakoda",30),
    11:("dal chawal",60),
    12:("chole chawal",70),
    13:("salad",20),
    14:("rasbhari 1kg",130),
    15:("rasbhari 0.5kg",65),
    16:("penuts",20),
    17:("matar",10),
    18:("tea",20),
    19:("choco milk",55),
    20:("mango shake",30),
    21:("banana shake",30),
    22:("mango shake with dry fruits",50),
    23:("banana shake with dry fruits",50),
    24:("dairy milk",100)
}
print("*......MENU......*")
print(" ")

for key,value in menu.items():
    print(f"{key}. {value[0]} : {value[1]} rupee")

print(" ")
print("PLEASE SELECT YOUR ITEM IN MENU?")
print(" ")

total_rupees=0

while True:
    select_item = int(input("Enter your item? Do you want to order:"))
    qty = int(input("Enter quantity of your item?:"))
    print(" ")

    if select_item in menu:
        item_name = menu[select_item][0]
        quantity = menu[select_item][1] * qty

        total_rupees+=quantity
        print(f"{qty} quantity {item_name} is order successfull please wait, your order will arrive shortly")
    else:
        print("Item is not available! please choose another item")

    print(" ")
    another_item=input("Do you want to order another item?(yes/no):").lower()

    if another_item == "yes":
        continue
    elif another_item == "no":
        break
    else:
        print("Invalid choice!")

print(" ")
print("Total rupees =",total_rupees)   






#........................                                    Thank You                                      .........................#


