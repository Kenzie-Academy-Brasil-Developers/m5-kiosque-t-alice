from menu import products


def get_product_by_id(id: int):
    my_list = {}

    if type(id) != int:
        raise TypeError("product id must be an int")

    for item in products:
        if item["_id"] == id:
            my_list = item

    return my_list


def get_product_by_type(my_type: str) -> list:
    my_list = []

    if type(my_type) != str:
        raise TypeError("product type must be a str")

    for item in products:
        if item["type"] == my_type:
            my_list.append(item)

    return my_list


def add_product(my_menu: list, **new_product: dict[str, any]):
    for item in products:
        if item["title"] == new_product["title"]:
            return "this product is already exist"

    my_id = len(my_menu) + 1
    my_item = {"_id": my_id, **new_product}
    my_menu.append(my_item)
    return my_item


def menu_report():
    product_count = len(products)
    my_total = 0.00
    my_list = {}
    my_count = 0

    for item in products:
        actual_type = item["type"]
        exist_type = my_list.get(actual_type)

        if exist_type is None:
            my_list.update({actual_type: 1})
        else:
            my_list[actual_type] += 1

        my_count += 1
        my_total += item["price"]
        my_list

    my_list_two = list(my_list)
    types_values = my_list_two[0]
    avarage_price = my_total / my_count

    return f"Products Count: {product_count} - Average Price: ${round(avarage_price, 2)} - Most Common Type: {types_values}"
