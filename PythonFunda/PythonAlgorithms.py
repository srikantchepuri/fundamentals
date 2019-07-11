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

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest)



    

def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

mylisttest = [100,4,2,16,55,6,77,1,99,102,50]
heapSort(mylisttest) 
print(mylisttest)   


import math
def jumpSearch(arr,x):
    right =int(math.sqrt(len(arr)))
    left=0
    while arr[right-1]<x and right<len(arr):
        left=right
        right+=int(math.sqrt(len(arr)))
        if(right>=len(arr)):
            right=len(arr)
    print(left)
    print(right)
    print("-----")
    
    for i in range(left,right,1):
        if(arr[i]==x):
            print("X found at :",i)
        
arr=[3,4,5,6,9,10,11,13,19]
jumpSearch(arr,11)




#Gas Station Algorithm
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2..
Completing the circuit means starting at i and ending up at i again.

'''

def traverse(gas,cost):
    for i in range(len(gas)):
        count=1
        total_gas=gas[i]
        next_gas=i
        while count<=len(gas):
            if total_gas>=cost[next_gas]:
                total_gas+=gas[next_gas]
                next_gas=(next_gas+1)%len(gas)
                count+=1
            else:
                break
            if(count==len(gas)):
                print("matched")
                return i
            else:
                print("did not match")
                break
    print("did not match")
    return -1
gas=[1,1,1,1,1]
cost=[1,1,1,0,1]
traverse(gas,cost)


#get majority element

def getMajorityElement(arr):
    mydict={}
    for i in arr:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i]=1
    

    return  max(mydict, key=mydict.get)

arr=[2, 2, 2, 3, 4, 4, 5, 6, 7, 8, 2]
getMajorityElement(arr)


def fibo(n,memo):
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2:
        result= 1
    else:
        result= fibo(n-1,memo)+fibo(n-2,memo)
    memo[n]=result
    return result

def fibo_memo(n):
    memo = [None] * (n + 1)
    return fibo(n,memo)

fibo_memo(5)  

def fibo_bottom_up(n):
    if n==1 or n==2 :
        return 1
    bottom_up=[None]*(n+1)
    bottom_up[1]=1
    bottom_up[2]=1
    for i in range(3,n+1):
        bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
    return bottom_up[n]

#Find sets of numbers that add up to N 

def count_sets(arr,total):
    mem={}
    count_sets_sub(arr,total,len(arr)-1,mem)
    
def count_sets_sub(arr,total,i,mem):
    key=str(total)+':'+str(i)
    if total = 0 :
        return 1
    elif total < 0:
        return 0
    elif  i < 0:
        return 0
    elif total < arr[i]:
        to_return=count_sets_sub(arr,total,i-1,mem)
    else:
        to_return=count_sets_sub(arr,total-arr[i],i-1,mem)+count_sets_sub(arr,total,i-1,mem)
    mem[key]=to_return
    return to_return


def helper(arr,k):
    if k == 0:
        return 1
    s=len(arr)-k
    #check if starting index of the sub string we are checking is zero
    if arr[s] =='0':
        return 0
    result = helper(arr,k-1)
    if k>=2 and int(arr[s:s+2])<=26:
        result += helper(arr,k-2)
    return result

def num_ways(arr):
    return helper(arr,len(arr))


def helper_dp(arr,k,memo):
    if k == 0:
        return 1
    s=len(arr)-k
    #check if starting index of the sub string we are checking is zero
    if arr[s] =='0':
        return 0
    if memo[k] is not None:
        return memo[k]
    result = helper_dp(arr,k-1,memo)
    if k>=2 and int(arr[s:s+2])<=26:
        result += helper_dp(arr,k-2,memo)
    memo[k]=result
    return result

def num_ways_dp(arr):
    memo=[None]*(len(arr)+1)
    return helper_dp(arr,len(arr),memo)

arr="123"
num_ways(arr)

num_ways_dp(arr)

abc=[None]*5