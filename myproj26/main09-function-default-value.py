def get_default_value():
    print("get_default_value()를 호출")
    return 10


def hello(name, age=get_default_value()):
    print(f"안녕. 나는 {name}이야. {age}살이지.")


hello("Tom")
hello("Steve")
hello("John")
