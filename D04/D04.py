import numpy as np

english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,55,60])

chinese_score = np.array([65,90,82,72,66,77])

count = 0
result = np.greater(english_score,math_score)
#np.where(result = True,result,result)

for item in result:
    if(item == True):
        count = count+1

#有多少學生英文成績比數學成績高？        
print(count)

d = np.greater(chinese_score,english_score,math_score)

#是否全班同學最高分都是國文？
print(np.all(d))

#print(np.isin(newArray))


