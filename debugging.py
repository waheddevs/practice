''' Packages & Debugging
(1) Python Packages & Core package
(2) Package MAnager & External package
(3) DEbugging
'''

import turtle
print('===== Python Packages & Core package =====')
''' Python Packages/Modules: Core, File and External '''
# Core packages > https://docs.python.org/3/library


# Core package
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(2)
# t.circle(150)
# turtle.done()


my_file = open('material/message.txt', 'r')
try:
    content = my_file.read()
    print('content:', content)
finally:
    my_file.close()

# with - Context Manager
with open('material/message.txt', 'r') as your_file:
    your_content = your_file.read()
    print('your_content:', your_content)

print('DONE')
