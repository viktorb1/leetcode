# 1897 · Meeting Room III
### Algorithms | Medium | Accepted Rate: 27%

You have a list intervals of current meetings, and some meeting rooms with start and end timestamp.When a stream of new meeting ask coming in, judge one by one whether they can be placed in the current meeting list without overlapping..A meeting room can only hold one meeting at a time. Each inquiry is independent.

The meeting asked can be splited to some times. For example, if you want to ask a meeting for [2, 4], you can split it to [2,3] and [3, 4].

Ensure that Intervals can be arranged in rooms meeting rooms
Ensure that the end time of any meeting is not greater than 50000
|Intervals|<=50000
|ask|<=50000
rooms<=20

#### Example 1:
Input:
Intervals:[[1,2],[4,5],[8,10]], rooms = 1, ask: [[2,3],[3,4]]
Output: 
[true,true]
Explanation:
For the ask of [2,3], we can arrange a meeting room room0.
The following is the meeting list of room0:
[[1,2], [2,3], [4,5], [8,10]]
For the ask of [3,4], we can arrange a meeting room room0.
The following is the meeting list of room0:
[[1,2], [3,4], [4,5], [8,10]]

#### Example 2:
Input:
[[1,2],[4,5],[8,10]]
1
[[4,5],[5,6]]
Output:
[false,true]