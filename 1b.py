import fileinput
def stats(filename):
    linec,wordc,charc=0,0,0
    with open(filename,'r+') as file:
        for line in file:
            linec += 1
            for word in line.split():
                wordc += 1
                charc += len(word)
    print "Line Count:",linec ,"\nWord Count:",wordc,"\nCharacter Count:",charc
file=open('samplefile.txt','w+')
file.write('check\nfor\na\nsample\ninput')
file.close()
stats('samplefile.txt')
