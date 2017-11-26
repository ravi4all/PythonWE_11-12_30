# Readline and Readlines
with open('data.txt') as file:
    for i in range(5):
        data = file.readline()
        print(data)

with open('data.txt') as file_1:
    data = file_1.readlines()
    for d in data:
        print(d)
