def bubbleSort(alist):


   for i in range(len(alist)-1,0,-1):


       for j in range(i):

           #Comparing element with its right side neighbor
           if alist[j] > alist[j+1]:

               #swapping
               temp = alist[j]
               alist[j] = alist[j+1]
               alist[j+1] = temp

   return alist
