import Problem
import Header
import Footer
import os
from random import shuffle

f = open('out.tex', 'w')

head = Header.Header()
foot = Footer.Footer()

files = os.listdir("p")
shuffle(files)

f.write(str(head))
i = 0
for file in files:
	l = []
	fi = open("p/" + file, 'r')
	# read in the random variables and create them

	# then read in the string and create it
	prob = Problem.Problem(i, fi.readlines(), [])
	# then create a problem object and print/write it
	f.write(str(prob))
	fi.close()
	i = i + 1

string = """
Recall that a \\textit{postulate} is a statement that we \\textit{define} as being true. It cannot
be logically deduced from other postulates like a \\textit{theorem} can.
The Segment Addition Postulate and Ruler Postulate seem redundant. Are they redundant? Why or why not?
"""
challenge = Problem.Problem('Challenge', [string], [])

f.write(str(challenge))
f.write(str(foot))
f.close()



