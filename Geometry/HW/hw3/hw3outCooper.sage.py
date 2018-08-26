
# This file was *autogenerated* from the file hw3outCooper.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_200 = Integer(200); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_189 = Integer(189); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_0 = Integer(0); _sage_const_207 = Integer(207); _sage_const_20 = Integer(20); _sage_const_161 = Integer(161); _sage_const_67 = Integer(67); _sage_const_21 = Integer(21); _sage_const_86 = Integer(86); _sage_const_187 = Integer(187); _sage_const_81 = Integer(81); _sage_const_83 = Integer(83); _sage_const_157 = Integer(157); _sage_const_p03 = RealNumber('.03'); _sage_const_154 = Integer(154); _sage_const_152 = Integer(152); _sage_const_192 = Integer(192); _sage_const_2p0 = RealNumber('2.0'); _sage_const_196 = Integer(196); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_p1 = RealNumber('.1'); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_50 = Integer(50); _sage_const_123 = Integer(123); _sage_const_125 = Integer(125); _sage_const_100 = Integer(100); _sage_const_102 = Integer(102); _sage_const_104 = Integer(104); _sage_const_107 = Integer(107); _sage_const_300 = Integer(300); _sage_const_1000 = Integer(1000); _sage_const_128 = Integer(128); _sage_const_16 = Integer(16)## This file (hw3outCooper.sage) was *autogenerated* from the file hw3outCooper.tex.
import sagetex
_st_ = sagetex.SageTeXProcessor('hw3outCooper')
_st_.blockbegin()
try:
 from random import randint
 import random
 from datetime import datetime
 random.seed(datetime.now())
 import numpy as np
 var('A,B,C,D')
except:
 _st_.goboom(_sage_const_67 )
_st_.blockend()
_st_.blockbegin()
try:
 A = randint(_sage_const_10 ,_sage_const_100 )
 B = randint(_sage_const_10 ,_sage_const_200 )
 C = randint(_sage_const_10 ,_sage_const_300 )
 D = B
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 S = point([C,D])
except:
 _st_.goboom(_sage_const_81 )
_st_.blockend()
try:
 _st_.plot(_sage_const_0 , format='notprovided', _p_=P+Q+S)
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.inline(_sage_const_0 , A)
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.inline(_sage_const_1 , B)
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.inline(_sage_const_2 , C)
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.inline(_sage_const_3 , D)
except:
 _st_.goboom(_sage_const_86 )
_st_.blockbegin()
try:
 A = randint(_sage_const_10 ,_sage_const_100 )
 B = randint(_sage_const_10 ,_sage_const_200 )
 C = A
 D = randint(_sage_const_10 ,_sage_const_50 )
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 S = point([C,D])
except:
 _st_.goboom(_sage_const_102 )
_st_.blockend()
try:
 _st_.plot(_sage_const_1 , format='notprovided', _p_=P+Q+S)
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.inline(_sage_const_4 , A)
except:
 _st_.goboom(_sage_const_107 )
try:
 _st_.inline(_sage_const_5 , B)
except:
 _st_.goboom(_sage_const_107 )
try:
 _st_.inline(_sage_const_6 , C)
except:
 _st_.goboom(_sage_const_107 )
try:
 _st_.inline(_sage_const_7 , D)
except:
 _st_.goboom(_sage_const_107 )
_st_.blockbegin()
try:
 A = randint(_sage_const_10 ,_sage_const_100 )
 B = randint(_sage_const_10 ,_sage_const_200 )
 C = randint(_sage_const_10 ,_sage_const_300 )
 D = randint(_sage_const_10 ,_sage_const_50 )
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 S = point([C,D])
except:
 _st_.goboom(_sage_const_123 )
_st_.blockend()
try:
 _st_.plot(_sage_const_2 , format='notprovided', _p_=P+Q+S)
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.inline(_sage_const_8 , A)
except:
 _st_.goboom(_sage_const_128 )
try:
 _st_.inline(_sage_const_9 , B)
except:
 _st_.goboom(_sage_const_128 )
try:
 _st_.inline(_sage_const_10 , C)
except:
 _st_.goboom(_sage_const_128 )
try:
 _st_.inline(_sage_const_11 , D)
except:
 _st_.goboom(_sage_const_128 )
_st_.blockbegin()
try:
 var('m')
 y = function('y')
 m = randint(-_sage_const_5 ,_sage_const_5 )
 A = randint(_sage_const_10 ,_sage_const_100 )
 B = randint(_sage_const_10 ,_sage_const_200 )
 C = randint(_sage_const_10 ,_sage_const_300 )
 D = randint(_sage_const_10 ,_sage_const_50 )
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 LA = text('A', (A,B+_sage_const_p1 *max(D,B,max(y(A),y(C)))))
 S = point([C,D])
 LS = text('B', (C,D))
 __tmp__=var("x"); y = symbolic_expression((B+D)/_sage_const_2p0  + m*(x-(A+C)/_sage_const_2p0 )).function(x)
 LA = text('A', (A,B+_sage_const_p03 *max(D,B,max(y(A),y(C)))))
 LS = text('B', (C,D+_sage_const_p03 *max(D,B,max(y(A),y(C)))))
 T = plot(y, (x, min(A,C), max(A,C)))
except:
 _st_.goboom(_sage_const_152 )
_st_.blockend()
try:
 _st_.plot(_sage_const_3 , format='notprovided', _p_=P+Q+S+T+LA+LS)
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.inline(_sage_const_12 , A)
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.inline(_sage_const_13 , B)
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.inline(_sage_const_14 , C)
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.inline(_sage_const_15 , D)
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.inline(_sage_const_16 , y(x))
except:
 _st_.goboom(_sage_const_161 )
_st_.blockbegin()
try:
 var('m')
 y = function('y')
 m = randint(-_sage_const_5 ,_sage_const_5 )
 A = randint(_sage_const_10 ,_sage_const_100 )
 B = randint(_sage_const_10 ,_sage_const_200 )
 C = randint(_sage_const_10 ,_sage_const_300 )
 D = randint(_sage_const_10 ,_sage_const_50 )
 P = line([[A,B],[C,D]])
 Q = point([A,B])
 LA = text('A', (A,B+_sage_const_p03 *max(D,B,max(y(A),y(C)))))
 S = point([C,D])
 LS = text('B', (C,D))
 __tmp__=var("x"); y = symbolic_expression((B+D)/_sage_const_2p0  + m*(x-(A+C)/_sage_const_2 ) + _sage_const_1 ).function(x)
 LA = text('A', (A,B+_sage_const_p03 *max(D,B,max(y(A),y(C)))))
 LS = text('B', (C,D+_sage_const_p03 *max(D,B,max(y(A),y(C)))))
 T = plot(y, (x, min(A,C), max(A,C)))
except:
 _st_.goboom(_sage_const_187 )
_st_.blockend()
try:
 _st_.plot(_sage_const_4 , format='notprovided', _p_=P+Q+S+T+LA+LS)
except:
 _st_.goboom(_sage_const_189 )
try:
 _st_.inline(_sage_const_17 , A)
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.inline(_sage_const_18 , B)
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.inline(_sage_const_19 , C)
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.inline(_sage_const_20 , D)
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.inline(_sage_const_21 , y(x))
except:
 _st_.goboom(_sage_const_196 )
_st_.blockbegin()
try:
 B = randint(_sage_const_4 ,_sage_const_20 )
 C = randint(_sage_const_10 , _sage_const_1000 )
except:
 _st_.goboom(_sage_const_207 )
_st_.blockend()
_st_.endofdoc()

