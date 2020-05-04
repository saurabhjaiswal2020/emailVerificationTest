import requests

def create_file(file_name,emails):
    f = open(file_name, "a")
    f.write(str(emails + '\n'))
    f.close()



def disposable_check(domain):
    file = open('disposable_domains.txt', "r")

    for x in file:
        if domain in x.strip():
            return False
        else:
            return True

x = disposable_check('gmail.com')
print(x)