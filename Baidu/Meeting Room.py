# //Give a list of meeting times, find minimum of rooms it need to take
# // 1000-1100, 1000-1200 => 2 rooms
# // 300-400, 200-300 => 1 room
# // 200-400, 100-300 => 2 rooms
# // 300-400, 300-400, 200-300 => 2 rooms
# // 500-700, 200-300, 400-600 => 2 rooms
# // 300-400, 200-400, 300-500 => 3 rooms

# // 2200-400, 2100-2300 => 2 rooms

import heapq


def meetingRoom(times):
    if not times or len(times) == 0:
        return 0
    times.sort(key=lambda x: x[0])
    intervals = []
    heapq.heapify(intervals)
    heapq.heappush(intervals, (times[0][1], times[0]))
    for i in range(1, len(times)):
        temp = heapq.heappop(intervals)[1]
        if times[i][0] >= temp[1]:
            temp[1] = times[i][1]
        else:
            heapq.heappush(intervals, (times[i][1], times[i]))
        heapq.heappush(intervals, (temp[1], temp))
    return len(intervals)

arr1 = [[300, 400], [200, 400], [300, 500]]
arr2 = [[1, 10], [2, 4], [6, 7]]
arr3 = [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]
arr4 = [[1, 5], [8, 9], [8, 9], [8, 9]]

print meetingRoom(arr2)
# https://leetcode.com/problems/meeting-rooms-ii/?tab=Description
# if times[x - 1][0] > times[x - 1][1] and times[x][0] > times[x][1]:
#     room += 1
#     end = max(end, times[x][1])
#     continue
