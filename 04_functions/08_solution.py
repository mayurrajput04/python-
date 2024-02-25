def dict(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key} : {value}")

dict(name = 'mayur', gender = "male")
dict(name='suraj')
dict(name ='shanta' ,gender = 'female' , relation = 'mother')