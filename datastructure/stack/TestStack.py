from StackByArray import Stack
# from StackByLinkedList import Stack


stack = Stack(5)
# stack = Stack()

stack.push(1)
stack.push(3)
stack.push(5)
stack.push(9)
stack.push(10)

stack.show()

print(stack.pop())
print(stack.pop())

print(stack.peek())
print(stack.peek())

stack.show()
