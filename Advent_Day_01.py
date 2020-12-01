with open("day_1_input.txt") as raw_data:
    data = raw_data.read()
arr = [int(x) for x in data.split('\n') if x]

###printing the multiplication of the two numbers
def day1_1():
    for x in arr:
        for y in arr:
            if x + y == 2020:
                print('x:',x,'y:',y)
                return x * y

###printing the multiplication of the three numbers
def day1_2():
    for x in arr:
        for y in arr:
            for z in arr:
                if x + y + z == 2020:
                    print('x:',x,'y:',y,'z:',z)
                    return x * y * z
                
                
print(f"Day 1.1: {day1_1()}")
print(f"Day 1.2: {day1_2()}")
