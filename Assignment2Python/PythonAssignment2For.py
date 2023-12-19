# Variables
text = str(input("Enter sentence:"))
rev = str("")

# 3 different version of For loop that will reverse the input characters

#count = len(text) - 1
#for x in range(count, -1, -1):
    #rev = rev + text[x] 

count = len(text)
for count in range(0, count, +1):
    rev = text[count] + rev

#for x in text:
    #rev = x + rev

print("\n", text, "\nREVERSED:\n", rev)