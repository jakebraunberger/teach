import os
import subprocess

class_list = ['Caitlynn', 'Chailynn', 'Aspen',
'Kevin', 'Hennessie', 'Tavion', 'Hannah',
'Keziah', 'Avery', 'Madalynn', 'Elijah',
'Teegan', 'Christian', 'Natasha', 'Evyn']

fi = open('hw1.tex', 'r')


lines = fi.readlines()

line_copy = lines
for student in class_list:
	latex_file = 'hw1out' + student + '.tex'
	fo = open(latex_file, 'w')
	lines = line_copy
	str_out = ''
	for line in lines:
		if (line.find('xxx', 0) != -1):
			pos = line.find('xxx', 0)
			line = line[0:pos] + student + line[pos+3:]
		str_out += line
	fo.write(str_out)
	fo.close()
	subprocess.check_call(["pdflatex", latex_file])
	subprocess.check_call(["sage", latex_file[0:-3]+"sage"])
	subprocess.check_call(["pdflatex", latex_file])
