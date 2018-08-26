class Header:
	""" Produces header for latex file """
	def __init__(self, author):
		self.author = author
	def __str__(self):
		return """\\documentclass[12pt]{article}

			\\usepackage[margin=1in]{geometry} 
			\\usepackage{amsmath,amsthm,amssymb}
			\\usepackage{float}
			\\usepackage[pdftex]{graphicx}

			 

			\\newcommand{\\N}{\\mathbb{N}}
			\\newcommand{\\Z}{\\mathbb{Z}}

			 

			\\newenvironment{theorem}[2][Theorem]{\\begin{trivlist}
			\\item[\\hskip \\labelsep {\\bfseries #1}\\hskip \\labelsep {\\bfseries #2.}]}{\\end{trivlist}}

			\\newenvironment{lemma}[2][Lemma]{\\begin{trivlist}
			\\item[\\hskip \\labelsep {\\bfseries #1}\\hskip \\labelsep {\\bfseries #2.}]}{\\end{trivlist}}

			\\newenvironment{exercise}[2][Exercise]{\\begin{trivlist}
			\\item[\\hskip \\labelsep {\\bfseries #1}\\hskip \\labelsep {\\bfseries #2.}]}{\\end{trivlist}}

			\\newenvironment{problem}[2][Problem]{\\begin{trivlist}
			\\item[\\hskip \\labelsep {\\bfseries #1}\\hskip \\labelsep {\\bfseries #2.}]}{\\end{trivlist}}

			\\newenvironment{question}[2][Question]{\\begin{trivlist}
			\\item[\\hskip \\labelsep {\\bfseries #1}\\hskip \\labelsep {\\bfseries #2.}]}{\\end{trivlist}}

			\\newenvironment{corollary}[2][Corollary]{\\begin{trivlist}
			\\item[\\hskip \\labelsep {\\bfseries #1}\\hskip \\labelsep {\\bfseries #2.}]}{\\end{trivlist}}

			 

			\\begin{document}\n\n\n
			\\title{HW 2}
			\\author{""" + self.author + """}
			\\date{}
			\\maketitle
I've completely randomized the following problems so you won't be able to cheat. Recall how to 
graph on the real number line. If $x$ is taken
to be your variable, you will shade in the regions for which the statement is true. For example, if you're
trying to plot $x < 10$, you will shade in everything to the left of $x = 10$ (because everything to the 
left of $x = 10$ is where $x < 10$) and leave unshaded everything to the right of $x = 10$ because that's where
$x > 10$.

Since the problems are randomized, you may have a contradiction such as $x < 10$ and $x > 11$. If that's the case,
don't plot anything and write $\\phi$ down.

Also there's a challenge problem at the end. This one is worth 2 homework passes.

			"""