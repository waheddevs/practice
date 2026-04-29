''' Packages & Debugging
(1) Python Packages & Core package
(2) Package MAnager & External package
(3) DEbugging
'''

from PIL import Image
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


print('===== Package MAnager & External package =====')
''' Package Manager > pip
    Python > pip pipenv
    NodeJS > npm yarn
    PHP > Composer
    MacOS > brew
'''
# External Package > https://pypi.org/

with Image.open('material\photo_2026-01-25_18-19-04.jpg') as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save('material\sample.png')
