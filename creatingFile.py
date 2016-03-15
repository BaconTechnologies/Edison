import sys

def write():
    print('Creating new text file') 

    filename = raw_input('Enter name of text file: ')  # Name of text file coerced with +.txt

    print filename + '.txt'

    try:
        file = open('output.txt','a')   # Trying to create a new file or open one
        file.write("Some text")
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

write()