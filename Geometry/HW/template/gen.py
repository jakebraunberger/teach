import os
import subprocess
import Problem
import random

class_list = ['Chantel', 'Angel', 'Jaxon', 'Waylon', 'Lindsay',
				'Elli', 'Christian', 'Madison', 'Jake', 'Cooper']

fi = open('hw3.tex', 'r')


lines = fi.readlines()


line_copy = lines
for student in class_list:
	problem_being_read_in = False
	str_problem = ""
	problem_list = []

	latex_file = 'hw3out' + student + '.tex'
	fo = open(latex_file, 'w')
	lines = line_copy
	str_out = ''
	for line in lines:
		# build the individual file
		if (line.find('xxx', 0) != -1):
			pos = line.find('xxx', 0)
			line = line[0:pos] + student + line[pos+3:]
		
		# total hack work around.... todo: change sometime
		if (line.find('\\end{document}',0) == -1)
			# just don't write it to the string that we write to the file
			problem_being_read_in = True

		# find problem start %ppps
		problem_start_head = line.find('\%ppps', 0)
		problem_end_head = line.find('\%pppe', 0)
		if (problem_start_head != -1):
			# need to read lines until the end is encountered
			problem_being_read_in = True
			number_of_problems_like_this = int(line[problem_start_head+5:])
		if (problem_being_read_in):
			str_problem += line

		if (not problem_being_read_in):
			str_out += line

		if (problem_end_head = line.find('\%pppe',0)):
			problem_being_read_in = False
			for i in range(number_of_problems_like_this):
				problem_list.append(Problem.Problem(str_problem))
			str_problem = ""

	# write the header
	fo.write(str_out)
	random.shuffle(problem_list)
	
	for problem in problem_list:
		fo.write(str(problem))
		

	# write the end
	fo.write("\\end{document}")
	
	fo.close()
	subprocess.check_call(["pdflatex", latex_file])
	subprocess.check_call(["sage", latex_file[0:-3]+"sage"])
	subprocess.check_call(["pdflatex", latex_file])
