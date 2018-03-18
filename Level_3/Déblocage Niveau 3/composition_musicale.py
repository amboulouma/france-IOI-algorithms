def if_double(c, s):
    if s[c] == s[c+1]: return True
    else: return False


def if_double_found(sl):
    for cl in range(len(sl) - 1):
        if if_double(cl, sl): return True


s = list(input())
while if_double_found(s):
    for c in range(len(s) - 1):
        if if_double(c, s):
            del s[c]
            del s[c]
            break
print(''.join(s))
