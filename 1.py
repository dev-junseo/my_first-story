def f(x):
    print("f 시작")
    return x + 1
    print("f 끝")
def g(x):
    print("g 시작")
    return x*x + 1
    print("g 끝")

print(f(3))
print(g(4))
print(f(3) + g(4))

def print_square(x):
    print(x * x)
def get_square(x):
    return x * x

print(print_square(3))
print(get_square(3))

def print_hello():
    print("Hello")

print(print_hello())

print("비주얼스튜드오 코드와의 첫만남")
print("hello")
print("오늘은 3월 16일")
a = 11
b = 15
print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a % b)

def print_full_name(first_name, last_name):
    print("%s , %s" %(last_name, first_name))
    
print(print_full_name("준서", "하"))

def your_ID(name, ID, passward = 0000):
    print("Your name is %s" %(name))
    print("Your ID is %s" %(ID))
    print("Your passward is %d" %(passward))

your_ID("가나다", "aaaa")
print()
your_ID("라마바", "bbbb", 1234)


def calculate_change(payment, cost):
    value1 = payment - cost               #총 거스름돈
    value2 = int(value1/50000)            #5만원 지폐 갯수
    value3 = value1 - value2 * 50000      #그 나머지
    value4 = int(value3/10000)            #만원 지폐 갯수
    value5 = value3 - value4 * 10000      #그 나머지
    value6 = int(value5/5000)             #오천원 지폐 갯수
    value7 = value5 - value6 * 5000       #그 나머지
    value8 = int(value7/1000)             #천원 지폐 갯수
    print("50000원 지폐 : %d장" %(value2))
    print("10000원 지폐 : %d장" %(value4))
    print("5000원 지폐 : %d장" %(value6))
    print("1000원 지폐 : %d장" %(value8))

#test
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

print()