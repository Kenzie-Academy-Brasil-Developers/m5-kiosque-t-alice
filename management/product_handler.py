from menu import products


def get_product_by_id(id: int):
    my_list = {}

    for item in products:
        if item["_id"] == id:
            my_list = item

    return my_list


def get_product_by_type(type: int):
    my_list = []

    for item in products:
        if item["type"] == type:
            my_list.append(item)

    return my_list


def add_product(menu: list, **new_product):
    for item in products:
        if item["title"] == new_product["title"]:
            return "This product is already exist"

    new_id = len(menu) + 1
    new_item = {"_id": new_id, **new_product}
    menu.append(new_item)
    return new_item
