# LIFO : Last In First Out : Stack
## Example : web browser (back button)

browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

last = browsing_session.pop()
print(last)

print(browsing_session)

if not browsing_session:
    print('Error.')

# FIFI : First in First Out : Queue

from collections import deque

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
print(queue)
