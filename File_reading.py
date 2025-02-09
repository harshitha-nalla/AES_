
file_name = "file.txt"
with open(file_name, "r") as file:
    file_content = file.read()

print("File content:")
print(file_content)
print()

words = file_content.split()
char_count=0
word_count=0
for i in range (0,len(words)):
    print()
    print(words[i])
    word_count+=1
    print("The number of characters in the word are: "+str(len(words[i])))
    char_count+=len(words[i])
    for j in range (0,len(words[i])):
        print(f"The ascii value of the character {words[i][j]} in word are: "+ str(ord(words[i][j])))
print()
print()
print("The total word count is : "+str(word_count))
print("The total characters are: "+str(char_count))



