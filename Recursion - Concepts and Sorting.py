"""
Recursion- A function can call any other function including itself. A function that calls itself is called a recursive
function. The result is a virtual loop or repetition used in a fashion similar to a while loop.
"""

def printRev(n):
    if n>0:
        print(n)
        printRev(n-1)

printRev(4)

#--The recursive calls continue until a value of zero is passed to the function at which time the body of the if statement
#--is skipped and execution reaches the end of the function.

"""
All recursive solutions must satisfy three rules or properties:
1. A recursive solution must contain a base case
2. A recursive solution must contain a recursive case
3. A recursive solution must contain a convergence case, i.e. a recursive solution must progress towards the base case
"""

"""
RECURSIVE CASE:
A recursive problem subdivides itself into smaller version of itself. For a problem to be subdivided it must contain
a term that can be divided into smaller sets. This subdivision is handled by the recursive case where the function calls
itself. in printRev() function the recursive case is performed for all values of n>0.

BASE CASE:
The base case is the terminating case and represents the smallest subdivision of the problem. It signals the end of
the virtual loop or the recursive calls. In printRev the base case occurs when n=0 and the function simply returns
without performing any additional operations.

CONVERGENCE CASE:
Finally a recursive solution must progress towards the base case or the recursion will never stop resulting in an infinite
virtual loop. The progression typically occurs in each recursive call, when the larger problem is divided into smaller
parts. The larger term is reduced to a smaller value by each recursive call. in printRev() the progression is achieved
by subtracting one from the current value of n

"""

def factorial(n):

    if n==1: #--base case the program terminates once n=1 is reached, else it continues the virtual loop
        return 1
    else:
        return n * factorial(n-1) #--recursion case and convergence case


print(factorial(5))

def fibonacci(n):



    # assert n>=1, "fibonacci not defined for n<1"
    if n<=1:
        print("I am here")
        print("Returned:",n)
        return n
    else:
        print(n)
        return (fibonacci(n-1)+fibonacci(n-2))

print("fibonacci series")
print(fibonacci(5))
# if __name__=='__main__':
#      for i in range(1,10):
#          print(fibonacci(i),end=" ")
#

#------------------------------------Binary Search----------------------------------

def binary_search(list_elements,search):

    if len(list_elements)==0: #--base case when size of the list becomes zero and element is not found
        return False

    else:
        mid = len(list_elements) // 2 #--finding the mid value
        if list_elements[mid]==search:
            return True
        else:
            if search<list_elements[mid]:
                return binary_search(list_elements[0:mid], search)
            else:
                return binary_search(list_elements[mid+1:],search)


print(binary_search([1,2,3,4,5,6,7],7))

#---------------------------Mystery Function 1: Adding b, a number of times or in simple a*b---------------------------
def mystery_func1(a, b):
    if a == 0:
        return 0
    return b + mystery_func1(a-1, b)

print(mystery_func1(4,5))

#---------------------------Mystery Function 2: Adding up from 1 to n--------------------------------------------------
def mystery_func2(n):
    if n == 1:
        return 1
    return n + mystery_func2(n-1)

print(mystery_func2(5))

def mystery_func3(a, b):
    print(a,",",b)
    if b == 0:
        return 1
    if b % 2 == 0:
        return mystery_func3(a*a, b//2)

    return mystery_func3(a*a, b//2) * a

print(mystery_func3(2,3))


def merge_sort(arr):

    n=len(arr)


    if n>1:
        mid=n//2
        left_list=arr[:mid]
        right_list=arr[mid:]

        merge_sort(left_list)
        merge_sort(right_list)
        print("Splitting:" + str(left_list) + "and" + str(right_list))

        i=0
        j=0
        k=0


        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                arr[k]=left_list[i]
                i+=1
            else:
                arr[k]=right_list[j]
                j+=1

            k+=1

        while i<len(left_list):
            arr[k]=left_list[i]
            i+=1
            k+=1

        while j<len(right_list):
            arr[k]=right_list[j]
            j+=1
            k+=1


    return arr

l=[6,5,3,1,8,7,2,4]

print(merge_sort(l))

#--------------------------------Quick Sort-----------------------------
"""
Function Definition:
quick_sort() is used to calculate the first and last index of a list and calling the quick_sort_aux using
these set of inputs
"""
print("-------------------------------Quick Sort--------------------------------------")
def quick_sort(list):
    first=0
    last=len(list)-1
    quick_sort_aux(list,first,last)


def quick_sort_aux(list,first,last):

    if first<last:
        partition_point=partition(list,first,last)
        print("Partiotion at Index:", partition_point)
        print(list)
        print("After Partitioning:"+str(list[first:partition_point])+str(list[partition_point+1:last+1]))

        quick_sort_aux(list, first,partition_point-1)
        quick_sort_aux(list,partition_point+1,last)




def partition(list,first,last):

    #--Calculate the pivot value; Usually the first element in the list is considered as the pivot value
    pivot=list[first]
    print("Pivot:",pivot)
    left_index=first+1
    right_index=last
    complete=False

    while not complete:

        while pivot>=list[left_index] and left_index<=right_index:
            left_index+=1

        while pivot=<list[right_index] and left_index<=right_index:
            right_index-=1

        if right_index<left_index:
            complete=True
        else:
            tmp=list[left_index]
            list[left_index]=list[right_index]
            list[right_index]=tmp
        print(list)
    #--Swap the pivot element with the element of right index
    list[first],list[right_index]=list[right_index],list[first]
    #--Returning right index which is the partiiton point
    return right_index


l=[2,5,3,7,10,12,9]
quick_sort(l)
