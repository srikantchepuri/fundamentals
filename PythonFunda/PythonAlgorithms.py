#Linear Search

def LinearSearch(mylist, searchval):
    position = -1
    for i in range(len(mylist)):
        if mylist[i]==searchval:
            position=i

    if position==-1:
        print("Search value not found in the array")
    else:
        print("Search value found in the array at :",position)

LinearSearch([1,2,3,4,5,6,77,88,99,100,101],99)


#Binary Search

def BinarySearch(mylist, key):
    position = -1
    left=0
    right=len(mylist)-1
    print("before while")
    while(left<=right):
        mid=(left+right)//2
        if(key==mylist[mid]):
            position=mid
            break
        elif (key>mylist[mid]):
            left=mid+1
        else:
            right=mid-1 
    print(position)
    
BinarySearch([1,2,3,4,5,6,77,88,99,100,101],77)    


mylisttest=[1,2,3,4,5,6,77,88,99,100,101]
#Binary Search Recursively
def BinarySearchRecursive(mylist,key, left, right):
    if(left>right):
        print("Not found")
        return False
    mid=(left+right)//2
    if(key==mylist[mid]):
        print("Found")
        return True
    elif key>mylist[mid]:
        BinarySearchRecursive(mylist,key,mid+1,right)
        
    else:
        BinarySearchRecursive(mylist,key,left,mid-1)
        

BinarySearchRecursive(mylisttest,77,0,len(mylisttest)-1)  
BinarySearchRecursive(mylisttest,773,0,len(mylisttest)-1)  

#Bubble Sort - Bubble the max to the end
mylisttest=[100,4,2,16,55,6,77,1,99,102,50]

def BubbleSort(mylist):
    for i in range(len(mylist)):
        for j in range(1,len(mylist)-i):
            if(mylist[j] < mylist[j-1]):
                swap=mylist[j-1]
                mylist[j-1]=mylist[j]
                mylist[j]=swap
    print(mylist)            
        

BubbleSort(mylisttest)


#A different way to implememt bubble sort

mylisttest=[100,4,2,16,55,6,77,1,99,102,50]

def BubbleSortV2(mylist):
    isSorted=False
    while isSorted==False:
        isSorted=True
        for i in range(len(mylist)-1):
            if(mylist[i]>mylist[i+1]):
                swap=mylist[i]
                mylist[i]=mylist[i+1]
                mylist[i+1]=swap
                isSorted=False

    print(mylist)            
        

BubbleSortV2(mylisttest)


#Selection Sort - Bring the lowest number to the left 
mylisttest=[100,4,2,16,55,6,77,1,99,102,50]

def SelectionSort(mylist):
    for i in range(len(mylist)):
        min=i
        for j in range(i+1,len(mylist)):
            if(mylist[min] > mylist[j]):
                min=j
        swap=mylist[i]
        mylist[i]=mylist[min]
        mylist[min]=swap
    print(mylist)
SelectionSort(mylisttest)


#Insertion Sort - Insert each element from unsorted array into sorted array

mylisttest=[100,4,2,16,55,6,77,1,99,102,50]
def InsertSort(mylist):
    for i in range(1,len(mylist)):
        j=i
        while(j>0 and mylist[j]<mylist[j-1]):
                swap=mylist[j]
                mylist[j]=mylist[j-1]
                mylist[j-1]=swap
                j-=1
    print(mylist)


InsertSort(mylisttest)

#Merge Sort
mylisttest=[100,4,2,16,55,6,77,1,99,102,50]
def MergeSort(mylist):
    if(len(mylist)>1):
        mid=len(mylist)//2
        leftList=mylist[:mid]
        rightList=mylist[mid:]
        MergeSort(leftList)
        MergeSort(rightList)
        #Merge
        i=j=k=0

        while i<len(leftList) and j<len(rightList):
            if(leftList[i]<rightList[j]):
                mylist[k]=leftList[i]
                i+=1
            else:
                mylist[k]=rightList[j]
                j+=1
            k+=1
        while i<len(leftList):
            mylist[k]=leftList[i]
            i+=1
            k+=1
        while j<len(rightList):
            mylist[k]=rightList[j]
            j+=1
            k+=1
    #print(mylist)

#Run Merge Sort
MergeSort(mylisttest)
print(mylisttest)



#Heap Sort Implementation

def heapify(mylist,hroot):
    max=hroot
    left = hroot * 2 + 1
    right = hroot * 2 + 2
    print(left)
    print(right)
    if hroot < len(mylist) and mylist[hroot] < mylist[left]:
        max = left

    if hroot < len(mylist) and mylist[max] < mylist[right]:
        max = right

    if hroot != max:
        swap = mylist[hroot]
        mylist[hroot] = mylist[max]
        mylist[max] = swap
        heapify(mylist, max)



    

def buildMaxheap(mylist):
    hroot =(len(mylist))//2-1
    print(hroot)
    while hroot>=0:
        print(hroot)
        #heapify1(mylist,len(mylist),hroot)
        heapify(mylist,hroot)
        hroot=hroot-1
    
    print(mylist)

mylisttest = [100,4,2,16,55,6,77,1,99,102,50]
heapify(mylisttest,3)


buildMaxheap(mylisttest)    


