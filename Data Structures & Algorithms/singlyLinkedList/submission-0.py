class Listnode:
    def __init__(self,data,nextnode = None):
        self.data = data
        self.next = nextnode
        
class LinkedList:
    
    def __init__(self):
        self.head = Listnode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        pos = 0
        while(curr):
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Listnode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Listnode(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i<index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while(curr):
            res.append(curr.data)
            curr = curr.next
        return res

        
