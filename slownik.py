dict = {}

keys = input ("Podaj slowa-klucze slownika: ")
values = input ("Podaj opisy slow-kluczy: ")

keys_list = keys.split() 
values_list = values.split()

print(keys_list)
print(values_list)

for key in keys_list:
    for value in values_list:
        dict[key] = value
        values_list.remove(value)
print(dict)
