b = int(input("enter number of process >>>"))
aa=[]
timer=0
for i in range (0,b):
	a=[]
	at = 0
	print 'assume arrival time is 0'
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
			if aa[j][1] > aa[j+1][1] :
				aa[j], aa[j+1] = aa[j+1], aa[j]
		
	
bubbleSort(aa)	
print aa

if aa[0][0]==0:
  print (" ") 
  print("process 1 wait for :" +str(0))
  print (" ") 
  print("process 1 start at :" +str(aa[0][0])) 
  print (" ")
  print("process 1 ends at :" +str(aa[0][1]))
  print (" ") 
if aa[0][0]!=0:
  print("process 1 wait for :" +str(aa[0][0]))
  print (" ") 
  print("process 1 start at :" +str(aa[0][0])) 
  print (" ")
  print("process 1 ends at :" +str(aa[0][1]+aa[0][0]))
  print (" ")

wait=aa[0][0] 
start= aa[0][0]
end = aa[0][0]+aa[0][1]

for i in range (1,b):
  if aa[i][0]>end:	
	  wait=aa[i][0]-end
	  start=aa[i][0]
	  end=aa[i][0]+aa[i][1]
	
	  print ("   ")
	  print'process ' +str(i+1)   ,'wait for :' +str(wait)
	  print ("   ")
	  print 'process ' +str(i+1) ,' start at :' + str(start)
	
	  print ("   ")
	  print'process' +str(i+1) , 'ends at :' + str (end)
	  print ("   ")
  else:
	  wait=0
	  start=end
	  end=end+aa[i][1]
	
	  print ("   ")
	  print 'process ' +str(i+1) , ' wait for : ' +str(wait)
	
	  print ("   ")
	  print 'process ' +str(i+1) ,' start at :' + str(start)
	
	  print ("   ")
	  print'process' +str(i+1) , 'ends at :' + str (end)
	  print ("   ")