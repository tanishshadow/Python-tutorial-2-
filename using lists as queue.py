from collections import deque
# deque is fast as comparing to regular inserts in python


queue = deque(["tom","tanish","john","python"])
print(queue)

queue.append("c++")
popped = queue.popleft()
print(popped)

