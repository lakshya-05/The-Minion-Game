def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    ks = 0
    ss = 0
    l = len(string)
    for i in range(len(string)):
        if string[i] in vowels:
            ks = ks + l - i
        else:
            ss = ss + l - i

    if ks > ss:
        print("Kevin {}".format(ks))
    elif ss > ks:
        print("Stuart {}".format(ss))
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
