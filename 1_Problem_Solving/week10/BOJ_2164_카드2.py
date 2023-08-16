from collections import deque

N = int(input())

card = deque()
for i in range(1, N+1):
    card.append(i)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
    # card.rotate(-1) -> 왼쪽으로 1만큼 회전

print(card[0])