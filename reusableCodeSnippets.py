#reuseable code snippets

## add a directory to pythonpath, replace __somepath__ with directory
if "__somepath__" not in sys.path:
    sys.path.append("__somepath__")

##make commandline executeable
if __name__ == "__main__":
    import sys#not needed if sys already imported
    fib(int(sys.argv[1]))#demonstrates how to use sys.argv list

#function to make list from  
def makeStringFromList(valList):
    valString=""
    for i, val in enumerate(valList):
        if i==len(valList):
            valString+=val
        else:
            colString+=val+", "
    return valString
