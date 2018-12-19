import sys
import re
from multiprocessing import Process

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
#looper to prevent stack growing too large.
def looper(s, msg):
    n = list(s)
    print("In thread")
    while(True):
        if(checkchars(n)):
            break
    print(msg)
    print("Length of string is now " + str(len(n))+"\n")


if __name__ == '__main__':

    sys.setrecursionlimit(50000)
    f = open('day5/input.txt', 'r')
    data = f.readline()
    # sample data for testing
    # data = "dabAcCaCBAcCcaDA"

    # Day 5 solution 1
    # If an upper and lower letter are the same letter (type) but different polarity (upper/lower)
    # then destroy them (remove them) from the string.
    # Comment out if only looking for solution 2 of day 5
    d = list(data)
    while(True):
        if (checkchars(d)):
            break
    print("Number left = ", len(d))

    # Day 5 solution 2
    # Used multiprocess library to fork off 26 children to process at the same time
    # This saves time especially with my Ryzen 16 Thread beast!
    lowerChar = 'a'
    upperChar = 'A'
    length = 0
    # need to remove each 26 letters at one time and then run the checkchars function on each one to see which one gives us the smallest lenght. 
    for i in range(26):
        searchText = "["+lowerChar+upperChar+"]"
        msg = "Did search with removing of " + searchText + "\n"
        t = re.sub(searchText, '', data)
        lowerChar = chr(ord(lowerChar) + 1)
        upperChar = chr(ord(upperChar) + 1)

        p = Process(target=looper, args=[t, msg])
        p.start()
    