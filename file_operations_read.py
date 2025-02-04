fp = open("text.txt") #this is open for reading
print(fp.read()) #read method gets the entire file content
fp.close() #this is good practice bc then it wont et you open it again

#same thing using a context manager
with open("text.txt", "r") as f:
    print(f.read()) #no need to close

#to read line by line
with open("text.txt", "r") as f:
    for line in f:
        print(line)