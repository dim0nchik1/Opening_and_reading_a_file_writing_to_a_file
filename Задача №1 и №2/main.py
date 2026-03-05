from pprint import pprint

cook_book = {}
with open('../Opening_and_reading_a_file_writing_to_a_file/Задача №1 и №2/recipes.txt', encoding='utf-8') as f:
    line = ','.join(f.readlines()).replace('|', '').replace('\n', '').split(',,')
    for i in range(len(line)):
        cook_book[line[i].split(',')[0]] = []
        for x in range(0, int(line[i].split(',')[1])):
            cook_book[line[i].split(',')[0]].append({'ingredient_name':line[i].split(',')[2+x].replace('  ', ',').split(',')[0],
                                                     'quantity': line[i].split(',')[2+x].replace('  ', ',').split(',')[1],
                                                     'measure': line[i].split(',')[2+x].replace('  ', ',').split(',')[2]})

def get_shop_list_by_dishes(dishes, person_count):
    ingredient = {}
    for dish in dishes:
        if dish in cook_book:
            for item in cook_book[dish]:
                if item['ingredient_name'] not in ingredient:
                    ingredient[item['ingredient_name']] = {'measure':item['measure'],
                                                        'quantity': int(item['quantity']) * person_count}
                else:
                    ingredient[item['ingredient_name']]['quantity'] += int(item['quantity']) * person_count
    return ingredient


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))