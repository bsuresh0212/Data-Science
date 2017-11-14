def swap_case(s):
    string = ""
    for str in s:
        if str.islower():
            string += str.upper()
        elif str.isupper():
            string += str.lower()
        else:
            string += str
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)