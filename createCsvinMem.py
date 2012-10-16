import pyodbc
import sys
import os.path
import csv

def csvInternalObject(inFile):
    mapFile=open(inFile, 'rb')
    mapDict=csv.DictReader(mapFile)
    csvList=[]
    for row in mapDict:
        rowDict={}
        for i in mapDict.fieldnames:
            rowDict[i]=row[i]
        csvList.append(rowDict)
        


