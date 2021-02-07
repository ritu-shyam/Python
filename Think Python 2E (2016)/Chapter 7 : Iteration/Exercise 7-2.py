# Eval function

def eval_loop() :
    a = input('Enter a string :')
    while a != 'done' :
        e = eval(a)
        print(e)
        a = input('Enter a string :')
    return e

eval_loop()
