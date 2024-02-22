def add(a):
    int_list.append(a)


def s(a):
    sm = 0
    for i in a:
        sm += i
    return sm


def l():
    gl_str = "Local"
    print(gl_str)


def g(number):
    if number < 10:
        return number
    return number % 10 + g(number // 10)


def rev(s):
    if s == "":
        return s
    else:
        return rev(s[1:]) + s[0]


int_list = [10, 20, 30, 40]
a = int(input())
add(a)
print(int_list)

lst = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print(s(lst))

gl_str = "Global"
l()

ricxvi = int(input())
print(g(ricxvi))

a = input()
print(rev(a))
