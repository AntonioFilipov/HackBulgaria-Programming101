import sys 

def concat_files(files):
    for file_item in files:
        my_file = open(file_item, "r")
        MEGATRON += my_file.read() + "\n"
        my_file.close()
    return MEGATRON

def main():
    