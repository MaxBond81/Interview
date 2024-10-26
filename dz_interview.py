

class Stack:
    def __init__(self):
        self.list_stack = []

    def is_empty(self):
        return True if len(self.list_stack) == 0 else False

    def push(self, item):
        self.list_stack.append(item)

    def pop_(self):
        return self.list_stack.pop()

    def peek(self):
        return self.list_stack[-1]

    def size_(self):
        return len(self.list_stack)


def stack_balance(sequence):
    STAPLES_DICT = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack_balance = Stack()
    balanced = True
    index = 0
    while index < len(sequence) and balanced:
        symbol = sequence[index]
        if symbol in STAPLES_DICT:
            stack_balance.push(symbol)
        else:
            if stack_balance.is_empty():
                balanced = False
            else:
                if symbol == STAPLES_DICT.get(stack_balance.peek()):
                    stack_balance.pop_()
                else:
                    balanced = False
        index = index + 1
    if balanced and stack_balance.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

if __name__ == '__main__':
    print(stack_balance("(([)])"))




