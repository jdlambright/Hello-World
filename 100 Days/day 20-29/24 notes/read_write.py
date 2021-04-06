#these are notes on how to open write and read files

#the first way. this is less efficient because you have to remember to close it
#open is a built in keyword

# file = open("my_file.txt")
#
# #read method returns contents of file as a string
# #we save it into a variable
# contents = file.read()
#
# print(contents)
#
# #we always need to close the file to not waste computers resources
# file.close()


#________________________Better way_________________
#this is a much more efficient way "file" is a variable
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#writing to a file
#the open method defaults to read only
#mode= "w" puts it in writing mode which replaces all text
#mode= "a" allows you to append to end of file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nnew text")


#you can create a brand new file by putting it in writing mode
#and by giving the file a name  in the string example:

# with open("new_file.txt", mode = "w") as file:
#     file.write("\nNew Text")

#in the snake scoreboard on lines 11-12 we wrote this to retrieve the data
#and set high score as a variable to that data
with open("data.txt") as quote:
    self.high_score = int(quote.read())

#in lines 26-28 we wrote this to erase and rewrite the current data if a new high score was acheived
    new_score = str(self.high_score)
    with open("data.txt", mode="w") as file:
                file.write(new_score)