que_size=eval(input("Enter The Size Of Stack.:\t"))
que=[]
enque = 0
deque = 0
while True:
    chce = int(input('''
    1 Insert Element
    2 Delete Element
    3 Front Element
    4 Rear Element
    5 Display Stack
    6 Exit Oeration
    '''))

    if chce == 1:
        if len(que) == que_size:
            print("The Queue Is Already Full.")
        else:
            elmnt = input("Enter The Element To Be Insert:\t")
            que.append(elmnt)    
            print("The Values of Queue:\t",que)
            enque +=1
    elif chce == 2:
        if len(que) == 0:
            print("The Queue Is Already Empty.")
        else:
            delelmnt = que.pop(0)
            print("The Deleted Element:\t",delelmnt)
            print("Print All The Values Of Queue After Poping The Element:\t",que)
            enque -=1
    elif chce == 3:
        if len(que) == 0:
            print("The Queue Is Already Empty.")
        else:
            print("The Front Element Of Queue is:\t",que[0])
            print("Print All The Values Of Queue:\t",que)
    elif chce == 4:
        if len(que) == 0:
            print("The Queue Is Already Empty.")
        else:
            print("The Rear Element of Queue is",que[-1])
            print("Print All The Values Of Queue:\t",que)
    elif chce == 5:
        if len(que) == 0:
            print("The Queue Is Already Empty.")
        else:
            print("Print All The Values Of Queue:\t",que)
    elif chce == 6:
        break
    else:
        print("Invalid Choice")