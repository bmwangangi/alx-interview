#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]
    
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)
    
    return all(visited)

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False
