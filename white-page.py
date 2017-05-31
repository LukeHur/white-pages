print ("Why did you come here, it was a wrong choice") # Print the message in the first line
print ("\nWelcome to my world") # Print this message in a new line

reflect = raw_input("Press freaking ENTER") # make this variable Enter to get input by a user

if reflect == "": #Set a plan if the user gives no input
    filename = raw_input("Insert the freaking file name you freaking want") # name the file by the name the writer writes

    with open (filename+".txt","w") as f: #Open directly the file the user named (made)
        print ("Freaking write 3 freaking people's informations you want") # print this text

        print ("<First Person>") # print this text
        line1 = raw_input("Name: ") # make a new variable for line1 that the user types
        f.write(line1) # write the name in first line
        f.write("\n") # write the name in new line
        line2 = raw_input("Birthday: ") # make a new variable for line2 that the writer types
        f.write(line2) # write the Birthday in second line
        f.write("\n") # write the Birthday in new line
        line3 = raw_input("Phone Number: ") # make a new variable for line3 what the writer writes
        f.write(line3) # write the Phone Number in third line
        f.write("\n") # write the Phone Number in new line

        print ("<Second Person>") # print this text
        line1 = raw_input("Name: ") # make a new variable for line1 that the user types
        f.write(line1) # write the name in first line
        f.write("\n") # write the name in new line
        line2 = raw_input("Birthday: ") # make a new variable for line2 that the writer types
        f.write(line2) # write the Birthday in second line
        f.write("\n") # write the Birthday in new line
        line3 = raw_input("Phone Number: ") # make a new variable for line3 what the writer writes
        f.write(line3)  # write the Phone Number in third line
        f.write("\n") # write the Phone Number in new line

        print ("<Third Person>") # print this text
        line1 = raw_input("Name: ") # make a new variable for line1 that the user types
        f.write(line1) # write the name in first line
        f.write("\n") # write the name in new line
        line2 = raw_input("Birthday: ") # make a new variable for line2 that the writer types
        f.write(line2) # write the Birthday in second line
        f.write("\n") # write the Birthday in new line
        line3 = raw_input("Phone Number: ") # make a new variable for line3 what the writer writes
        f.write(line3)  # write the Phone Number in third line
        f.write("\n") # write the Phone Number in new line


        print "The file is saved. Bye!" # print what I wrote
        f.close() # close the program, I love David and Mr. Olinda
