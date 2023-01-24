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
