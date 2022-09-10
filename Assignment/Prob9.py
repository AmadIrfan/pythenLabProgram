import Funcs as f
word=input('Enter a word ')

isPalindrome=f.PalindromRecursive(word)
if isPalindrome:
    print('Palindrome')
else:
    print('no Palindrome')