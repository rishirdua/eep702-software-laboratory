from __future__ import division

#import libraries
import re;
import dateutil.parser as dparser;
import os, time, math, tempfile
import numpy

try:
    import Gnuplot, Gnuplot.PlotItems, Gnuplot.funcutils
except ImportError:
    # kludge in case Gnuplot hasn't been installed as a module yet:
    import __init__
    Gnuplot = __init__
    import PlotItems
    Gnuplot.PlotItems = PlotItems
    import funcutils
    Gnuplot.funcutils = funcutils

_digits = re.compile('\d')

def contains_digits(d):
    return bool(_digits.search(d))

#Let user press enter so that all the graphs do not pop open at once
def wait(str=None, prompt='Press return to continue...\n'):
    if str is not None:
        print str
    raw_input(prompt)


#load dictionary
with open('positive_list.txt') as f:
    poslist = f.readlines()
f.close()
poslist = map(lambda s: s.strip(), poslist)
with open('negative_list.txt') as f:
    neglist = f.readlines()
f.close()
neglist = map(lambda s: s.strip(), neglist)

#declate variables
posscore = []; negscore = []; neutscore = []; normscore = [];

#initialize variables
for i in range(0,24):
	posscore.insert(i,0);
	negscore.insert(i,0);
	neutscore.insert(i,0);
	normscore.insert(i,0);
post = 0;
posflag=0;
negflag=0;

#calculate scores
with open('data.txt') as f:
    for line in f:
	if contains_digits(line):		
		d = dparser.parse(line, fuzzy=True)
		#print "d.hour is " + str(d.hour)
		if (posflag==1):
			posscore[d.hour]=posscore[d.hour]+1;
		if (negflag==1):
			negscore[d.hour]=negscore[d.hour]+1;
		if (posflag==0 and negflag==0):
			neutscore[d.hour]=neutscore[d.hour]+1;
		posflag=0;
		negflag=0;
	else:
		for posword in poslist:
			if posword in line:
				posflag=1;
		for negword in neglist:
			if negword in line:
				negflag=1;
f.close()

#display to user
print "Interval\t:)\t:(\t;)\tComment\n________\t_____\t_____\t_____\t_______\n"
for i in range(0,24):
	print str(i) +":00-" + str(i+1) + ":00\t" + str(posscore[i]) + "\t" + str(negscore[i])+ "\t" + str(neutscore[i])+"\t",
	if (posscore[i]==0 and negscore[i]==0):
		print "NONE!"
	elif (posscore[i]>negscore[i]):
		print "HAPPY!"
	else:
		print "SAD!"
print "________\t_____\t_____\t_____\t_______\n"


#normalize the scores
f = open('graph.dat', 'w')
for i in range(0,24):
	if (posscore[i]+negscore[i]+neutscore[i] == 0):
		normscore[i]=0;
	else:
		normscore[i] = (posscore[i] - negscore[i])/(posscore[i]+negscore[i]+neutscore[i]);
	f.write(str(i) + "\t" + str(normscore[i]) + "\n");
f.close();

#plot using gnuplot
g = Gnuplot.Gnuplot(debug=1)
g.clear()
g.title('normalized counted data')
g.xlabel('time')
g.ylabel('score')
g.plot(Gnuplot.File('graph.dat', with_='lines'))
g.replot()
wait();



#partb
maxposval = 0;
maxnegval = 0;
maxneutval = 0;
maxposind = 0;
maxnegind = 0;
maxneutind = 0;
print "Interval\t:)\t:(\t;)\tComment\n________\t_____\t_____\t_____\t_______\n"
for i in range(0,24):
	if (posscore[i]>maxposval):
		maxposval = posscore[i];
		maxposind = i
	if (negscore[i]>maxnegval):
		maxnegval = negscore[i];
		maxnegind = i
	if (neutscore[i]>maxneutval):
		maxneutval = neutscore[i];
		maxneutind = i
print "Results of max posts of a particular sentiment"
print "Positive\t" + str(maxposind) +":00-" + str(maxposind+1) + "\t" + str(maxposval)
print "Negative\t" +  str(maxnegind) +":00-" + str(maxnegind+1) + "\t" + str(maxnegval)
print "Neutral\t" +  str(maxneutind) +":00-" + str(maxneutind+1) + "\t" + str(maxneutval)
print "________\t_____\t_____\t_____\t_______\n"


#partc

location1 = raw_input('Enter place 1 (eg: LosAngeles): ')
location2 = raw_input('Enter place 2 (eg: Iraq): ')

print "LOCATION 1:\t" + location1 + "\n"
#reset variables
for i in range(0,24):
	posscore.insert(i,0);
	negscore.insert(i,0);
	neutscore.insert(i,0);
	normscore.insert(i,0);
