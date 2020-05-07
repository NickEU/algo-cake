#In order to win the prize for most cookies sold,
# my friend Alice and I are going to merge 
#our Girl Scout Cookies orders and enter as one unit.

#Each order is represented by an “order id” (an integer).

#We have our lists of orders sorted numerically already,
#in lists. Write a function to merge our lists of orders into one sorted list.

def merge_lists(list1, list2):
    result = []
    l1Idx = l2Idx = 0
    while True:
        if l1Idx == len(list1):
            result += list2[l2Idx:]
            break
        
        if l2Idx == len(list2):
            result += list1[l1Idx:]
            break

        if list1[l1Idx] < list2[l2Idx]:
            result.append(list1[l1Idx])
            l1Idx += 1
        else:
            result.append(list2[l2Idx])
            l2Idx += 1
    
    return result



my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, alices_list) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19])
print(merge_lists([1, 2], []) == [1, 2])
print(merge_lists([], [1, 2, 3]) == [1, 2, 3])
print(merge_lists([1, 5, 8, 12], [3, 4, 6]) == [1, 3, 4, 5, 6, 8, 12])
print(merge_lists([], []) == [])