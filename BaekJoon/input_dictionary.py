def hello():
    print("Hello, World!")

def add(a, b):
    print(f"{a} + {b} = {a+b}")

def multiply(a, b):
    print(f"{a} x {b} = {a*b}")

my_dict = {"hello": hello, "add": add, "multiply": multiply}

input_value = input("Enter a key (hello, add, or multiply): ")

if input_value in my_dict:
    my_dict[input_value]()  # 해당하는 함수 실행
else:
    print("The key is not in the dictionary.")
