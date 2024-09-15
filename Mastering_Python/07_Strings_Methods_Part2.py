# -------------------------------------------------------------------
# Learn Python in Arabic #013 - Strings Methods Part 1
# Strings Methods
# len () => returns the number of items in a container
# strip() => removes right and left spaces or characters ---- rstrip() removes right spaces only --- lstrup() removes left spaces only 
# -------------------------------------------------------------------

a = "I love you"

len (a) # => returns the number of items in a container
print (len(a)) #number of specaes in the obj or container: 10 (letters and spaces) # This has nothing to do with Index or Slicing bcz both starts from 0

# to use strip(), write the name of the variable and then dot (.)
b = "       I love you         "
print (b.strip())  #strip() => removes right and left spaces 
print (b.rstrip()) #rstrip() removes right spaces only
print (b.lstrip()) #lstrup() removes left spaces only

c = "*****I love you*****"
print (c.strip("*"))  # strip() => removes right and left # characters # don't forget the ""
print (c.rstrip("*")) # rstrip() removes right * characters only
print (c.lstrip("*")) # lstrup() removes left  * characters only 


















