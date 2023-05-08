import time

STACKHIGHT = 5
moves = 0

##ragma region Graphics
showGraphic = True
# test
stacks = [[0 for __ in range(STACKHIGHT)] for _ in range(3)]


def printElement(elementSize):
    dif = (STACKHIGHT * 2 - elementSize)
    lenofspaces = dif // 2  # Wie viele leerzeichen müssen links von einem element dargestellt werden

    print(" " * lenofspaces + "=" * elementSize + " " * lenofspaces, end=" ")


def moveStackElement(from_stack, to_stack):
    global moves
    moves += 1
    # ==========================
    # find the index of the highest existing element
    position = STACKHIGHT - 1
    while True:
        if stacks[from_stack - 1][position]:
            break
        position -= 1

    # find the index of the lowest freeplace
    position2 = 0
    while True:
        if not stacks[to_stack - 1][position2]:
            break
        position2 += 1

    # Swap positions -> a,b = b,a
    tmp = stacks[to_stack - 1][position2]
    stacks[to_stack - 1][position2] = stacks[from_stack - 1][position]
    stacks[from_stack - 1][position] = tmp


def printStacks():
    # ===========================
    # Print Stacks
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    for i in range(STACKHIGHT - 1, -1, -1):  # (int i = STACKHIGHT - 1; i >= 0; i--)
        for j in range(3):  # (int j = 0; j < 3; j++)
            printElement(stacks[j][i])
        print()


def moveAndPrint(_from, to):
    moveStackElement(_from, to)
    if showGraphic:
        printStacks()


# pragma endregion


# Logic
def move(n, from_stack, to_stack, tmp_stack):
    if n == 1:  # If the Stack has only one element we can move the element
        moveAndPrint(from_stack, to_stack)
        return
    # If not, we want to move all elements above the lowest element to a temporary stack
    # so we can move the lowest element to the goal stack
    move(n - 1, from_stack, tmp_stack, to_stack)  # We can use the to_stack as temporary stack.
    moveAndPrint(from_stack, to_stack)
    move(n - 1, tmp_stack, to_stack, from_stack)


# Then we want to move the elements we moved to the temp_stack to the top of our element in the goal stack.


def fillstacks():  # stack[0] = {1,2,...,STACKHIGHT}, stack[1] = stack[2] = {0,...,0}

    for i in range(STACKHIGHT):  # (int i = 0; i < STACKHIGHT; i++)
        stacks[0][i] = (STACKHIGHT - i) * 2
        stacks[1][i] = stacks[2][i] = 0  # make sure the lists are "empty"


if __name__ == '__main__':
    T_start = time.time()
    fillstacks()
    printStacks()
    move(STACKHIGHT, 1, 3, 2)
    T_stop = time.time()
    print(f"\n {moves} moves in {T_stop - T_start} milliseconds with printing={'TRUE' if showGraphic else 'FALSE'}")

