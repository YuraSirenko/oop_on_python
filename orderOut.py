from order import *


def create_order_out_restaurant(customer_id, total_sum, delivery_address):
    new_order = OrderOut(customer_id, total_sum, delivery_address)
    print(f"New order out created with id : {new_order.order_id}")
    return new_order


class OrderOut(Order):
    def __init__(self, customer_id, total_sum, delivery_address):
        super().__init__(customer_id, total_sum)
        self._delivery_address = delivery_address

    @property
    def delivery_address(self):
        return self._delivery_address

    def get_data(self):
        order_info = self.get_base_data()
        order_info["delivery_address"] = self._delivery_address
        return order_info

    @staticmethod
    def greeting():
        return "Hi, dear customer! Bona Apetit!"