from collections import deque

my_deque = deque([1, 2, 3])
print(f"Initial deque: {my_deque}")

my_deque.append(4)
my_deque.appendleft(0)
print(f"After adding elements: {my_deque}")

right_element = my_deque.pop()
left_element = my_deque.popleft()
print(f"Removed right element: {right_element}")
print(f"Removed left element: {left_element}")
print(f"Deque after removals: {my_deque}")

my_deque.rotate(1)
print(f"Deque after rotation: {my_deque}")
