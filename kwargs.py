def func(*args,**kwargs):
    print('I like {} {}'.format(args[0], kwargs['food']))

func(10,20,30,food='chicken')