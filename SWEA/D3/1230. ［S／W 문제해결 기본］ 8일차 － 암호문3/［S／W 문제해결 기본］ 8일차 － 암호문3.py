# 1230. 암호문3

"""
연결리스트

1. I(삽입) x, y, s : 앞에서부터 x번째 암호문 바로 다음에 y개의 암호문을 삽입한다. s는 덧붙일 암호문들이다.[ ex) I 3 2 123152 487651 ]
=> insert(si, x+i) for i in range(y)

2. D(삭제) x, y : 앞에서부터 x번째 암호문 바로 다음부터 y개의 암호문을 삭제한다.[ ex) D 4 4 ]
=> delete(x) for _ in range(y)

3. A(추가) y, s : 암호문 뭉치 맨 뒤에 y개의 암호문을 덧붙인다. s는 덧붙일 암호문들이다. [ ex) A 2 421257 796813 ]
=> append(si) for i in range(y) 
"""



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data, position):
        """새로운 노드를 삽입한다."""
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("범위를 벗어난 삽입입니다.")
                current = current.next
            new_node.next = current.next
            current.next = new_node
            
    def is_empty(self):
        """연결 리스트가 비어있는지 확인한다."""
        return self.head is None
    
    def append(self, data):
        """리스트의 마지막에 노드를 추가한다."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    def delete(self, position):
        """특정 위치의 노드를 삭제하고 값을 반환한다."""
        if self.is_empty():
            raise IndexError("리스트가 비어있습니다.")
        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None or current.next is None:
                    raise IndexError("범위를 벗어났습니다.")
                current = current.next
            deleted_node = current.next
            deleted_data = deleted_node.data
            current.next = deleted_node.next
        return deleted_data
    
    def get(self, position):
        """특정 위치의 값을 반환한다."""
        if self.is_empty():
            raise IndexError("리스트가 비어있습니다.")
        if position == 0:
            return self.head.data
        else:
            current = self.head
            for _ in range(position):
                if current is None or current.next is None:
                    raise IndexError("범위를 벗어났습니다.")
                current = current.next
            return current.data


T = 10
for tc in range(1, T+1):
    # 원본 암호문 뭉치 속 암호문의 개수 N ( 2000 ≤ N ≤ 4000 의 정수)
    N = int(input())
    
    # 원본 암호문 뭉치 리스트
    corpus = SinglyLinkedList()
    for s in input().split():
        corpus.append(s)
    
    # 명령어의 개수 ( 250 ≤ M ≤ 500 의 정수)
    M = int(input())
    
    # 명령어 리스트
    commands = input().split()
    
    # 명령어의 인덱스
    index = 0
    while index < len(commands):
        command = commands[index]
        
        if command == "I":  # 삽입
            # [ ex) I 3 2 123152 487651 ]
            index += 1
            x = int(commands[index])
            index += 1
            y = int(commands[index])
            index += 1
            for i in range(y):
                si = commands[index + i]
                corpus.insert(si, x + i)
            index += y
            
        elif command == "D":  # 삭제
            # [ ex) D 4 4 ]
            index += 1
            x = int(commands[index])
            index += 1
            y = int(commands[index])
            for _ in range(y):
                corpus.delete(x)
            index += 1
            
        else:  # 추가 (A)
            # [ ex) A 2 421257 796813 ]
            index += 1
            y = int(commands[index])
            index += 1
            for i in range(y):
                si = commands[index + i]
                corpus.append(si)
            index += y
    
    result = [''] * 10
    for x in range(10):
        result[x] = corpus.get(x)
        
    print(f"#{tc}", *result)