#note: to finish make it runnable from command line with inFile and outFile parameters 
import sys
import codecs
import os.path
import csv
from xml.etree import ElementTree

def addInfo(outFile):
    xmlFile=open(u'C:\\Users\\srobbins\\Desktop\\refworks_xml.xml', 'rb')
    xmlTree=ElementTree.ElementTree()
    xmlTree.parse(xmlFile)     
    csvFile=codecs.open(outFile, encoding='utf-8', mode='wb')
    #testOutput=open(r'C:\Users\srobbins\Desktop\OutPut\mapTest.csv', 'wb')
    fieldnames=[]
    for i in xmlTree.iterfind("reference"):
        for j in i.iter():
            if j.tag!='k1'and j.tag!="reference" and j.tag not in fieldnames:
                fieldnames.append(j.tag)
    xmlFile.seek(0)
    for i in xmlTree.iterfind("reference"):
        for j in i.iter():
            if j.tag=='k1' and j.text not in fieldnames:
                fieldnames.append(j.text)
    xmlFile.seek(0)
    csvDict=csv.DictWriter(csvFile, fieldnames)
    csvDict.writeheader()
    for i in xmlTree.iterfind("reference"):
        row={}
        for j in i.iter():
            if j.tag in csvDict.fieldnames:
                row[j.tag]=j.text    
            if j.tag=='k1':
                row[j.text]='X'
        for k in row.keys():
            row[k]=row[k].encode('ascii', 'xmlcharrefreplace')
            
        csvDict.writerow(row)
    xmlFile.seek(0)

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: python test.py outfile.xml'
        sys.exit(-1)
    outFileName = args[0]
## if os.path.exists(outFileName):
## print 'error: out-file already exists'
## sys.exit(-1)
    addInfo(outFileName)

if __name__ == '__main__':
    main()
