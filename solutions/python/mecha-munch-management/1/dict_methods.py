"""Functions to manage a users shopping cart items."""

from collections import Counter

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    return Counter(current_cart) + Counter(items_to_add)


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    updated =  dict(ideas)
    updated |= dict(recipe_updates)
    return dict(reversed(sorted(updated.items())))


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfilment_cart = { item : [cart[item]]  + aisle_mapping[item]   for  item in cart.keys() }
    return dict(reversed(sorted(fulfilment_cart.items())))

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, inventory_item in store_inventory.items():
        cart_item = fulfillment_cart.get(item)
        if cart_item:
            inventory_item[0] -= cart_item[0]
            if inventory_item[0] == 0 :
                inventory_item[0] = "Out of Stock"         
    return store_inventory        
 
