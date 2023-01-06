path = "C:/Users/pc/Desktop/python_projects/과제/jan6/PJT-01/data/fruits.txt"
berry = {}

with open(path, "r") as f:
    fruits_list = f.read()                # 3542개의 글자가 있음. 
    fruits = fruits_list.split("\n")       # 394개의 과일이 있음. 
    

    for fruit in fruits:                       #각 과일마다 berry로 끝나면, 그것을 기록함. 
        if fruit.endswith("berry") == True:    #'berry'로 끝나는 과일을 찾음.
            if fruit in berry:
                berry[fruit] += 1
            else:
                berry[fruit] = 1
    
with open("04.txt", "w") as f:
    for key, value in berry.items():
        f.write(key + " " + str(value) + "\n")