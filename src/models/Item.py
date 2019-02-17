class Item:
    def __init__(self, product_sku, product_name):
        self.product_sku = product_sku
        self.product_name = product_name

    def as_dict(self):
        result = dict()
        result['product_sku'] = self.product_sku
        result['product_name'] = self.product_name
        return result
