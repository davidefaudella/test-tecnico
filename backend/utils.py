from models.Item import Item


def parse(input_data):

    def format_name(name):
        if "imported" in name:
            name.insert(0, name.pop(name.index("imported")))
        return " ".join(name)

    items = []
    try:
        rows = input_data.split("\n")
        for row in rows:
            words, price = row.split(" at ")
            qty, *name = words.split(" ")
            items.append(
                Item(
                    name=format_name(name),
                    price=float(price),
                    qty=int(qty),
                    imported=("imported" in name)
                )
            )
    except ValueError as e:
        return items
    return items
