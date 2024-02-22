import random

a = int(input())
sum = 0
for i in range(a):
    sum += i
print(sum)

a = int(input())
while a != 0:
    print(a)
    a -= 1

a = random.randint(0, 1000)
while True:
    guess = int(input())
    if a == guess:
        print("გამოიცანი")
        break
    elif a < guess:
        print("ნაკლები")
    else: print("მეტი")

total_sum = 0
while True:
    insert = input()
    if insert == "sum":
        print(total_sum)
        break
    elif insert.isdigit() and int(insert) > 0:
        total_sum += int(insert)
