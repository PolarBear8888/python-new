if __name__ == '__main__':
    #132319810101****
    nID = ' '
    while 1:
        nID = input("Input your id:")
        if len(nID) != len("132319810101****"):
            print ('wring length of id,input again')
        else:
            break
    print ('your id is %s' % (nID))