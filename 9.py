import functools
import numbers


def zp(lst1, lst2):
    return zip(lst1, lst2)


print(list(zp(lst1=[1, 2, 3], lst2=['a', 'a', 'c'])))


def namravli(lst):
    return functools.reduce(
        lambda a, b: a * b if isinstance(a, numbers.Number) and isinstance(b, numbers.Number) else Exception(
            "TypeError"),
        lst)


lis = [1, 2, 3, 4, 5, 'a']
print(namravli(lis))

lit = [1, 2, 3, 4, 5, 6, 7]
kenti = list(filter(lambda n: n % 2 != 0, lit))
print(kenti)


def filter_strings(input_list, target):
    return list(filter(lambda s: target in s, input_list))


lt = ['hello', 'world', 'coding', 'nod', 1]
target = "ing"
try:
    print(filter_strings(lt, target))
except TypeError:
    print("something is not correct format")
