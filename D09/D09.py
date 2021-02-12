import pandas as pd
DFBoston = pd.read_csv("./D09/boston.csv")
print(DFBoston)


newDF = pd.DataFrame()
newDF.add(DFBoston['CHAS'])
newDF.add(DFBoston['NOX'])
newDF.add(DFBoston['RM'])
print(newDF)

newDF.to_excel("./D09/final.xlsx")