def solution(node):
    while node:
        print(node.value, end="\n")
        node = node.next_item
    return node