post = 0;
posflag=0;
negflag=0;


with open('data.txt') as f:
    for line in f:
	if contains_digits(line):		
		d = dparser.parse(line, fuzzy=True)
		#print "d.hour is " + str(d.hour)
		if (posflag==1) and (location1 in line):
			posscore[d.hour]=posscore[d.hour]+1;
		if (negflag==1) and (location1 in line):
			negscore[d.hour]=negscore[d.hour]+1;
		if (posflag==0 and negflag==0) and (location1 in line):
			neutscore[d.hour]=neutscore[d.hour]+1;
		posflag=0;
		negflag=0;
	else:
		for posword in poslist:
			if (posword in line):
				posflag=1;
		for negword in neglist:
			if (negword in line):
				negflag=1;
f.close()

#display
print "Interval\t:)\t:(\t;)\tComment\n"
for i in range(0,24):
	print str(i) +":00-" + str(i+1) + ":00\t" + str(posscore[i]) + "\t" + str(negscore[i])+ "\t" + str(neutscore[i])+"\t",
	if (posscore[i]==0 and negscore[i]==0):
		print "NONE!"
	elif (posscore[i]>negscore[i]):
		print "HAPPY!"
	else:
		print "SAD!"


print "LOCATION 2:\t" + location2 + "\n"
#reset variables
for i in range(0,24):
	posscore.insert(i,0);
	negscore.insert(i,0);
	neutscore.insert(i,0);
	normscore.insert(i,0);
post = 0;
posflag=0;
negflag=0;


with open('data.txt') as f:
    for line in f:
	if contains_digits(line):		
		d = dparser.parse(line, fuzzy=True)
		#print "d.hour is " + str(d.hour)
		if (posflag==1) and (location2 in line):
			posscore[d.hour]=posscore[d.hour]+1;
		if (negflag==1) and (location2 in line):
			negscore[d.hour]=negscore[d.hour]+1;
		if (posflag==0 and negflag==0) and (location2 in line):
			neutscore[d.hour]=neutscore[d.hour]+1;
		posflag=0;
		negflag=0;
	else:
		for posword in poslist:
			if (posword in line):
				posflag=1;
		for negword in neglist:
			if (negword in line):
				negflag=1;
f.close()

#display
print "Interval\t:)\t:(\t;)\tComment\n________\t_____\t_____\t_____\t_______\n"
for i in range(0,24):
	print str(i) +":00-" + str(i+1) + ":00\t" + str(posscore[i]) + "\t" + str(negscore[i])+ "\t" + str(neutscore[i])+"\t",
	if (posscore[i]==0 and negscore[i]==0):
		print "NONE!"
	elif (posscore[i]>negscore[i]):
		print "HAPPY!"
	else:
		print "SAD!"
		
print "________\t_____\t_____\t_____\t_______\n"


#problem 4
locations = "london, LosAngeles, Iraq, Delhi, Washington"

#calculate for full
#initialize variables
for i in range(0,5):
	posscore.insert(i,0);
	negscore.insert(i,0);
	neutscore.insert(i,0);
	normscore.insert(i,0);
post = 0;
posflag=0;
negflag=0;


#calculate scores
print "Recalculating overall scores for normalization";
with open('data.txt') as f:
    for line in f:
	if contains_digits(line):		
		if "London" in line:
			loc = 0;
		elif "LosAngeles" in line:
			loc = 1;
		elif "Iraq" in line:
			loc = 2;
		elif "Delhi" in line:
			loc = 3;
		elif "Washington" in line:
			loc = 4;

		#print "d.hour is " + str(d.hour)
		if (posflag==1):
			posscore[loc]=posscore[loc]+1;
		if (negflag==1):
			negscore[loc]=negscore[loc]+1;
		if (posflag==0 and negflag==0):
			neutscore[loc]=neutscore[loc]+1;
		posflag=0;
		negflag=0;
	else:
		for posword in poslist:
			if posword in line:
				posflag=1;
		for negword in neglist:
			if negword in line:
				negflag=1;
f.close()


#calculate for required portion
print "Calculating scores for all locations";
rposscore = []; rnegscore = []; rneutscore = [];
#reset variables
for i in range(0,5):
	rposscore.insert(i,0);
	rnegscore.insert(i,0);
	rneutscore.insert(i,0);
	normscore.insert(i,0);
post = 0;
posflag=0;
negflag=0;


