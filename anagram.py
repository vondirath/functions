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

# alt
def question12(s, t):
    if s is None or t is None or s == '' or t == '':
        return False
    lent = len(t)
    if lent > len(s):
        return False

    for i in range(0, lent + 1):
        if ''.join(sorted(s[i: i + lent])) == ''.join(sorted(t)):
            return True
    return False

# alt 2
def hashmap(str):
    alphabetMap = {
        'a': 2, 
        'b': 3, 
        'c': 5,
        'd': 7, 
        'e': 11, 
        'f': 13,
        'g': 17, 
        'h': 19, 
        'i': 23,
        'j': 29, 
        'k': 31, 
        'l': 37,
        'm': 41, 
        'n': 43,
        'o': 47,
        'p': 53,
        'q': 59,
        'r': 61,
        's': 67,
        't': 71,
        'u': 73,
        'v': 79,
        'w': 83,
        'x': 89,
        'y': 97,
        'z': 101,
        'A': 103,
        'B': 107,
        'C': 109,
        'D': 113,
        'E': 127,
        'F': 131,
        'G': 137,
        'H': 139,
        'I': 149,
        'J': 151,
        'K': 163,
        'L': 167,
        'M': 173,
        'N': 179,
        'O': 181,
        'P': 191,
        'Q': 193,
        'R': 197,
        'S': 199,
        'T': 211,
        'U': 223,
        'V': 227,
        'W': 229,
        'X': 233,
        'Y': 239,
        'Z': 241
    }

    return reduce(lambda memo, char: memo * alphabetMap[char], list(str), 1);

def question1(s, t):
    length = len(t)
    anagram = hashmap(t)

    for i in xrange(0, len(s) - length):
        if hashmap(s[i: i + length]) == anagram:
            return True
    return False

# false
print question1("hhabz", "acy")
# true
print question1("banana", 'nana')


