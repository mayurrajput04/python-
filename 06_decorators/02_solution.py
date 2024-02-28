def debug(func):
    def wrapper(*args , **kwargs):
        args_value = ",".join(str(arg) for arg in args)
        kwargs_value = ",".join(f"{k} = {v} " for k,v in kwargs.items())
        print(f"calling {func.__name__} with {args_value} args and {kwargs_value} kwargs")
        return func(*args ,**kwargs)
    return wrapper






@debug
def hello():
    print("hello")

@debug
def greet(name , greeting = "Hi"):
    print(f"{greeting} {name} !")

hello()

greet("mayur" , greeting = "hello")