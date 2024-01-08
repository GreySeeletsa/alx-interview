#!/usr/bin/python3


def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened.

    Num of boxes is n.
    """
    visited = {0}
    queue = [boxes[0]]
    while queue:
        box = queue.pop(0)
        for key in box:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(boxes[key])
    return len(visited) == len(boxes)
