class Item:
    def __init__(self, item_id, item_name, item_price):
        self._item_id = item_id
        self._item_name = item_name
        self._item_price = item_price

    @property
    def item_id(self):
        return self._item_id

    @property
    def item_name(self):
        return self._item_name

    @property
    def item_price(self):
        return self._item_price

    def get_data(self):
        return {
            "item_id": self._item_id,
            "item_name": self._item_name,
            "item_price": self._item_price
        }
