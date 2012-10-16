import pyodbc

def makeQuotedStringFromList(valList):
    valString=""
    for i, val in enumerate(valList):
        if len(valList)==1:
            valString="'"+val+"'"            
        elif i==0:
            valString+="'"+val+"', '"
        elif i==len(valList)-1:
            valString+=val+"'"
        else:
            valString+=val+"', '"
    return valString

def makeStringFromList(valList):
    valString=""
    for i, val in enumerate(valList):         
        if i==len(valList)-1:
            valString+=val
        else:
            valString+=val+", "
    return valString

def getConnection(connectionString):
    cnxn = pyodbc.connect(connectionString)
    return cnxn

def selectColumn(tabName, colName, cnxn):
    cursor=cnxn.cursor()
    cursor.execute("SELECT "+colName+" FROM "+tabName)
    return cursor.fetchall()
    
    
def insert(tabName, valList, cnxn, colList=[]):
    #len(valList) must equal len(colList=[]) 
    cursor=cnxn.cursor()
    columns=makeStringFromList(colList)
    valList=makeQuotedStringFromList(valList)
    print columns
    print valList
    if columns!="":
        print "INSERT INTO "+tabName+" ("+columns+") VALUES ("+valList+")"
        cursor.execute("INSERT INTO "+tabName+" ("+columns+") VALUES ("+valList+")")
    else:
        cursor.execute("INSERT INTO "+tabName+" VALUES ( "+valList+" )")
    cnxn.commit()
    
    
