# -------------------------------------------------------------------
# Learn Python in Arabic #014 - Strings Methods Part Two
# Strings Methods
# split() --> gives a list of splitted or separated words of a variable 
# -------------------------------------------------------------------

a = "I love Alahly the African Club of Century"
print (a.split()) # ['I', 'love', 'Alahly;', 'the', 'African', 'Club', 'of', 'Century']
# in this case, the default for the separation is the space, but if we want to change this, we simply put it between the brackets

b = "Alahly-Fans-are-the-best"
print (b.split("-")) # do not forget the ""

# when pointing the arrow on split you would find
'''sep
    The separator used to split the string.

    When set to None (the default value), will split on any whitespace
    character (including \n \r \t \f and spaces) and will discard
    empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.'''

# sep is the delimiter string 
# maxsplit --> split only the first (x) words or cases and then leave the remaining as a one word

c = "Islam-is-True-Religion"
print (c.split("-",2)) # ['Islam', 'is', 'True-Religion']

# using rsplit would do the same but from right, so
d = "Islam-is-True-Religion"
print (d.rsplit("-",2)) # ['Islam-is', 'True', 'Religion']

# To know the type ---> use type
print (type(a.split())) # list class

# center() --> center-align a string, padding it with a specified character (default is a space) to achieve a specified total length. 
e = "Hana"
print (e.center(8)) # the number or length parameter has to be put
# the result is "  Hana  ", as there are two spaces which added before and after the variable.

f = "Hana"
print (f.center(8,"=")) # not instead of using default spaces, we used =
# the result is "==Hana=="
# if we used odd number, the bigger number would be with the left not the right. 
# so if it print (f.center(9,"=")), output would be ===Hana==

# count --> used to count how many times a word has been repeated
g = "Hana has to be happy because happy wife means happy life"
print (g.count("happy")) # count() takes at least 1 argument and it must be str, not int. # the output will be 3
print (g.count("happy",0,20)) # count() takes at most 3 argument. First one is the word, second is the first index, third is the last index # the output will be 1 as it only includes "Hana has to be happy"

# swapcase() --> simply swap the case of the letters
h = "yOU cAN'T sEE mE"
print (h.swapcase()) # Output is "You Can't See Me"

# startswith() ---> simply if it starts with the written str, we get True. If not, we get False.  
# # takes at least 1 argument and it must be str

i = "I love Allah"
print (i.startswith("I") ) # Since the statement does start with I, we got True.
j = "Allah Loves me" 
print (j.startswith("A") ) # Since the statement does start with A, we got True.
h = "Allah Loves me" 
print (h.startswith("allah") ) # Since the statement does not start with allah but Allah, we got False.
print (h.startswith("m",12,13) ) # Since the defined index does start with m, we got True.

# same role with endswith()
print (i.endswith("h") ) # Since the statement does end with h, we got True.
print (i.endswith("e",0,6) ) # Since the defined index does end with e, we got True.



















