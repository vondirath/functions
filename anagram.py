# brute force

def get_value(s):
    value = []
    for i in s:
        value.append(ord(i))
    return sum(value)


def isanagram(s, t):
    if s is None or t is None or s == '' or t == '':
        return False
    lent = len(t)
    if lent > len(s) or lent > 20 or len(s) > 20:
        return False
    anagram = get_value(t)

    for i in range(0, lent + 1):
        if get_value(s[i: i + lent]) == anagram:
            return True
    return False


# O(n)? 
# test cases
# true
print isanagram("banana", 'nana')
# false
print isanagram("longstring", "yell")
# false
print isanagram("1234", "seven")
print isanagram('', 'k')
print isanagram('aaaaaaaaaaaaaaaaaaaa', 'bbbb')