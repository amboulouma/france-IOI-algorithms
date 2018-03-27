for ascii in range(ord('a'), ord('z') + 1):
    if chr(ascii) != 'a' and chr(ascii) != 'e' and chr(ascii) != 'o' and chr(ascii) != 'i' and chr(ascii) != 'y' and chr(ascii) != 'u':
        print(chr(ascii), end=" ")