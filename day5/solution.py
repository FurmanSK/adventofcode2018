import sys
sys.setrecursionlimit(50000)
f = open('day5/input.txt', 'r')
data = f.readline()
# sample data for testing
# data = "dabAcCaCBAcCcaDA"

def checkchars(s):
    #for i, character in enumerate(s):
    for i, char in enumerate(s):
        # check first if next value is not end of string
        if i == len(s)-1:
            print("Made it to end\n")
            return True
        if char.isupper():
            # then check if next element is lower
            if s[i+1].islower():
                #if so then go to upper and compare
                if s[i+1].upper() == s[i]:
                    del s[i+1]
                    del s[i]
                    # after removing. Call checkchars(l) again
                    #checkchars(s)
                    return False

        if char.islower(): # if current char is lower
            if s[i+1].isupper(): # then if next char is upper check if as lower its equal
                if s[i+1].lower() == s[i]:
                    del s[i+1]
                    del s[i]
                    # checkchars(s)
                    return False

    

# If an upper and lower letter are the same letter (type) but different polarity (upper/lower)
# then destroy them (remove them) from the string.
d = list(data)
while(True):
    print("lenght = " , len(d))
    if (checkchars(d)):
        break
print("Number left = ", len(d))