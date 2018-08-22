from random import randint

class Problem:
	def __init__(self, number, string, l):
		self.number = number
		self.string = string
		self.list = l
		print string

	def __str__(self):
		out = "\\begin{problem}{"+str(self.number)+"} \n"
		for line in self.string:
			i = 0
			prev_pos = 0
			pos = line.find("xxx")
			if (pos == -1):
				out += line
			while (pos != -1):
				out += line[prev_pos:pos]
				prev_pos = pos + 3
				out += str(randint(-10,10))
				i = i + 1
				pos = line.find("xxx", prev_pos)
			if (prev_pos != 0):
				out += line[prev_pos:]
			out += "\n \\end{problem}"
		return out
