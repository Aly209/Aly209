# -------------------------------------------------------------------
# Learn Python in Arabic #012 - Strings - Indexing And Slicing
# All (Data) in Python is (Object)
# Object contains Element/s
# Each Elements has its own Index --- we use the index to reach the element 
# Python use Zero Based Indexing --- Index starts from Zero 0
# Square Brackets are used to access the Elements
# Indexing and Slicings enable us accessing parts of Strings, Tuples, or Lists 
# -------------------------------------------------------------------

# indexing = used to access a single item
MyString = "I love you"

print (MyString [0]) # index 0 => I 
print (MyString [1]) # index 1 => ( ) => (space) 
print (MyString [2]) # index 2  => l

print (MyString [-1]) # Negative counts from End. so index -1 => u
# so index 5 = index -5
print (MyString [-5]) # index -5  => e
print (MyString [5]) # index 5  => e

 # Slicing = used to access multiple Sequence Items
 # [Start:End:Steps]
 # [Start:End] ---- End is not included

print (MyString [2:6]) # print love
print (MyString [:6]) # if start is not written, system starts from 0















