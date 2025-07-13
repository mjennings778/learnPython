
file = f"test.txt"
with open(file, 'w') as file:
    for i in range(0, 4096):
        file.write(f'{i}\n')