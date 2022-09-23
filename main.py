cook_book = {}

with open('date.txt') as file:
    for line in file:
        ingridients = []
        name = line.replace('\n', '')
        emp_count = file.readline()
        for i in range(int(emp_count)):
            emp = file.readline().replace('\n','')
            ing, mass, wtf = emp.split(' | ')
            lst = {}
            lst['ingredient_name'] = ing
            lst['quantity'] = mass
            lst['measure'] = wtf
            ingridients.append(lst)
        cook_book[name] = ingridients
        file.readline()

def cook(dishes, person_count):
    eat = []
    for name, ingr in cook_book.items():
        if name == dishes:
            for ing in ingr:
                app = ''
                app += str((ing['ingredient_name']) + ' ' + (str(int(ing['quantity']) * person_count)) + ' ' + (ing['measure']))
                eat.append(app)
    for i in eat:
        print(i)

def get_shop_list_by_dishes(dishes, person_count):
    if type(dishes) == str:
        cook(dishes, person_count)
    if type(dishes) == list:
        for i in dishes:
            print()
            cook(i, person_count)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
