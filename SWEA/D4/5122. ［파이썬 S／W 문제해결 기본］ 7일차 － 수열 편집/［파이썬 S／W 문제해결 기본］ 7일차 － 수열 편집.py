# 5122. 수열 편집

"""
연결 리스트

I 2 7 -> 2번 인덱스 앞에 7을 추가하고, 한 칸 씩 뒤로 이동한다.
=> insert(7, 2)

D 4 -> 4번 인덱스 자리를 지우고, 한 칸 씩 앞으로 이동한다.
=> delete(4)

C 3 8 -> 3번 인덱스 자리를 8로 바꾼다.
=> update(8, 3)
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
        
    def update(self, data, position):
        """특정 위치의 값을 변경한다."""
        if self.is_empty():
            raise IndexError("리스트가 비어있습니다.")
        
        if position == 0:
            self.head.data = data
        
        else:
            current = self.head
            for _ in range(position):
                if current is None or current.next is None:
                    raise IndexError("범위를 벗어났습니다.")
                current = current.next
            current.data = data
        
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


T = int(input())
for tc in range(1, T+1):
    # 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    N, M, L = map(int, input().split())
    arr = SinglyLinkedList()
    # 수열을 입력받아 연결리스트에 저장
    for number in input().split():
        arr.append(number)
    
    # 추가할 인덱스와 숫자 정보
    for _ in range(M):
        command = input().split()
        if command[0] == 'I':
            index, value = map(int, command[1:])
            arr.insert(value, index)
        elif command[0] == 'D':
            arr.delete(int(command[1]))
        else:  # command[0] == 'C':
            index, value = map(int, command[1:])
            arr.update(value, index)
            
    # 인덱스 L의 데이터 출력
    try:
        print(f'#{tc} {arr.get(L)}')
    except IndexError:
        print(f'#{tc} -1')
        