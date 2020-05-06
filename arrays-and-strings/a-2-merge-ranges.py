from copy import deepcopy
# O(n * log n)
# sort the input first
# then merge the meeting times in one pass
def merge_ranges(input):
    def sortFunc(el):
        return el[0]
    meetings = deepcopy(input)
    meetings.sort(key=sortFunc)
    result = [meetings[0]]
    
    for currStart, currEnd in meetings[1:]:
        lastEl = result[-1]
        if currStart <= lastEl[1]:
            result[-1] = (lastEl[0], max(currEnd, lastEl[1]))
        else: 
            result.append((currStart, currEnd))
    
    return result

    


input = [(0, 1), (3, 5), (4, 8), (10, 12), (10, 12), (9, 10), (17, 46)]
print(merge_ranges(input) == [(0, 1), (3, 8), (9, 12), (17, 46)])
print(merge_ranges([(1, 2), (2, 3)]) == [(1, 3)])
print(merge_ranges([(2, 3), (1, 5)]) == merge_ranges([(1, 5), (2, 3)]) == [(1, 5)])
print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)])
print(merge_ranges([(1, 3), (2, 4)]) == [(1, 4)])