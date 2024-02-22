import re

list = []
while True:
    print("a – append\nr – remove\ne – exit")
    command = input()
    if command == 'r':
        print("What number should be removed?")
        temp = input()
        if temp.isdigit():
            cifri = int(temp)
            if cifri in list:
                list.remove(cifri)
            else:
                print("Input is not in list")
        else:
            print("Input is not number")
    elif command == 'a':
        print("What number should be added?")
        temp = input()
        if temp.isdigit():
            list.append(int(temp))
        else:
            print("Input is not number")
    elif command == 'e':
        print(list)
        break
    else:
        print("Invalid command")

my_list = [43, '22', 12, 66, 210, ["hi"]]
for i in range(len(my_list)):
    if my_list[i] == 210:
        print(i)
my_list.append("hello")
my_list.pop(2)
print(my_list)
my_list_2 = my_list.copy()
my_list_2.clear()
print(my_list, my_list_2)

a = input()
if not re.match(r"^[(][\d0-9]{3}[)] [\d0-9]{3}-[\d0-9]{3}$", a):
    print('Invalid format')
else:
    print(a)
