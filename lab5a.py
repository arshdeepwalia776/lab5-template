#!/usr/bin/env python3
# Author ID: aswalia6

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: could not read file"
    except Exception as e:
        return f"Error: {str(e)}"

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return "Error: could not read file"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

