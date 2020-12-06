

#regular version
f = open("C:/Users/thiemoT480/Desktop/advent_of_code2020/data/day1/data_list.txt", "r")
values = f.readlines()
values = [int(value.rstrip('\n')) for value in values]


counter = 0
for index, value in enumerate(values):
    for value2 in values[index:-1]:
        counter += 1
        if (value + value2) == 2020:
            print(f'value1: {value} value2: {value2}')
            print(f'result: {value * value2}')

print(f'2 values version ran for {counter} iterations')

counter2 = 0
for index,value in enumerate(values):
    for index2, value2 in enumerate(values[index:-1]):
        for value3 in values[index2:-1]:
            counter2 += 1
            if (value+value2+value3) == 2020:
                print(f'value1: {value} value2: {value2} value3: {value3}')
                print(f'result: {value * value2 * value3}')

print(f'3 values version ran for {counter2} iterations')
