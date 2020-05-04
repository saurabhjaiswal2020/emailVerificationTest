import requests

def create_file(file_name,emails):
    f = open(file_name, "a")
    f.write(str(emails + '\n'))
    f.close()