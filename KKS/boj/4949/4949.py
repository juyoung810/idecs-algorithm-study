stack = []
while True:
    query = input()
    if query == '.':
        break
    paren_dict = {'(': ')', '[': ']'}
    for i in range(len(query)):
        if query[i] == '.':
            if len(stack) == 0:
                print("yes")
                stack = []
            else:
                print("no")
                stack = []
        if query[i] in ["(", "["]:
            stack.append(query[i])
        elif query[i] in [")", "]"]:
            if len(stack) >= 1:
                temp = stack.pop()
                if paren_dict[temp] != query[i]:
                    print("no")
                    stack = []
                    break
            else:
                print("no")
                stack = []
                break

