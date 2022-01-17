from math import ceil


class Item:
    def __init__(self, name, qty, price, imported):
        self.name = name
        self.qty = qty
        self.price = price
        self.imported = imported

        self.exempt_categories = ["chocolate", "chocolates", "book", "pills"]
        self.basic_tax_rate = 10
        self.import_tax_rate = 5

    def taxes(self):
        taxes = 0
        if not self.isExempt():
            taxes = self.calc_tax('basic') * self.qty
        if self.imported:
            taxes += self.calc_tax('import') * self.qty
        return round(taxes, 2)

    def calc_tax(self, t):
        rate = self.basic_tax_rate if t == 'basic' else self.import_tax_rate
        tax = (self.price * rate) / 100
        return ceil(tax / 0.05) * 0.05

    def isExempt(self):
        # array intersection
        arr = list(filter(
            lambda x: x in self.name.split(), self.exempt_categories
        ))
        return len(arr)

    def total(self):
        return round(self.price * self.qty + self.taxes(), 2)

    def toString(self):
        return "{} {}: {}".format(str(self.qty),
                                  self.name, format(self.total(), '.2f'))
