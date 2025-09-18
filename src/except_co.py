class ExceptBo(Exception):

    def test_add_product(self, quantity):
        if quantity == 0:
            raise ValueError()
