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
    
    for idx, currEl in enumerate(meetings):
        lastEl = result[len(result) - 1]
        if currEl[0] <= lastEl[1]:
            start = lastEl[0]
            end = lastEl[1]
            if currEl[1] > lastEl[1]:
                end = currEl[1]
            result[len(result) - 1] = (start, end)
        else: 
            result.append(currEl)
    
    return result

    


input = [(0, 1), (3, 5), (4, 8), (10, 12), (10, 12), (9, 10), (17, 46)]
print(merge_ranges(input) == [(0, 1), (3, 8), (9, 12), (17, 46)])
print(merge_ranges([(1, 2), (2, 3)]) == [(1, 3)])
print(merge_ranges([(2, 3), (1, 5)]) == merge_ranges([(1, 5), (2, 3)]) == [(1, 5)])
print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)])
print(merge_ranges([(1, 3), (2, 4)]) == [(1, 4)])