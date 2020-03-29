import pprint
stuff= {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(stuff):
    print("Inventory:")
    value_count=0
    for k,v in stuff.items():
        print(k,v)
        value_count=value_count+v
    print("Total no. of items: ", value_count)


display_inventory(stuff)