"""
Max este o pisica mare care doarme toata ziua
Max -> obiectul
clasa -> pisica
proprietatea -> marimea
atributul -> doarme
"""

# class Pisica:
#     pass
#
# primul_obiect = Pisica()
# Tom = Pisica()

def push(val):
    stack.append(val)

def pop():
    value = stack[-1]
    del stack[-1]
    return value

push(3)
push(2)
push(1)