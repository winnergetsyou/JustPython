#!/usr/bin/python3

# This program "main_function" will sort all the lines of the text file into alphabetical order

def main_function():
    """
    USE YOUR file LOCATION x=open("C:/Users/ajith/Downloads/ShortStory.txt", "r+")
    """
    x=open("C:/Users/ajith/Downloads/ShortStory.txt", "r+")
    # USE YOUR LOCATION x=open("C:/Users/ajith/Downloads/ShortStory.txt", "r+")
    # this above command opens the file and we can use read & write function
    
    y= x.read()
    #Stores the text file in the variable of string type
    #print(y) for checking y value
    #print(type(y)) for checking y type
    
    
    y=y.replace('"','')
    #removes all the quotes "" from the text file 
    
    z1=y.splitlines()
    #z1 stores the list of lines. spiltline function seperates the text file and stores each lines into elements of an array
    #print(z1) for checking line splits
    

    z2=sorted(z1)
    # sorts the z2 value into alphabetical order
    # print(z2) will print all z2 in array list matrix

    print(*z2, sep = "\n")
    # prints elements line by line 
    
    x.close()
    #closes the file
    
if __name__ == '__main__':
    main_function()


