# Variables
text = str(input("Enter sentence:"))
rev = str("")

# 2 different version of While loop that will reverse the input characters

#count = len(text) - 1
#while count >= 0:
    #rev = rev + text[count]
    #count = count - 1

x = int(0)
count = len(text)
while x < count:
    rev = text[x] + rev
    x = x + 1
print("\n", text, "\nREVERSED:\n", rev)