b=str(input())
list=['a','e','i','o','u']
splchr=['!','$','&']
if b in list:
    print("Vowel")
elif b in splchr:
    print("Invalid")
elif b is not list:
    print("Consonant")
