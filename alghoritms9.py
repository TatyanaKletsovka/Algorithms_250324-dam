
def add_el(new_lst, new_el):
    new = new_el + 1
    new_lst.append(new)
    return new_lst



lst = [1]
element = 2
# element = element + 4
print(add_el(lst, element))
print(lst)
print(element)
