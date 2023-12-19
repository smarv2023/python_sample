names = ['Marvin', 'Luffy', 'Angel', 'Cloud', 'Tifa',
         'Barret', 'Goku', 'Vegeta', 'Saitama', 'Genos']
revlist = []


# Function to reverse the order of the name and create a file
def reverseNamesAndWriteToFile(names):
    for i in reversed(range(len(names))):
        revlist.append(names[i])
    result = open("resultsFile.txt", 'w')
    for file in revlist:
        # I just add comma in the file so that it will be easy to distinguish
        result.write(file + ", ")
    result.close()
    print("Original", names, "\nReversed", revlist, "\nFile created!!!")


# To call the function
reverseNamesAndWriteToFile(names)
