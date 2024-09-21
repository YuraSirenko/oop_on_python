from order import *


def create_order_in_restaurant(customer_id, total_sum, number_of_customers, table_id):
    new_order = OrderIn(customer_id, total_sum, number_of_customers, table_id)
    print(f"New order in created with id : {new_order.order_id}")
    return new_order


class OrderIn(Order):
    def __init__(self, customer_id,total_sum, number_of_customers, table_id):
        super().__init__(customer_id, total_sum)
        self._table_id = table_id
        self._number_of_customers = number_of_customers

    @property
    def table_id(self):
        return self._table_id

    @property
    def number_of_customers(self):
        return self._number_of_customers

    def update_number_of_customers(self, n):
        self._number_of_customers = n

    def get_data(self):
        order_info = self.get_base_data()
        order_info["table_id"] = self._table_id
        order_info["number_of_customers"] = self._number_of_customers
        return order_info

    @staticmethod
    def greeting():
        return "Hi, dear customer! It`s so nice to see you here!"
