class CQueue:

    def __init__(self):
        self.arr1=[]
        self.arr2=[]


    def appendTail(self, value: int) -> None:
        self.arr2.append(value)

    def deleteHead(self) -> int:
        if not self.arr1:
            self.arr1.extend(self.arr2[::-1])
            self.arr2=[]
        return self.arr1.pop() if self.arr1 else -1