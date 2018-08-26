## This file (hw3outAngel.sage) was *autogenerated* from the file hw3outAngel.tex.
import sagetex
_st_ = sagetex.SageTeXProcessor('hw3outAngel')
_st_.blockbegin()
try:
 from random import randint
 import random
 from datetime import datetime
 random.seed(datetime.now())
 import numpy as np
 var('A,B,C,D')
except:
 _st_.goboom(67)
_st_.blockend()
_st_.blockbegin()
try:
 A = randint(10,100)
 B = randint(10,200)
 C = randint(10,300)
 D = B
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 S = point([C,D])
except:
 _st_.goboom(81)
_st_.blockend()
try:
 _st_.plot(0, format='notprovided', _p_=P+Q+S)
except:
 _st_.goboom(83)
try:
 _st_.inline(0, A)
except:
 _st_.goboom(86)
try:
 _st_.inline(1, B)
except:
 _st_.goboom(86)
try:
 _st_.inline(2, C)
except:
 _st_.goboom(86)
try:
 _st_.inline(3, D)
except:
 _st_.goboom(86)
_st_.blockbegin()
try:
 A = randint(10,100)
 B = randint(10,200)
 C = A
 D = randint(10,50)
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 S = point([C,D])
except:
 _st_.goboom(102)
_st_.blockend()
try:
 _st_.plot(1, format='notprovided', _p_=P+Q+S)
except:
 _st_.goboom(104)
try:
 _st_.inline(4, A)
except:
 _st_.goboom(107)
try:
 _st_.inline(5, B)
except:
 _st_.goboom(107)
try:
 _st_.inline(6, C)
except:
 _st_.goboom(107)
try:
 _st_.inline(7, D)
except:
 _st_.goboom(107)
_st_.blockbegin()
try:
 A = randint(10,100)
 B = randint(10,200)
 C = randint(10,300)
 D = randint(10,50)
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 S = point([C,D])
except:
 _st_.goboom(123)
_st_.blockend()
try:
 _st_.plot(2, format='notprovided', _p_=P+Q+S)
except:
 _st_.goboom(125)
try:
 _st_.inline(8, A)
except:
 _st_.goboom(128)
try:
 _st_.inline(9, B)
except:
 _st_.goboom(128)
try:
 _st_.inline(10, C)
except:
 _st_.goboom(128)
try:
 _st_.inline(11, D)
except:
 _st_.goboom(128)
_st_.blockbegin()
try:
 var('m')
 y = function('y')
 m = randint(-5,5)
 A = randint(10,100)
 B = randint(10,200)
 C = randint(10,300)
 D = randint(10,50)
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 LA = text('A', (A,B+.1*max(D,B,max(y(A),y(C)))))
 S = point([C,D])
 LS = text('B', (C,D))
 y(x) = (B+D)/2.0 + m*(x-(A+C)/2.0)
 LA = text('A', (A,B+.03*max(D,B,max(y(A),y(C)))))
 LS = text('B', (C,D+.03*max(D,B,max(y(A),y(C)))))
 T = plot(y, (x, min(A,C), max(A,C)))
except:
 _st_.goboom(152)
_st_.blockend()
try:
 _st_.plot(3, format='notprovided', _p_=P+Q+S+T+LA+LS)
except:
 _st_.goboom(154)
try:
 _st_.inline(12, A)
except:
 _st_.goboom(157)
try:
 _st_.inline(13, B)
except:
 _st_.goboom(157)
try:
 _st_.inline(14, C)
except:
 _st_.goboom(157)
try:
 _st_.inline(15, D)
except:
 _st_.goboom(157)
try:
 _st_.inline(16, y(x))
except:
 _st_.goboom(161)
_st_.blockbegin()
try:
 var('m')
 y = function('y')
 m = randint(-5,5)
 A = randint(10,100)
 B = randint(10,200)
 C = randint(10,300)
 D = randint(10,50)
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 LA = text('A', (A,B+.03*max(D,B,max(y(A),y(C)))))
 S = point([C,D])
 LS = text('B', (C,D))
 y(x) = (B+D)/2.0 + m*(x-(A+C)/2) + 1
 LA = text('A', (A,B+.03*max(D,B,max(y(A),y(C)))))
 LS = text('B', (C,D+.03*max(D,B,max(y(A),y(C)))))
 T = plot(y, (x, min(A,C), max(A,C)))
except:
 _st_.goboom(187)
_st_.blockend()
try:
 _st_.plot(4, format='notprovided', _p_=P+Q+S+T+LA+LS)
except:
 _st_.goboom(189)
try:
 _st_.inline(17, A)
except:
 _st_.goboom(192)
try:
 _st_.inline(18, B)
except:
 _st_.goboom(192)
try:
 _st_.inline(19, C)
except:
 _st_.goboom(192)
try:
 _st_.inline(20, D)
except:
 _st_.goboom(192)
try:
 _st_.inline(21, y(x))
except:
 _st_.goboom(196)
_st_.blockbegin()
try:
 B = randint(4,20)
 C = randint(10, 1000)
except:
 _st_.goboom(207)
_st_.blockend()
_st_.endofdoc()
