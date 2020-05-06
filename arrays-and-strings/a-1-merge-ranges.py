# O (n ^ 2)
def mergeRanges(meetings):
    results = [meetings[0],]
    for meeting in meetings:
      flag = True
      for idx, result in enumerate(results):
          result = list(result)
          if (meeting[0] < result[0] and meeting[1] < result[1]
          and meeting[1] >= result[0]):
                results[idx] = (meeting[0], result[1])

          elif (meeting[0] > result[0] and meeting[1] > result[1]
          and meeting[0] <= result[1]):
                results[idx] = (result[0], meeting[1])

          elif (meeting[0] < result[0] and meeting[1] > result[1]):
                results[idx] = (meeting[0], meeting[1])

          if not ((meeting[0] < result[0] and meeting[1] < result[0]
          or meeting[0] > result[1] and meeting[1] > result[1])):
              flag = False

      if flag == True:
          results.append(meeting)      

    return results


input = [(0, 1), (3, 5), (4, 8), (10, 12), (10, 12), (9, 10), (17, 46)]
print(mergeRanges(input) == [(0, 1), (3, 8), (9, 12), (17, 46)])
print(mergeRanges([(1, 2), (2, 3)]) == [(1, 3)])
print(mergeRanges([(2, 3), (1, 5)]) == mergeRanges([(1, 5), (2, 3)]) == [(1, 5)])
print(mergeRanges([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)])
print(mergeRanges([(1, 3), (2, 4)]) == [(1, 4)])