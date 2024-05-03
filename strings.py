# # strings = "This is Python"
# # char = "C"
# # multiline_str = """This is a multiline string with more than one line code."""
# # unicode = u"\u00dcnic\u00f6de"
# # raw_str = r"raw \n string"

# # print(strings)
# # print(char)
# # print(multiline_str)
# # print(unicode)
# # print(raw_str)

str = 'Python Programming'
# # print('str = ', str)
# # #first character
# # print('str[0] = ', str[0])

# # #last character
# # print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

# # #slicing 6th to 2nd last character
# # print('str[5:-2] = ', str[5:-2])

# # Python String Operations
# str1 = 'Hello'
# str2 ='World!'

# # using +
# print('str1 + str2 = ', str1 + str2)

# # using *
# print('str1 * 3 =', str1 * 3)
 
# # Iterating through a string
# count = 0
# for x in 'Hello World':
#     if(x == 'l'):
#         count = count +1
# print(count,'letters found')

# str = 'MITWPU'
# # enumerate()
# xx = list(enumerate(str))
# print('list(enumerate(str) = ',xx)
# print('len(str) = ', len(str))


"MITwpu".upper()
"MITwpu".lower()
"This will split all words into a list".split()
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'Welcome to MITWPU Pune'.find('co')
'Happy New Year'.replace('Happy','Brilliant')

print("MITwpu".upper())
print("MITwpu".lower())
print(''.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))

print('Welcome to MITWPU Pune'.find('co'))
print('Happy New Year'.replace('Happy','Brilliant'))
print("This will split all words into a list".split())

print("Hello", "World","Rishi", sep=', ', end='!\n',flush=True)
# Output: Hello, World!
