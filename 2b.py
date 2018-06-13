import fileinput
def censor(filename):
    with open(filename,'r+') as f1, open('censor.txt','w+') as f2:
        for line in f1:
	    print "Original Line : ",line,"\nCensored Words : ",
            for word in line.split(' '):
                if len(word)==4:
		    print word,
                    line=line.replace(word,'xxxx')
            f2.write(line)
	    print "\nCensored Line : ",line
file=open('samplefile.txt','w+')
file.write('This file is uncensored.\nEach four letter word must be censored.\nCheck the file with variant size inputs.')
file.close()
censor('samplefile.txt')
