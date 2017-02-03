import random
def generate_list():
    
    alist = [x+1 for x in range(random.randint(1,10))]
    assert (alist)
    return alist
    
def printIt():
    print(generate_list())
    
def main():
    printIt()
        
if __name__=='__main__':
    print"Test printIt():"
    main()        