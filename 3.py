arr = [44, 23, 11, 8, 20, 56, 33, 55]
contains = False
a = eval(input())
for i in arr:
    if a == i:
        contains = True
        break

if contains:
    print("The number in list")
else:
    print("The number not in list")

a = int(input())
if a % 2 == 0:
    print("The number is even")
else: print('The number is odd')

st1 = 'wow'
st2 = st1
if st1 is st2:
    print("Same object")
else: print("Different object")

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
a = int(input())
printed = False
if num_list[2] < a < num_list[-1]:
    print("More than list elements")
    printed = True
if a == num_list[5]:
    print("Equal")
    printed = True
if not printed:
    print("None of the conditions were met")