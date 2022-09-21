def readg():
    f = open ( 'graph.txt' , 'r')
    l = [[int(num) for num in line.split(',')] for line in f ]
    return l 
def lengthg():
    return sum(1 for line in open('graph.txt'))
