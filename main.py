from orderIn import *
from orderOut import *
from itemHasOrder import *

o1 = OrderIn(1, 200, 2, 4)
o2 = OrderOut(2, 100,  "123 Main St")

items = [
    Item(1, "ApplePie", 35),
    Item(2, "BananaBread", 25),
    Item(3, "CherryTart", 30)
]

print(items[0].get_data())
relation1 = ItemHasOrder(items[1],o1)
relation2 = ItemHasOrder(items[2],o2)

print(o1.get_data())
print(o2.get_data())
print(relation1.get_data())
print(relation2.get_data())

o3 = create_order_in_restaurant(2,0,1,10)
print(o3.greeting())
o4 = create_order_out_restaurant(2,0,"mak street 12")
print(o4.greeting())
