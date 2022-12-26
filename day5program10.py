def CheckPalindrome(n):
    b=input(n)
    if b==b[::-1]:
        return 'yes'
    else:
        return 'no'
inp=input("Enter a number:")
print(CheckPalindrome(inp))

