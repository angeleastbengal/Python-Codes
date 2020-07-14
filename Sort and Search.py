
#------------------------------Bubble Sort---------------------------------------
def bubble_sort(list):
    #--bubble sort represents use of bubble, i.e. the biggest bubble sits at the end

    for i in range(1,len(list)+1): #---Traverse the entire list
        for y in range(0,len(list)-i): #-- Traverse entire list - items sorted at the end
            if list[y]>list[y+1]: #--Push highest element at the top
                temp=list[y]
                list[y]=list[y+1]
                list[y+1]=temp
        print(list)
    return list

l_data=[5, 6, 3, 1, 2, 7]
bubble_sort(l_data)

print("-------------------Selection Sort---------------------------")

def selection_sort(list):

#--Arranging data in sequence
    for i in range(len(list)-1,0,-1):

        #--Assumed position of largest value
        pos=0

        for y in range(1,i+1):
            if list[pos]<list[y]: #--If a value smaller than small is found
                pos=y #--Position is stored


        temp=list[i]
        list[i]=list[pos]
        list[pos]=temp
        print(list)

    return list

l_data=[5, 6, 3, 1, 2, 7]
selection_sort(l_data)

print("-------------------Selection Sort---------------------------")
def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp
        print(a_list)


l_data=[5, 6, 3, 1, 2, 7]
selection_sort(l_data)

print("-------------------Selection Sort---------------------------")
def selection_sort(list):

#--Arranging data in sequence
    for i in range(0,len(list)):
        small=list[i] #--considering ith value to be the smallest
        pos=i

        for y in range(i+1,len(list)):
            if small>list[y]: #--If a value smaller than small is found
                pos=y #--Position is stored
                small=list[y] #--Small is updated

        temp=list[i]
        list[i]=list[pos]
        list[pos]=temp
        print(list)

    return list

l_data=[5, 6, 3, 1, 2, 7]
selection_sort(l_data)

print("--------------------------Insertion Sort-------------------------")
def insertion_sort(list):
    #--Sorts a sequence in ascending order using insertion sort technique
    for i in range(1,len(list)):
        #--Save the value to be positioned
        val=list[i]
        #--Find position where value fits the ordered part of the list
        pos=i
        #--Shift items to the right during the search
        while pos>0 and val<list[pos-1]:
            list[pos]=list[pos-1]
            pos-=1
        #--Put saved value in open slot
        list[pos]=val
        print(list)
    return list

l_data=[5, 6, 3, 1, 2, 7]
insertion_sort(l_data)