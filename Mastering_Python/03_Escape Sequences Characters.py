# -------------------------------------------------------------------
# Learn Python in Arabic #009 - Escape Sequences Characters
# \ =>  Back Slash
# \b => back space => removes the prev space
# \ =>  escape the NEXT line
# \\ => escape back slash
# \' => escape sigle quote
# \" => escape double quote
# \r => Carriage Return => run to know
# \t => Horizontal Tab 

# -------------------------------------------------------------------

# Back Slash b
print ("Hello\b world") # will remove the o

# \ => escape the NEXT line
print ("Hello \
I \
Love Python")

# to print the back slash itself, add one more back slash
print ("Hello I love you too \\")
# to print the signle/double quote, use back slash before and after
print ('I love Signle Quote \'Test\'')

#Line Feed => creating a second line
print ("Hello World\nSecond Line")

# Carriage Return => run to know \r
print ("123456\rHana")

# Horizontal Tab \t
print ("Hna\tHesham")

# Charactrer Hex Value
print ("\x41\x4c\x49") #printing ALI using HEX Characters # 41 is A, ...
print ("\x48\x41\x4e\x41") #printing HANA using HEX Characters. 4e is N,...