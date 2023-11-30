# Simple stack-based virtual machine
class SimpleVM:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

# Usage
vm = SimpleVM()
vm.push(5)
vm.push(10)
result = vm.pop()
print("Result from VM:", result)