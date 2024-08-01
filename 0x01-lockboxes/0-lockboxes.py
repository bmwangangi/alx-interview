#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not
    Args:
        boxes (list): List of lists containing the keys in each box
    Returns:
        bool: True if all boxes can be opened, False otherwise
    '''
    if not boxes:
        return False
    
    length = len(boxes)
    opened_boxes = set([0])  # Start with the first box already opened
    keys = list(boxes[0])  # Initialize with keys from the first box
    
    while keys:
        key = keys.pop()
        if key < length and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])
    
    return len(opened_boxes) == length

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False
