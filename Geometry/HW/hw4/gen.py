import os
import subprocess
import Problem
import Header
import random

class_list = ['Chantel', 'Angel', 'Jaxon', 'Waylon', 'Lindsay',
				'Elli', 'Christian', 'Madison', 'Jake', 'Cooper']
class_list = ['test']
fi = open('hw4.tex', 'r')


lines = fi.readlines()


line_copy = lines
for student in class_list:
	problem_being_read_in = False
	header_being_read_in = True
	str_problem = ""
	str_header = ""
	problem_list = []
	

	latex_file = 'hw4out' + student + '.tex'
	fo = open(latex_file, 'w')
	lines = line_copy
	str_out = ''
	for line in lines:
		if (line.find('%hhhs',0) != -1):
			problem_being_read_in = False
			header_being_read_in = True
		# build the individual file
		if (line.find('xxx', 0) != -1):
			pos = line.find('xxx', 0)
			line = line[0:pos] + student + line[pos+3:]
		
		if (line.find('%hhhe',0) != -1):
			header_being_read_in = False
			header = Header.Header(str_header)

		if (header_being_read_in):
			str_header += line

		# total hack work around.... todo: change sometime
		if (line.find('\\end{document}',0) == -1):
			# just don't write it to the string that we write to the file
			problem_being_read_in = True

		# find problem start %ppps
		problem_start_head = line.find('%ppps', 0)
		problem_end_head = line.find('%pppe', 0)
		if (problem_start_head != -1):
			# need to read lines until the end is encountered
			print line
			problem_being_read_in = True
			number_of_problems_like_this = int(line[problem_start_head+5:])
		if (problem_being_read_in):
			str_problem += line

		if (problem_end_head != -1):
			problem_being_read_in = False
			for i in range(number_of_problems_like_this):
				problem_list.append(Problem.Problem(str_problem))
			str_problem = ""

	# write the header
	fo.write(str(header))
	random.shuffle(problem_list)
	
	for problem in problem_list:
		print str(problem)
		fo.write(str(problem))
		

	# write the end
	fo.write("\\end{document}")
	
	fo.close()
	subprocess.check_call(["pdflatex", latex_file])
	subprocess.check_call(["sage", latex_file[0:-3]+"sage"])
	subprocess.check_call(["pdflatex", latex_file])
