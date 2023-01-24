from menu import products


def calculate_tab(table: list):

    my_total = 0.00

    for item in table:
        for product in products:
            if product["_id"] == item["_id"]:
                my_total += product["price"] * item["amount"]

    return {"subtotal": f"${round(my_total, 2)}"}
