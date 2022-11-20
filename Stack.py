stk_size = eval(input("Enter The Size Of Stack.\t"))
stk = []

while True:
    chce = int(input('''
    1 Push Element
    2 Pop Element
    3 Peek Element
    4 First Element
    5 Display Stack
    6 Exit Oeration
    '''))

    if chce == 1:
        if len(stk) == stk_size:
            print("The Stack Is Already Full.")
        else:
            elmnt = input("Enter The Element To Be Insert:\t")
            stk.append(elmnt)    
            print("The Values Of Stack are:\t",stk)
    elif chce == 2:
        if len(stk) == 0:
            print("The Stack Is Already Empty.")
        else:
            delelmnt=stk.pop()
            print("The Deleted Element:\t",delelmnt)
            print("Print All The Values Of Stack After Poping The Element:\t",stk)
    elif chce == 3:
        if len(stk) == 0:
            print("The Stack Is Already Empty.")
        else:
            print("The Peek Element of Stack is:\t",stk[-1])
            print("Print All The Values Of Stack:\t",stk)
    elif chce == 4:
        if len(stk) == 0:
            print("The Stack Ia Already Empty.")
        else:
            print("The First Element of Stack is:\t",stk[0])
            print("Print All The Values Of Stack:\t",stk)
    elif chce == 5:
        if len(stk) == 0:
            print("The Stack Ia Already Empty.")
        else:
            print("Print All the Values of Stack:\t",stk)
    elif chce == 6:
        break
    else:
        print("Invalid Choice")