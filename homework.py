def read_cook_book(filename):
    cook_book = {}

    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
                if len(ingredient_info) != 3:
                    continue
                ingredient_name = ingredient_info[0]
                quantity = int(ingredient_info[1].strip())
                measure = ingredient_info[2].strip()
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })

            cook_book[dish_name] = ingredients

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list


def combine_files(file_list, output_filename):
    file_data = []

    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append((file_name, len(lines), lines))

    file_data.sort(key=lambda x: x[1])

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for file_name, line_count, lines in file_data:
            outfile.write(f"{file_name}\n{line_count}\n")
            outfile.writelines(lines)


cook_book = read_cook_book('recipes.txt')
print(cook_book)

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shop_list)

files_to_combine = ['1.txt', '2.txt']
combine_files(files_to_combine, 'result.txt')
