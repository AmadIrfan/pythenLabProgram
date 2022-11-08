from funcs import PalindromRecursive
word=input('Enter a word ')

isPalindrome=PalindromRecursive(word)
if isPalindrome:
    print('Palindrome')
else:
    print('no Palindrome')