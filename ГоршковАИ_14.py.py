def file_processor(filename):
    """Функция 1: Обработчик файлов"""
    data_list = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            parts = line.split('"')
            name = parts[1].strip()
            numbers = parts[2].strip().split()
            data_list.append([name] + numbers)
    
    return data_list


def process_seas():
    """Функция 2: Обработка морей"""
    seas = []
    data = file_processor('Моря.txt')
    
    for item in data:
        name = item[0]
        depth = float(item[1])
        salinity = float(item[2])
        seas.append({'название': name, 'глубина': depth, 'соленость': salinity})
    
    return seas


def process_lakes():
    """Функция 3: Обработка озер"""
    lakes = []
    data = file_processor('озера.txt')
    
    for item in data:
        name = item[0]
        depth = float(item[1])
        width = float(item[2])
        lakes.append({'название': name, 'глубина': depth, 'ширина': width})
    
    # Находим самое глубокое озеро
    deepest_lake = max(lakes, key=lambda x: x['глубина'])
    deepest_lake_copy = deepest_lake.copy()
    deepest_lake_copy['статус'] = 'самое глубокое озеро'
    lakes.append(deepest_lake_copy)
    
    return lakes


def process_rivers():
    """Функция 4: Обработка рек"""
    rivers = []
    data = file_processor('реки.txt')
    
    for item in data:
        name = item[0]
        volume = float(item[1])
        fill_time = float(item[2])
        creation_year = item[3]
        lengh = item[4]
        rivers.append({
            'название': name, 
            'объем': volume, 
            'время наполнения': fill_time, 
            'год создания': creation_year,
            'длина реки': lengh
        })
    
    return rivers


def process_reservoirs():
    """Функция 5: Обработка водохранилищ"""
    reservoirs = []
    data = file_processor('водохранилища.txt')
    
    for item in data:
        name = item[0]
        length = float(item[1])
        water_flow = item[2]
        reservoirs.append({
            'название': name, 
            'длина': length, 
            'расход воды': water_flow
        })
    
    return reservoirs


def save_to_file(filename, data_line):
    """Сохранение новой записи в файл"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(data_line + '\n')


def add_lake():
    """Добавление нового озера"""
    print("\n--- Добавление нового озера ---")
    name = input("Введите название озера: ")
    depth = input("Введите глубину (м): ")
    width = input("Введите ширину (м): ")
    
    data_line = f'"{name}" {depth} {width}'
    save_to_file('озера.txt', data_line)
    print("Озеро успешно добавлено!")


def add_sea():
    """Добавление нового моря"""
    print("\n--- Добавление нового моря ---")
    name = input("Введите название моря: ")
    depth = input("Введите глубину (м): ")
    salinity = input("Введите соленость (‰): ")
    
    data_line = f'"{name}" {depth} {salinity}'
    save_to_file('Моря.txt', data_line)
    print("Море успешно добавлено!")


def add_reservoir():
    """Добавление нового водохранилища"""
    print("\n--- Добавление нового водохранилища ---")
    name = input("Введите название водохранилища: ")
    length = input("Введите длину (км): ")
    water_flow = input("Введите расход воды: ")
    
    data_line = f'"{name}" {length} {water_flow}'
    save_to_file('водохранилища.txt', data_line)
    print("Водохранилище успешно добавлено!")


def add_river():
    """Добавление новой реки"""
    print("\n--- Добавление новой реки ---")
    name = input("Введите название реки: ")
    volume = input("Введите объем (м³): ")
    fill_time = input("Введите время наполнения (ч): ")
    creation_year = input("Введите год создания: ")
    river_length = input("Введите длину реки: ")
    
    data_line = f'"{name}" {volume} {fill_time} {creation_year} {river_length}'
    save_to_file('реки.txt', data_line)
    print("Река успешно добавлено!")


def display_all_data():
    """Функция 6: Вывод всех данных"""
    seas_data = process_seas()
    lakes_data = process_lakes()
    rivers_data = process_rivers()
    reservoirs_data = process_reservoirs()
    
    print("=" * 50)
    print("МОРЯ")
    print("=" * 50)
    for sea in seas_data:
        print(f"Название: {sea['название']}")
        print(f"  Глубина: {sea['глубина']} м")
        print(f"  Соленость: {sea['соленость']} ‰")
        print("-" * 30)
    
    print("\n" + "=" * 50)
    print("ОЗЕРА")
    print("=" * 50)
    for lake in lakes_data:
        print(f"Название: {lake['название']}")
        print(f"  Глубина: {lake['глубина']} м")
        if 'ширина' in lake:
            print(f"  Ширина: {lake['ширина']} м")
        if 'статус' in lake:
            print(f"  Статус: {lake['статус']}")
        print("-" * 30)
    
    print("\n" + "=" * 50)
    print("РЕКИ")
    print("=" * 50)
    for river in rivers_data:
        print(f"Название: {river['название']}")
        print(f"  Объем: {river['объем']} м³")
        print(f"  Время наполнения: {river['время наполнения']} ч")
        print(f"  Год создания: {river['год создания']}")
        print(f"  Длина реки: {river['длина реки']}")
        print("-" * 30)
    
    print("\n" + "=" * 50)
    print("ВОДОХРАНИЛИЩА")
    print("=" * 50)
    for reservoir in reservoirs_data:
        print(f"Название: {reservoir['название']}")
        print(f"  Длина: {reservoir['длина']} км")
        print(f"  Расход воды: {reservoir['расход воды']}")
        print("-" * 30)


def show_menu():
    """Отображение главного меню"""
    while True:
        print("\n" + "=" * 50)
        print("ГЛАВНОЕ МЕНЮ - УПРАВЛЕНИЕ ВОДНЫМИ ОБЪЕКТАМИ")
        print("=" * 50)
        print("1 - Просмотреть все данные")
        print("2 - Добавить новое озеро")
        print("3 - Добавить новое море")
        print("4 - Добавить новое водохранилище")
        print("5 - Добавить новую реку")
        print("0 - Выход")
        print("-" * 50)
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            display_all_data()
        elif choice == '2':
            add_lake()
        elif choice == '3':
            add_sea()
        elif choice == '4':
            add_reservoir()
        elif choice == '5':
            add_river()
        elif choice == '0':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")



show_menu()