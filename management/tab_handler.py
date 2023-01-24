from menu import products


def calculate_tab(table: list):

    sub_total = 0.00

    for item in table:
        for product in products:
            if product["_id"] == item["_id"]:
                sub_total += product["price"] * item["amount"]

    return {"subtotal": f"${round(sub_total, 2)}"}
