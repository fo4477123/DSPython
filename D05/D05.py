import numpy as np

english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,np.nan,60])

chinese_score = np.array([65,90,82,72,66,77])

#max
MathMax = np.nanmax(math_score)
ChMax = np.nanmax(chinese_score)
EnMax = np.nanmax(english_score)
#min
MathMin = np.nanmin(math_score)
ChMin = np.nanmin(chinese_score)
EnMin = np.nanmin(english_score)
#mean
MathMean = np.nanmean(math_score)
ChMean = np.nanmean(chinese_score)
EnMean = np.nanmean(english_score)
#AVG
MathAvg = np.average(math_score)
ChAvg = np.average(chinese_score)
EnAvg = np.average(english_score)
#std
MathSTD = np.nanstd(math_score)
ChSTD = np.nanstd(chinese_score)
EnSTD = np.nanstd(english_score)


new_math_score = np.array([60,85,60,68,55,60])

#max
MathMax = np.nanmax(new_math_score)
#min
MathMin = np.nanmin(new_math_score)
#mean
MathMean = np.nanmean(new_math_score)
#AVG
MathAvg = np.average(new_math_score)
#std
MathSTD = np.nanstd(new_math_score)


result = np.cov(chinese_score,new_math_score)
result2 = np.cov(chinese_score,english_score)
d=np.greater(result,result2)
if(np.all(d) == True):
    print ("數學")
else:
    print("英文")
