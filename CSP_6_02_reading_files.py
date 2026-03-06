#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    #Given a file return the longest line from within that file
    f = open(fileName)
    max = ""
    for line in f:
        if len(line) > len(max):
            max = line
    return max


def toBinary(fileName):
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    with open(fileName, 'r') as f:
        data = f.read().replace('\n', '').replace(' ', '')  # read as single string, strip whitespace

    # Split into chunks of 8 (last chunk may be smaller)
    return [data[i:i + 8] for i in range(0, len(data), 8)]


