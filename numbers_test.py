from numbers import First, Second
a1 = First(1, 5, 3, 4, 2, 3) # First's constructor takes variable of arguments
assert (a1.evens == [2, 4]) # evens are in sorted order
assert (a1.odds == [1, 5, 3, 3]) # odds are in the original order
assert str(First(4, 3, 2, 5)) == 'First(evens=[2, 4], odds=[3, 5])' # use __class__ and __name__ attribute
# Two First's object are equal if their evens are equal.
assert (First(4, 3, 2, 5) == First(2, 3, 4))
assert (First(4, 3, 2, 5) != First(3, 4, 5))
assert (First(4, 3, 2, 5) != "Correct handling this situation!")
# del_odds and deleted_odds are different methods (one is destructive)
a2 = First(4, 3, 2, 5)
a2.del_odds()
assert (str(a2) == 'First(evens=[2, 4], odds=[])')
a3 = First(4, 3, 2, 5)
a4 = a3.deleted_odds() # use __class__ attribute
assert (isinstance(a4, First))
assert (str(a3) == 'First(evens=[2, 4], odds=[3, 5])')
assert (str(a4) == 'First(evens=[2, 4], odds=[])')
s = []
assert (First(1, 2) not in s)
s.append(First(1, 2))
assert (First(1, 2) in s)
assert (First(1, 2, 3) in s)
b1 = Second(3, 7) # creates an First with values [3,4,5,6,7]
assert (isinstance(b1, First))
assert (str(b1) == 'First(evens=[4, 6], odds=[3, 5, 7])') # use __class__, __bases__, __name__ attribute
# only Second's object can call transform:
b2 = b1.transform(2) # so instead of (3,7) it's now (3+2,7+2)
print(str(b2))
assert (str(b2) == 'First(evens=[6, 8], odds=[5, 7, 9])')
assert (type(b2) == Second)
crashed = False
try:
    a = First(1, 2).transform()
except:
    crashed = True
assert (crashed == True)
print("Passed!")
