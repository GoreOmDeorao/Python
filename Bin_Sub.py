def dectobin(num):
    ans = ""
    while num > 0:
        rem = num % 2
        ans = str(rem) + ans
        num = num // 2
    return int(ans)

def bintodect(num):
    ans = 0
    base = 1
    while num > 0:
        rem = num % 10
        ans = ans + rem * base
        base = base * 2
        num = num // 10
    return ans

def subt(a, b):
    return dectobin(a - b)

if __name__ == "__main__":
    print(subt(18, 11))

