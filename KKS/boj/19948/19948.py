poem = input()
space = int(input())
keyboard = list(map(int,input().split()))

def check_validity(poem, space):
    ans = ("".join(word[0].upper() for word in poem.split()))
    pre = poem[0]
    if keyboard[ord(pre.upper()) - 65] - 1 < 0:
        return print(-1)
    else:
        keyboard[ord(pre.upper()) - 65] -= 1

    for letter in poem[1:]:
        if pre == letter:
            continue
        elif letter == ' ':
            space -= 1
            if space < 0:
                return print(-1)
            else:
                pre = letter
        else:
            if keyboard[ord(letter.upper()) - 65] - 1 < 0:
                return print(-1)
            else:
                pre = letter
                keyboard[ord(letter.upper()) - 65] -= 1

    pre = ans[0]
    if keyboard[ord(pre.upper()) - 65] - 1 < 0:
        return print(-1)
    else:
        keyboard[ord(pre.upper()) - 65] -= 1
    for letter in ans[1:]:
        if pre == letter:
            continue
        elif letter == ' ':
            space -= 1
            if space < 0:
                return print(-1)
            else:
                pre = letter
        else:
            if keyboard[ord(letter.upper()) - 65] - 1 < 0:
                return print(-1)
            else:
                pre = letter
                keyboard[ord(letter.upper()) - 65] -= 1
    return print(ans)

check_validity(poem, space)