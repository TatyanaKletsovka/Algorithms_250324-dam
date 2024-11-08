def is_balanced(brackets):
    stack = []

    for bracket in brackets:
        if bracket == '(':  # если открывающая скобка
            stack.append(bracket)
        elif bracket == ')':  # если закрывающая скобка
            if not stack:  # если стек пуст, значит, лишняя закрывающая скобка
                return False
            stack.pop()  # удаляем соответствующую открывающую скобку

    # Если стек пустой, то все открывающие скобки были закрыты корректно
    return len(stack) == 0

# Примеры использования
print(is_balanced("(()()()())"))    # True
print(is_balanced("(((())))"))      # True
print(is_balanced("(()((())()))"))  # True
print(is_balanced("((((((())"))     # False
print(is_balanced("())"))           # False
print(is_balanced("(()()(()"))      # False
print(is_balanced("(())"))      # False
