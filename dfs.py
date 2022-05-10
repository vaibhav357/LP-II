import itertools 
def dfsalgo(childtree, openlist, closelist,goal):
    X=openlist[0]
    print("\n\n X = {}".format(X))
    closelist.append(X)
    for i in range(len(childtree)):
        if(X==childtree[i][0]):
            openlist.insert(0,childtree[i][1:])
            openlist=list(itertools.chain(*openlist))
            openlist.remove(X)
        if(X!=goal):
            print("\n OPEN {} CLOSE {}".format(openlist,closelist)) 
            if(X==goal):
                print('\n SUCCESS')
            elif(len(openlist)>0):
                dfsalgo(childtree, openlist, closelist,goal)
        else:
            print('\n\n FAILURE')

def createTree(roottree, treelength):
    try:
        for i in range(treelength):
            childtree[i].append(roottree[i+1])
            checkchild=input("\n Does "+roottree[i+1]+" has any child node Press n for no : ")
            if(checkchild=='n'):
                print()
            else:
                checkchildsibling=""
                while(checkchildsibling!='n'):
                    childname=input("\n Enter child node : ")
                    childtree[i].append(childname)
                    checkchildsibling = input("\n Does "+roottree[i+1]+" has any other children Press n for no: ")
    except IndexError:
        pass
roottree=[]
root=input("Enter the root node : ")
roottree.append(root)
checkchild=input("\n Does "+root+" has any child node Press n for no : ")
if(checkchild=='n'):
    print(roottree) 
else:
    checkchildsibling=""
    while(checkchildsibling!='n'):
        childname=input("\n Enter child node : ")
        roottree.append(childname)
        checkchildsibling = input("\nDoes "+root+" has any other child Press n for no : ")
treelength=len(roottree) 
childtree=[[] for x in range(treelength-1)] 
createTree(roottree,treelength) 
print("\n\n Tree successfully created root node wtih children\n")
print(roottree)
print("\n\n Children with their children and siblings \n")
print(childtree)
goal=input("\n Enter the goal node : ") 
openlist=[]
closelist=[]
X=roottree[0]
print("\n\n X = "+X)
openlist.append(roottree[1:])
openlist=list(itertools.chain(*openlist))
closelist.append(X) 
print("\nOPEN {} CLOSE {}".format(openlist,closelist))

