# ------------------------------------------------------------------------------
# Learn Python in Arabic #008 - Variables Part Two
# Definition for Source Code, Translation, Compilation, Runtime, Interprerted
# ------------------------------------------------------------------------------

# Reserved Words
help("keywords")
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not

# we can not use the above keywords as our variables
FALSE = "Flase" # FALSE here is a variable because it's different from the keyword "False"

# False = "False" # We can't use "False" as our variable because it's one of the keywods.
# print (False) 

# if we uncomment the above, we would have a SyntaxError: cannot assign to False

a, b, c = 1, 2, 3 #assigning variables is so easy
print (a)
print (b)
print (c)

