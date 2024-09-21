class Order:
    _order_counter = 0

    def __init__(self, customer_id, total_sum):
        Order._order_counter += 1
        self._order_id = Order._order_counter
        self._customer_id = customer_id
        self._total_sum = total_sum

    @property
    def total_sum(self):
        return self._total_sum

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def order_id(self):
        return self._order_id

    def update_total_sum(self, n):
        self._total_sum = n

    def get_base_data(self):
        return {
            "customer_id": self._customer_id,
            "total_sum": self._total_sum
        }
