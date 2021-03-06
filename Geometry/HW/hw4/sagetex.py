##
## This is file `sagetex.py',
## generated with the docstrip utility.
##
## The original source files were:
##
## sagetexpackage.dtx  (with options: `python')
## py-and-sty.dtx  (with options: `python')
## 
## This is a generated file. It is part of the SageTeX package.
## 
## Copyright (C) 2009 by Dan Drake <ddrake@member.ams.org>
## 
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 2 of the License, or (at your
## option) any later version.
## 
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
## Public License for more details.
## 
## You should have received a copy of the GNU General Public License along
## with this program.  If not, see <http://www.gnu.org/licenses/>.
## 
__version__ = """
  [2009/06/17 v2.2.1 embedding Sage into LaTeX documents]
"""
import sys
if __name__ == "__main__":
  print("""This file is part of the SageTeX package.
It is not meant to be called directly.

This file will be automatically used by Sage scripts generated from a
LaTeX document using the SageTeX package.""")
  sys.exit()
from sage.misc.latex import latex
import os
import os.path
import hashlib
import traceback
import subprocess
import shutil
class SageTeXProcessor():
  def __init__(self, jobname):
    self.progress('Processing Sage code for %s.tex...' % jobname)
    self.didinitplot = False
    self.useimagemagick = False
    self.useepstopdf = False
    self.plotdir = 'sage-plots-for-' + jobname + '.tex'
    self.filename = jobname
    self.souttmp = open(self.filename + '.sout.tmp', 'w')
    s = '% This file was *autogenerated* from the file ' + \
        os.path.splitext(jobname)[0] + '.sage.\n'
    self.souttmp.write(s)
  def progress(self, t,linebreak=True):
    if linebreak:
      print(t)
    else:
      sys.stdout.write(t)
      sys.stdout.flush()
  def initplot(self):
    self.progress('Initializing plots directory')
    if os.path.isdir(self.plotdir):
      shutil.rmtree(self.plotdir)
    os.mkdir(self.plotdir)
    self.didinitplot = True
  def inline(self, counter, s):
    self.progress('Inline formula %s' % counter)
    self.souttmp.write('\\newlabel{@sageinline' + str(counter) + '}{{' + \
                 latex(s).rstrip() + '}{}{}{}{}}\n')
  def blockbegin(self):
    self.progress('Code block begin...', False)
  def blockend(self):
    self.progress('end')
  def plot(self, counter, _p_, format='notprovided', **kwargs):
    if not self.didinitplot:
      self.initplot()
    self.progress('Plot %s' % counter)
    if format == 'notprovided':
      formats = ['eps', 'pdf']
    else:
      formats = [format]
    for fmt in formats:
      if fmt == 'pdf' and self.useepstopdf:
        epsfile = os.path.join(self.plotdir, 'plot-%s.eps' % counter)
        self.progress('Calling epstopdf to convert plot-%s.eps to PDF' % \
            counter)
        subprocess.check_call(['epstopdf', epsfile])
        continue
      plotfilename = os.path.join(self.plotdir, 'plot-%s.%s' % (counter, fmt))
      _p_.save(filename=plotfilename, **kwargs)
      if format != 'notprovided' and self.useimagemagick:
        self.progress('Calling Imagemagick to convert plot-%s.%s to EPS' % \
          (counter, format))
        self.toeps(counter, format)
  def toeps(self, counter, ext):
    subprocess.check_call(['convert',\
      '%s/plot-%s.%s' % (self.plotdir, counter, ext), \
      '%s/plot-%s.eps' % (self.plotdir, counter)])
  def goboom(self, line):
    print('\n**** Error in Sage code on line %s of %s.tex! Traceback\
 follows.' % (line, self.filename))
    traceback.print_exc()
    print('\n**** Running Sage on %s.sage failed! Fix %s.tex and try\
 again.' % ((self.filename,) * 2))
    self.souttmp.close()
    os.remove(self.filename + '.sout.tmp')
    sys.exit(int(1))
  def endofdoc(self):
    sagef = open(self.filename + '.sage', 'r')
    m = hashlib.md5()
    for line in sagef:
      if line[0:12] != " _st_.goboom" and line[0:12] != "print 'SageT":
        m.update(line)
    s = '%' + m.hexdigest() + '% md5sum of corresponding .sage file\
 (minus "goboom" and pause/unpause lines)\n'
    self.souttmp.write(s)
    self.souttmp.close()
    os.rename(self.filename + '.sout.tmp', self.filename + '.sout')
    self.progress('Sage processing complete. Run LaTeX on %s.tex again.' %\
             self.filename)

