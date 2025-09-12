# Stack Implementation in python

class Stack:
    def __init__(self, max_stack):
        self.__max_stack = max_stack
        self.__elements = [None] * max_stack
        self.__top = -1

    def get_max_stack(self):
        return self.__max_stack
    
    def is_full(self):
        return self.__top == (self.__max_stack -1)
    
    def is_empty(self):
        return self.__top == -1
    
    def push(self, data):
        if self.is_full():
            print("O V E R F L O W ! ! !")
        else:
            self.__top += 1
            self.__elements[self.__top] = data
            print(f"{data} has been PUSHED at index {self.__top}")

    def pop(self):
        if self.is_empty():
            print("U N D E R F L O W ! ! !")
        else:
            data = self.__elements[self.__top]
            print(f"{data} has been POPPED from index {self.__top}")
            self.__top -= 1
            return data
        
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            index = self.__top
            while(index >= 0):
                print(self.__elements[index], end = " ")
                index -= 1
            print()

n = int(input("Please enter the stack size:"))
stk = Stack(n)
stk.display()
stk.push(22)
stk.push(33)
stk.push(11)
stk.push(13)
stk.push(54)
stk.display()
print(stk.pop())
print(stk.pop())
print(stk.pop())
stk.display()