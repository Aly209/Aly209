# -------------------------------------------------------------------
# Learn Python in Arabic #011 - Strings
# Strigns
# -------------------------------------------------------------------

MyString_1 = 'This is a single quote'
MyString_2 = "This is a double quote"

print (MyString_1) ; print (MyString_2)

print ('This is a signle quote \'Test\'') # This is to print the quote using backslash 
print ('This is a single quote "Test"') # you can also simply use a different type of quotation and it works

print ("First\nSecond\nThird") # This is to print each-in-line word using \n 
print ("""First
Second
Third""") # This is another way to do so by using triple quotation
print ("""First Second Third""") # Writing them in the same line doesn't print each in a line

# Using triple quotation we can also easily print quotation from both types inside the sentence

print ("""First 'Test' 'Test'
Second
Third """) 

print ("""First "Test" "Test"
Second
Third """) 

# using backslash in the middle between qutoation will print it, while at the end of the line will ignore the new line ( notice that nothing happens at first line)
print ("""First 'Test' \ "Test" \ 
Second 'Test' \ "Test" \
Third""")

print ("""First 
Second 'Test' \\\ "Test" \
Third""") # 2 get 1 ---- 4 get 2 ---- 6 get 3 ---- 8 get 4 --- each \ escape one








