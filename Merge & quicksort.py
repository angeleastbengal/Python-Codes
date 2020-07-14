
#----------------------------------Working with Merge Sort--------------------------------
def merge_sort(list_data):

    n=len(list_data)
    if n>1:

        mid=len(list_data)//2 #--Calculating the mid index of the list. This index is used for partitioning the list
        left_list=list_data[:mid] #--Left half of the list
        right_list=list_data[mid:]#--Right half of the list

        """
        Using the concept of recursion to split every list into two halves
        """
        merge_sort(left_list)
        merge_sort(right_list)

        i=0 #--Counter for left list
        j=0 #--Counter for right list
        k=0 #--Counter for adding data back toi list

        """
        After the lists are split, two lists should be merged. Merging is the process of taking two smaller sorted
        list and combining them together into a single sorted new list
        """

        while i<len(left_list) and j<len(right_list):

            if left_list[i]<right_list[j]:
                list_data[k]=left_list[i]
                i+=1
            else:
                list_data[k]=right_list[j]
                j+=1

            k+=1

        #--It is possible that at the time of combination, one list might have elements who are not added back
        #--Adding remaining elements from left and right sublist
        while i < len(left_list):
            list_data[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list_data[k] = right_list[j]
            j += 1
            k += 1

    return list_data #--Returning the sorted list

l=[6,5,3,1,99,7,2,4]

print(merge_sort(l))


#--------------------------------Quick Sort-----------------------------
"""
Function Definition:
quick_sort() is used to calculate the first and last index of a list and calling the quick_sort_aux using
these set of inputs
"""
print("-------------------------------Quick Sort--------------------------------------")
def quick_sort(list):
    first=0 #--starting index
    last=len(list)-1 #--ending index
    quick_sort_aux(list,first,last) #--function call


def quick_sort_aux(list,first,last):

    if first<last:
        partition_point=partition(list,first,last)
        print("Partiotion at Index:", partition_point)
        print(list)
        print("After Partitioning:"+str(list[first:partition_point])+str(list[partition_point+1:last+1]))

        quick_sort_aux(list,first,partition_point-1)
        quick_sort_aux(list,partition_point+1,last)



def partition(list,first,last):

    #--Calculate the pivot value; Usually the first element in the list is considered as the pivot value
    pivot=list[first]
    print("Pivot:",pivot)

    left_index=first+1 #--left index starts with the element just after pivot
    right_index=last
    complete=False

    while not complete:

        #-- left and right index should converge on split point, post which the loop should stop
        while pivot>=list[left_index] and left_index<=right_index:
            left_index+=1

        while pivot<=list[right_index] and left_index<=right_index:
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
    #--Returning right index which is the partition point
    return right_index


l=[2,5,3,7,10,12,9]
quick_sort(l)
print(l)


#----------------------------------Fibonacci Series--------------------------------------------

def fibonacci(n):
    # assert n>=1, "fibonacci not defined for n<1"
    if n<=1:
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

#--------------------Fibonacci: Iteratively-----------------------------------

lim=int(input("Enter the term for which fibonacci is required\n"))

sum=1
fibonacci_list=[]
fibonacci_list.append(1)
fibonacci_list.append(1)
for i in range(1,lim-1):
    tmp=fibonacci_list[i]
    sum=fibonacci_list[i-1]
    fibonacci_list.append(sum+tmp)

for element in fibonacci_list:
    print(element,end= " ")


#-----------------------------Linear Search using Recursion-----------------------------------

def linear_Search(element_list,item):

    if len(element_list)==0:
        return False
    else:
        if element_list[0]==item:
            return True
        else:
            return linear_Search(element_list[1:],item)
print()
print("Linear Search")
l=[1,2,3,4,5,6,7,8]
print(linear_Search(l,11))

