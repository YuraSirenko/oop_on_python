from item import *
from order import *

class ItemHasOrder(Item, Order):
    def __init__(self, item, order):
        Item.__init__(self, item.item_id, item.item_name, item.item_price)
        Order.__init__(self, order.customer_id, order.total_sum)

    def get_data(self):
        item_info = Item.get_data(self)
        order_info = Order.get_base_data(self)
        return {**item_info, **order_info}