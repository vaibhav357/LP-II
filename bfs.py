import itertools						

def bfsalgo(childtree, openlist, closelist,goal):
	'''Implementation of BFS algo'''
	X=openlist[0]		
	print("\n\n X = {}".format(X))	
	closelist.append(X)	
	for i in range(len(childtree)):

		if(X==childtree[i][0]):		
			openlist.append(childtree[i][1:])	

	openlist=list(itertools.chain(*openlist))	
	del openlist[0]			

	if(X!=goal):			
		print("\n OPEN {}	CLOSE {}".format(openlist,closelist))	

	if(X==goal):			
		print('\n SUCCESS')
	elif(len(openlist)>0):	
		bfsalgo(childtree, openlist, closelist,goal)
	else:					
		print('\n\n FAILURE')


def createTree(treearr, treelength):
	'''Creating a child's child tree'''
	try:
		for i in range(treelength):
			childtree[i].append(treearr[i+1])		
			checkchild=input("\n Does "+treearr[i+1]+" has any child node Press n for no :	")	
			if(checkchild=='n'):
				print()
			else:
				checkchildsibling=""
				while(checkchildsibling!='n'):
					childname=input("\n Enter child node :	")				
					childtree[i].append(childname)							
					checkchildsibling = input("\n Does "+treearr[i+1]+" has any other children Press n for no :	")
	except IndexError:
		pass

treearr=[]										
root=input("Enter the root node :	")			

treearr.append(root)							

checkchild=input("\n Does "+root+" has any child node Press n for no :	")	
if(checkchild=='n'):
	print(treearr)															
else:
	checkchildsibling=""
	while(checkchildsibling!='n'):											
		childname=input("\n Enter child node :	")							
		treearr.append(childname)											
		checkchildsibling = input("\nDoes "+root+" has any other child Press n for no :	") 

treelength=len(treearr)						
childtree=[[] for x in range(treelength-1)]	
createTree(treearr,treelength)				

print("\n\n Tree successfully created root node wtih children\n")
print(treearr)

print("\n\n Children with their children and siblings \n")
print(childtree)							

goal=input("\n Enter the goal node :	")	

openlist=[]
closelist=[]

X=treearr[0]							
print("\n\n X = "+X)

openlist.append(treearr[1:])			
openlist=list(itertools.chain(*openlist))	
closelist.append(X)						
print("\nOPEN {}	CLOSE {}".format(openlist,closelist))	


bfsalgo(childtree,openlist,closelist,goal)	
