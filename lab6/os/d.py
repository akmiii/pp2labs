#count the number of lines in a text file

file = open("example.txt","r")
cnt = 0

text = file.read()
List = text.split("\n")
  
for i in List:
    if i:
        cnt += 1
          
print("Number of lines:", cnt)