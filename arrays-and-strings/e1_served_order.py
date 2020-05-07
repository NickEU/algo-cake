#I have two registers: one for take-out orders,
#and the other for the other folks eating inside the cafe.
#All the customer orders get combined into one list for the kitchen,
#where they should be handled first-come, first-served.

#INPUT:
#The take-out orders as they were entered into the system
#and given to the kitchen. (takeOutOrders)

#The dine-in orders as they were entered into the system
#and given to the kitchen. (dineInOrders)

#Each customer order (from either register) 
#as it was finished by the kitchen. (servedOrders)

#Given all three lists, write a function
#to check that my service is first-come, first-served.
#All food should come out in the same order customers requested it.

def check_service(takeOutOrders, dineInOrders, servedOrders):
    takeOutIdx = dineInIdx = 0
    for order in servedOrders:
        if takeOutIdx < len(takeOutOrders) and order == takeOutOrders[takeOutIdx]:
            takeOutIdx += 1
        elif dineInIdx < len(dineInOrders) and order == dineInOrders[dineInIdx]:
            dineInIdx += 1
        else:
            return False
    return True



print(check_service([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3]) == False)
print(check_service([1, 3, 5], [2, 4, 6, 9], [1, 2, 3, 5, 4, 6, 9]) == True)
print(check_service([1, 3, 5, 7, 11], [2, 4, 6, 9], [1, 2, 3, 5, 4, 6, 9, 7, 11]) == True)
print(check_service([1, 3, 5, 7, 11], [], [1, 3, 5, 7, 11]) == True)
print(check_service([], [2, 4, 6], [2, 6, 4]) == False)
print(check_service([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4, 6]) == True)