
n = 0

with open("C:/Users/pc/Desktop/python_projects/과제/jan6/PJT-01/data/fruits.txt", 'r') as f:
    fruits_list = f.read()
    fruits = fruits_list.split("\n")
    for fruit in fruits:
        n += 1

with open("02.txt", "w") as f:
    f.write(f'{n}')





