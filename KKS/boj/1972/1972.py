import sys
input = sys.stdin.readline

def check_surprise(word):
    N = len(word)
    for dist in range(1, N):
        wordset = set()
        for i in range(0, N-dist):
            d_word = word[i]+word[i+dist]
            if d_word in wordset:
                return False
            else:
                wordset.add(d_word)
    return True



while True:
    word = input().rstrip()
    if word == "*":
        exit(0)
    else:
        if check_surprise(word):
            print(f"{word} is surprising.")
        else:
            print(f"{word} is NOT surprising.")
