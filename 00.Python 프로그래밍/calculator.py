# calculator.py

# 함수 정의
def add(a,b):
    c = a + b
    print('add is called!')
    return c

def subtract(a,b):
    c = a - b
    print('subtract is called!')
    return c

def multiply(a,b):
    c = a * b
    print('multiply is called!')
    return c

def divide(a,b):
    c = a / b
    print('divide is called!')
    return c

# print('calculator:', __name__)

if __name__ == '__main__':
    ret = add(10,20)
    print(ret)






