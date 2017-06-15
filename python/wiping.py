#! /usr/bin/python3

import sys #import argv and exit()

filename = raw_input("Podaj plik html\n") #get file name of html from user

looking=[] # iniciation of looking list (print only user from this list)
for arg in sys.argv[1:]: # for all input files
	try:
		f = open(arg, 'r') # open file
		for line in f:
			looking.append(line.rstrip()) #add to list 
	except IOError:
		print "Nie wlasciwy plik z osobami"
		sys.exit()

try:
	f = open(filename, 'r') # open html file
except IOError:
	print "Nie wlasciwy plik .html"
	sys.exit()
	
fileContent="" # all lines from file
for line in f:
	fileContent+=line;# get all lines from file
	
startF=fileContent.find("<table width=\"100%\" class=\"problems\">") #get start of table
endF= fileContent.find("</tbody></table>",startF) # get end of table

if startF==-1 or endF==-1: # if hasn't got
	print "Nie wlasciwy plik .html"
	sys.exit()

try: # just in case
	fileContent=fileContent[startF:endF] #cut file lines to table

	while endF>0: # until end of tab
		startF=fileContent.find("<tr class=\"problemrow\">") # get start of table row
		endF= fileContent.find("</tr>",startF) # get end of  table row
		if endF<0: #check after update of end if table reach end
			continue;
		row = fileContent[startF:endF] # set row from start to end
		fileContent=fileContent[endF:] # cut row from whole file
		start= row.find("/users/")+7 # get start for nick
		end= row.find("\">",start) # get end for nick
		nick= row[start:end] # set nick from start to end
		if (len(looking)>1 and nick not in looking): # skip if looking list is declared and nick isn't on it 
			continue
		start=row.find(">",end)+1 # get start for name
		end=row.find("<",start) # get start for name
		name= row[start:end] # set name from start to end
		
		points=[]#declarate list of points
		tempStart=0 # fake declaration
		while tempStart<start: # until reach end of or behind end
			tempStart=start
			start=row.find(">",end)+1 #get start for score
			end=row.find("<",start)   #get start for score
			word=row[start:end] # set start and end of score
			try:
				int(word[0:1]) # try if its really digit
				points.append(word)
			except ValueError:
				if word=="-": # maybe at least "no point" char
					points.append("0.0")
		sum=points[-1] #get sum of points
		del points[-1] # remove sum of points
		del points[-1] # remove sql point (?)
		points=','.join(points) # make one string of points
		#print "\""+name + "\",\"" + nick + "\","+points+","+sum+";" #print with sum
		print "\""+name + "\",\"" + nick + "\","+points+";" #print without sum
except:
    print "Nie wlasciwy plik .html" # just in case