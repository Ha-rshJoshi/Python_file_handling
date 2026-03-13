def countline(name):
    count = 0
    with open(name,'r') as f:
        for line in f:
            count += 1
    print("total number of lines present: ",count)
def countchar(name):
    count = 0
    with open(name,'r') as f:
        for line in f:
            count+=len(line)
    print("total number of characters present: ",count)
def test(name):
    countline(name)
    countchar(name)