import pandas as pd
import numpy as np

## 20 points male
# man1

## 20 points female
# man1

import random

def randomize(n,lower,upper):
    randomlist = []
    for i in range(0,n):
        int = random.randint(lower,upper)
        randomlist.append(int)
    return randomlist

## FEMALE
man1 = randomize(21,60,90) #80
man2 = randomize(21,30,60) #40
man3 = randomize(21,30,60) #95
man4 = randomize(21,75,100) #65
man5 = randomize(21,55,72) #70
man6 = randomize(21,55,72) #50
man7 = randomize(21,47,78)#60
man8 = randomize(21,76,89)#70
man9 = randomize(21,18,46)#30
man10 = randomize(21,54,67)#60
man11 = randomize(21,43,87)#55
man12 = randomize(21,65,79)#58
man13  = randomize(21,74,95)#90

#dff = pd.DataFrame(list(zip(man1,man2,man3,man4, man5, man6, man7, man8, man9,man10, man11, man12, man13)),
#               columns =['man1','man2','man3','man4', 'man5', 'man6', 'man7', 'man8', 'man9','man10', 'man11', 'man12', 'man13'])

dff['ggt'] = 'female'

## MALE
man1 = randomize(18,24,55) #30
man2 = randomize(18,76,99) #90
man3 = randomize(21,34,53) #40
man4 = randomize(21,24,44) #25
man5 = randomize(21,65,79) #70
man6 = randomize(21,18,52) #25
man7 = randomize(21,43,67) #50
man8 = randomize(21,44,52) #45
man9 = randomize(21,74,92) #85
man10 = randomize(21,38,56) #45
man11 = randomize(21,71,93) #80
man12 = randomize(21,45,62) #55
man13  = randomize(21,73,92) #85



#dfm = pd.DataFrame(list(zip(man1,man2,man3,man4, man5, man6, man7, man8, man9,man10, man11, man12, man13)),
#               columns =['man1','man2','man3','man4', 'man5', 'man6', 'man7', 'man8', 'man9','man10', 'man11', 'man12', 'man13'])

dfm['ggt'] = 'male'



finaldf = dff.append(dfm)


finaldf.to_csv('testratings.csv')