with open('data.txt') as f:
    for line in f:
	if contains_digits(line):		
		if "London" in line:
			loc = 0;
		elif "LosAngeles" in line:
			loc = 1;
		elif "Iraq" in line:
			loc = 2;
		elif "Delhi" in line:
			loc = 3;
		elif "Washington" in line:
			loc = 4;
		#print "d.hour is " + str(d.hour)
		#print loc;
		if (posflag==1): #and (location1 in line):
			rposscore[loc]=rposscore[loc]+1;
		if (negflag==1): #and (location1 in line):
			rnegscore[loc]=rnegscore[loc]+1;
		if (posflag==0 and negflag==0): #and (location1 in line):
			rneutscore[loc]=rneutscore[loc]+1;
		posflag=0;
		negflag=0;
	else:
		for posword in poslist:
			if (posword in line):
				posflag=1;
		for negword in neglist:
			if (negword in line):
				negflag=1;
f.close()

#normalize
f = open('graph_loc.dat', 'w')
for i in range(0,5):
	if (posscore[i]+negscore[i]+neutscore[i] == 0):
		normscore[i]=0;
	else:
		normscore[i] = (rposscore[i] - rnegscore[i])/(posscore[i]+negscore[i]+neutscore[i]);
	#f.write(str(i) + "\t" + str(normscore[i]) + "\n");
	if i==0:
		city = "London"
	if i==1:
		city = "LosAngeles"
	if i==2:
		city = "Iraq"
	if i==3:
		city = "Delhi"
	if i==4:
		city = "Washington"

	f.write(str(i) + "\t" + str(normscore[i]) + "\n");
f.close();

#plot
g = Gnuplot.Gnuplot(debug=1)
g.clear()
g.title('Location normalized against all')
g.xlabel('0 : London, 1: LosAngeles, 2: Iraq, 3: Delhi, 4: Washington')
g.ylabel('y')
g.plot(Gnuplot.File('graph_loc.dat', with_='lines'))
g.replot()
wait();



#problem 5
print "Extra question"
#This was not in the EEP702 course and has been added by me for practice
location = raw_input('Enter a location: ');

#calculate for full
#initialize variables
for i in range(0,24):
	posscore.insert(i,0);
	negscore.insert(i,0);
	neutscore.insert(i,0);
	normscore.insert(i,0);
post = 0;
posflag=0;
negflag=0;

#calculate scores
print "Recalculating overall scores for normalization";
with open('data.txt') as f:
    for line in f:
	if contains_digits(line):		
		d = dparser.parse(line, fuzzy=True)
		#print "d.hour is " + str(d.hour)
		if (posflag==1):
			posscore[d.hour]=posscore[d.hour]+1;
		if (negflag==1):
			negscore[d.hour]=negscore[d.hour]+1;
		if (posflag==0 and negflag==0):
			neutscore[d.hour]=neutscore[d.hour]+1;
		posflag=0;
		negflag=0;
	else:
		for posword in poslist:
			if posword in line:
				posflag=1;
		for negword in neglist:
			if negword in line:
				negflag=1;
f.close()


#calculate for required portion
print "Calculating scores for " + location;
rposscore = []; rnegscore = []; rneutscore = [];
#reset variables
for i in range(0,24):
	rposscore.insert(i,0);
	rnegscore.insert(i,0);
	rneutscore.insert(i,0);
	normscore.insert(i,0);
post = 0;
posflag=0;
negflag=0;


with open('data.txt') as f:
    for line in f:
	if contains_digits(line):		
		d = dparser.parse(line, fuzzy=True)
		#print "d.hour is " + str(d.hour)
		if (posflag==1) and (location1 in line):
			rposscore[d.hour]=rposscore[d.hour]+1;
		if (negflag==1) and (location1 in line):
			rnegscore[d.hour]=rnegscore[d.hour]+1;
		if (posflag==0 and negflag==0) and (location1 in line):
			rneutscore[d.hour]=rneutscore[d.hour]+1;
		posflag=0;
		negflag=0;
	else:
		for posword in poslist:
			if (posword in line):
				posflag=1;
		for negword in neglist:
			if (negword in line):
				negflag=1;
f.close()
#normalize
f = open('graph_extra.dat', 'w')
for i in range(0,24):
	if (posscore[i]+negscore[i]+neutscore[i] == 0):
		normscore[i]=0;
	else:
		normscore[i] = (rposscore[i] - rnegscore[i])/(posscore[i]+negscore[i]+neutscore[i]);
	f.write(str(i) + "\t" + str(normscore[i]) + "\n");
f.close();

#plot
g = Gnuplot.Gnuplot(debug=1)
g.clear()
g.title('Location normalized against all')
g.xlabel('x')
g.ylabel('y')
g.plot(Gnuplot.File('graph_extra.dat', with_='lines'))
g.replot()
wait();
