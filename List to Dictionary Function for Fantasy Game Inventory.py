from collections import Counter

def displayInventory(stuff):
    print("Inventory:")
    value_count=0
    for k,v in stuff.items():
        print(k,v)
        value_count=value_count+v
    print("Total no. of items: ", value_count)

def addToInventory(inv, dragonLoot):
    cnt=Counter()
    new={}
    for i in dragonLoot:
        cnt[i]+=1

    for i in cnt.keys():
        if i not in inv:
            new[i]=cnt[i]
        else:
            new[i]=inv[i] + cnt[i]

    return new


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)