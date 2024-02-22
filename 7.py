def fib_siq(n):
    if n == 1 or n == 2:
        return 1
    elif n < 0:
        print("ფიბონაჩი უარყოფითებში ?")
    elif n == 0:
        return 0
    else:
        return fib_siq(n-1) + fib_siq(n-2)


def anagram (st1, st2):
    for i in st1:
        if len(st1) != len(st2):
            return False
        elif st1.count(i) != st2.count(i):
            return False
    return True


def factorial(n):
    if n == 0:
        return 1
    else:
        fac = 1
        while n != 0:
            fac = fac * n
            n -=1
        return fac


def counter(str, char):
    cnt = 0
    for i in str:
        if char == i:
            cnt +=1
    return cnt


a = int(input("ფიბონაჩის რიცხვი "))
while a > 0:
    print(fib_siq(a))
    a -= 1


st1 = input("სიტყვა 1 ")
st2 = input("სიტყვა 2 ")

if anagram(st1, st2):
    print("არის ანაგრამა")
else:
    print("არ არის ანაგრამა")

print(factorial(int(input("ფაქტორიზაცია "))))



print(counter(input("სიტყვა: "), input("სიმბოლო: ")))
