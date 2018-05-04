b = int(input("enter number of process >>>"))
aa=[]
l1=[]

for i in range (0,b):
	a=[]
	
	at = int(input("enter arrival time of process >>>"))
	a.append(at)
	bt = int(input("enter burst time of process >>>"))
	a.append(bt)
	aa.append(a)

def bubbleSort(aa):
	n = len(aa)
	
    # Traverse through all array elements
	for i in range(n):
		
        # Last i elements are already in place
		for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
			if aa[j][0] > aa[j+1][0] :
				aa[j], aa[j+1] = aa[j+1], aa[j]
		
	
bubbleSort(aa)
qt = int(input("enter quantum time  of process >>>"))

if aa[0][0]==0:
	if(aa[0][1]>qt):	
		print (" ") 
		print (" ") 
		print("process 1 start at :" +str(aa[0][0])) 
		print (" ")	
		print ("process 1 ends at :" +str(qt+aa[0][0]))
		tem=[]
		tem.append(0)
		temp = aa[0][1]-qt
		tem.append(temp)
		l1=[]
		l1.append(tem)
		aa[0][1]=qt
		print l1
	else:
		print (" ") 
		print (" ") 
		print("process 1 start at :" +str(aa[0][0])) 
		print (" ")
		print("process 1 ends at :" +str(aa[0][1]))
		print (" ")
		
if aa[0][0]!=0:
	print (" ") 
	if(aa[0][1]>qt): 
	 
		print("process 1 start at :" +str(aa[0][0])) 
		print (" ")
		print("process 1 ends at :" +str(aa[0][0]+qt))
		print (" ") 
		tem1=[]
		tem1.append(0)
		
		temp = aa[0][1]-qt
		tem1.append(temp)
		
		l1.append(tem1)
		aa[0][1]=qt
		print l1
	else:
		
		print (" ") 
		print("process 1 start at :" +str(aa[0][0])) 
		print (" ")
		print("process 1 ends at :" +str(aa[0][1]+qt))
		print (" ")
	

wait=aa[0][0] 
start= aa[0][0]
end = aa[0][0]+aa[0][1]
print end

for i in range (1,b):
  if aa[i][0]>end:	
	  wait=aa[i][0]-end
	  start=aa[i][0]
	
	  
	  if(aa[i][1]>qt): 
	 
		print("process 1 start at :" +str(start)) 
		print (" ")
		print("process 1 ends at :" +str(qt+start))
		print (" ") 
		tem2=[]
		tem2.append(0)
		
		temp = aa[i][1]-qt
		tem2.append(temp)
		
		l1.append(tem2)
		aa[i][1]=qt
		print l1
	  else:
		print (" ") 
		
		print("process 1 start at :" +str(start)) 
		print (" ")
		print("process 1 ends at :" +str(start+aa[i][1]))
		print (" ")
	
  else:
	  wait=0
	  start=end
	  
	
	  if(aa[i][1]>qt): 
	 
		print("process 1 start at :" +str(start)) 
		print (" ")
		print("process 1 ends at :" +str(qt+start))
		print (" ") 
		tem=[]
		tem.append(0)
		
		temp = aa[i][1]-qt
		tem.append(temp)
		l1=[]
		l1.append(tem)
		aa[i][1]=qt
		print l1
	  else:
		
		print (" ") 
		print("process 1 start at :" +str(start)) 
		print (" ")
		print("process 1 ends at :" +str(start+aa[i][1]))
		print (" ")
	