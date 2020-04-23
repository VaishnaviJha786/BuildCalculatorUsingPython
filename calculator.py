import re
print ("Our Magical Calculator")
print("Type '' to exit\n")

previous=0
run= True


def do_math():
    global run
    global previous
    equation=""
    if previous==0:
        equation=input("Enter Equation   :")
    else:
        equation=input(str(previous))
        
    if equation=='x':
        print("Good Bye!")
        run= False
    else:
        equation=re.sub('[a-zA-z,.:()" "#&@]','',equation)
        if previous ==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)


while run:
    do_math()
             
    
