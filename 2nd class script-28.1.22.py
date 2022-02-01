# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:42:47 2022

@author: DELL
"""

from scipy import stats
import pandas as pd
import numpy as np

import itertools
import operator
grades = pd.read_csv("E:\\Deloitte\\data\\grades.csv")
grades = pd.DataFrame(grades)

cs2m = pd.read_csv("E:\\Deloitte\\data\\cs2m.csv")
cs2m.shape
grades.ethnicity.dtype

grades.info()
grades.describe()
grades.skew()
grades.head(10)
grades.ix[:, 0:4].head(3)
grades4 = grades.iloc[:, 0:4]
grades1 = grades.iloc[0:20, 0:3]
grades1 = grades.sample(10)
grades[np.compress(grades.total, grades.total == 80)]

grades[grades.quiz1 == 8].iloc[:, 0:3]
grades[grades['quiz1'] == 8]


cs2m[np.compress(cs2m.BP, cs2m.BP == 170)]
grades.info()


cs2m[(cs2m.DrugR == 1) and (cs2m.Age > 20)]
grade3 = grades[grades.ethnicity == 3]
grade5 = grades[grades.ethnicity == 5]
pd.concat([grade3, grade5])

cs2m["newvar1"] = np.where((cs2m["Chlstrl"] > 175) & (cs2m["BP"] > 175),
                           "H", "L")

grades['newvar1'] = (grades['total']/200)*100
del grades['newvar1']
grades.drop(['x', 'y'], asix=1)

cs2m = cs2m.drop(['newvar'], axis=1)

stats.describe(cs2m)

# Functin


def plus1(a, b=1):
    return a+b


plus1(8)
plus1(230, 25)


def factorial1(n):
    x = 1
    for i in range(1, n+1):
        x = x*i
    return x


def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n1-1)


factorial1(-6)

fact(0)



def is_even(l):
    e=[]
    for n in l:
        if n%2==0:
            e.append(n)
    return e

is_even([1,2,3,4,5,8,59,75,68,99])
