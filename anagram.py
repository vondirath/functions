# brute force

def get_value(s):
    value = []
    for i in s:
        value.append(ord(i))
    return sum(value)


def isanagram(s, t):
    lent = len(t)
    anagram = get_value(t)

    for i in range(0, lent + 1):
        if get_value(s[i: i + lent]) == anagram:
            return True
    return False



# test cases
# true
print isanagram("banana", 'nana')
# false
print isanagram("longstring", "yell")
# false
print isanagram("1234", "seven")