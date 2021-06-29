'''stack data structures are those that are stacked upon one another just like we keep books
we can access only the top element in stacks.
stacks are linear data structures
we need the following functions to implement stacks
1.isEmpty(s)
2.Push(s,i)
3.Pop(s)
4.Peek(s)
5.Display(s)
'''
# implementing stack

S=[] #stack
top=None
def isEmpty(stk):
    "Returns if a stack is empty or not"

    # return stk==[]
    if stk==[]:
        return True
    else:
        return False


def push(stk,item):

    stk.append(item)
    top=len(stk)-1

def s_pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        i = stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
    return i


def peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]


def display(stk):
    if isEmpty(stk):
        print("Underflow")
    else:
        top=len(stk)-1
        print(stk[top],"<----TOP")
        for i in range(top-1,-1,-1):
            print(stk[i])


if __name__=="__main__":
    while True:
        print("STACK IMPLEMENTATION")
        print("1.PUSH")
        print("2.POP")
        print("3.DISPLAY")
        print("4.PEEK")
        print("5.EXIT")
        chs=[1,2,3,4,5]
        ch=int(input("Enter your choice(1-5):\n"))
        if ch in chs:
            if ch==1:
                i=int(input("Enter your number:\n"))
                push(S,i)
                print(f"succesfully pushed {i}")
                input("press any key to continue")

            elif ch==2:
                # i=int(input("Enter your number:\n"))/
                item=s_pop(S)
                if item=="Underflow":
                    print("Underflow ! cannot pop the stack")
                else:

                    print(f"succesfully popped {item}" )
                input("press any key to continue")
            elif ch==3:
                # i=int(input("Enter your number:\n"))
                display(S)
                input("press any key to continue")

            elif ch == 4:
                print(peek(S))
                input("press any key to continue")

            elif ch == 5:
                quit()
