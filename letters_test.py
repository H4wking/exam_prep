from letters import First, Second


a1 = First('miraculously') # First's constructor takes variable of arguments
assert (a1.consonants == ['m','r','c','l','s','l']) # consonants are in the original order
assert (a1.vowels == ['i','a','u','o','u','y']) # but vowels are in the original order
assert (str(First('miraculous')) == "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=['i', 'a', 'u', 'o', 'u'])")
# Two First's are equal if their consonants are equal.
assert (First('myricyl') == First('miracle'))
assert (First('miraculously') != First('miraculous'))
assert (First('miraculously') != "don't crash here!")
# clear_vowels and cleared_vowels are different methods (one is destructive)
a2 = First('miraculous')
a2.clear_vowels()
assert (str(a2) == "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=[])")
a3 = First('miraculous')
a4 = a3.cleared_vowels()
assert (isinstance(a4, First))
assert (str(a3) == "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=['i', 'a', 'u', 'o', 'u'])")
assert (str(a4) == "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=[])")
s = []
assert (First('myricyl') not in s)
s.append(First('myricyl'))
assert (First('myricyl') in s)
assert (First('miracle') in s)
b1 = Second('miracle',5) # creates an First with 5 as shift
assert (isinstance(b1, First))
assert (str(b1) == "First(consonants=['m', 'r', 'c', 'l'], vowels=['i', 'a', 'e'])") # use __class__, __bases__, __name__ attribute
# only Second's object can call encoder:
b2 = b1.encoder() # so instead of 'miracle' it's now "rnwfhqj'
print(str(b2))
assert (str(b2) == "First(consonants=['r', 'w', 'h', 'q', 'n', 'f', 'j'], vowels=[])") # encoding consonants then vowels
assert (type(b2) == Second)
crashed = False
try:
    a = First('abc').encoder()
except:
    crashed = True
    assert (crashed == True)
print("Passed!")