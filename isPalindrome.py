def isPalindrome(x):
    isPld = False
    if x>=0:
        strX = str(x)
        if strX == strX[::-1]:
            isPld = True
    return isPld

print(isPalindrome(1002341))