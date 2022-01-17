class Receipt:
    def __init__(self, items):
        # list of Item objects
        self.items = items

    def taxes(self):
        taxes = 0
        for item in self.items:
            taxes += item.taxes()
        return taxes

    def total(self):
        total = 0
        for item in self.items:
            total += item.total()
        return total

    def toString(self):
        output = "" if len(self.items) else "No Items" + "\n"
        for item in self.items:
            output += item.toString() + "\n"
        output += "Sales Taxes: {}\n".format(format(self.taxes(), '.2f'))
        output += "Total: {}".format(format(self.total(), '.2f'))
        return output
