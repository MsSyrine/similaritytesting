# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
def cosine_similarity(t1,t2):
    "cosine similarity of T1 to T2: (t1 dot t2)/{||t1||*||t2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(t1)):
        x = t1[i]; y = t2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

t1,t2 = [453, 45], [54, 1]
print(t1, t2, cosine_similarity(t1,t2))

