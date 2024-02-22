print(input().encode('utf-8'))

str = input().strip().lower()
if 'python' not in str:
    str += ' Python'
print(str.replace("python", "Python"))

a = input()
print(a[0:int((len(a)+1)/2)])

if input().isdigit():
    print("Valid")
else: print("Invalid")

str2 = input()
str2_bt = bytes(str2)
print(str2_bt, str2_bt.decode("utf-8"))
