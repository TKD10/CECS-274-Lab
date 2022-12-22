import numpy as np

def get_information(path):
    with open(path) as file:    #used to extract files from the path
        data = np.zeros(5)      #in java, int characters[5]
        i = 0
        for line in file:   #creates for loop for all lines in file numbers.txt and go one by one
            data[i] = int(line)     #iterates i in the data set
            i += 1            #increments i
        return data

def put_information(data):
    with open("output.txt", "w") as file:       #uses file descriptors to ask permission to write to a file
        i = 4       #iteration
        while i > -1:       #has to go past 0
            file.write(str(int(data[i])) + "\n")   #data i stores a float and string
            i -= 1      #decrements as an iterator
        return



def main():
    file_path = input()
    read_data = get_information(file_path)
    put_information(read_data)

if __name__ == "__main__":
    main()
