def process_file(filename):
    seas = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip('"')
            parts = line.split('"')
            name = parts[0].strip('"')
            parts = str(parts[1])
            parts = parts.split(" ")
            parts[2].replace("\n","")
            depth = float(parts[1])
            salinity = float(parts[2])
            seas.append({'название': name, 'глубина': depth, 'соленость': salinity})
    
    return seas

def process_file1(filename):
    seas = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip('"')
            parts = line.split('"')
            name = parts[0].strip('"')
            parts = str(parts[1])
            parts = parts.split(" ")
            parts[2].replace("\n","")
            depth = float(parts[1])
            widht = float(parts[2])
            seas.append({'название': name, 'глубина': depth, 'ширина': widht})
    
    return seas


seas_data = process_file('Моря.txt')
print("--------")

for sea in seas_data:
     print(f"название: {sea['название']}, глубина: {sea['глубина']}, соленость: {sea['соленость']}")


def max1(seas):
    mad = 0
    c = str()
    for item in seas:
        if item['глубина'] > mad:
            mad = item['глубина']
            c = item['название']
    return c
print(max1(seas_data))
seas_data = process_file1('озера.txt')
print("---------")
for lake in seas_data:
     print(f"название: {lake['название']}, глубина: {lake['глубина']}, ширина: {lake['ширина']}")