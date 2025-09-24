def process_file(filename):
    times = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # line = line.strip()
            hours, minutes, seconds = map(int, line.split())
            times.append((hours, minutes, seconds))
    times.sort()
    result = []
    for h, m, s in times:
        result.append({'часы': h, 'минуты': m, 'секунды': s})
    
    return result

times_data = process_file('время.txt')
for time in times_data:
    print(f"часы: {time['часы']}, минуты: {time['минуты']}, секунды: {time['секунды']}")