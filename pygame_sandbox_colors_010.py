welcome_msg = 'pygame_sandbox_colors_000.py open!'
buffer = '\n*************\n'
print(buffer + welcome_msg + buffer)


color_file = 'sandbox_color_file_000.txt'
color_object_list = []

class Color(object):
    def __init__(self, space_separated_color_string):
        #first string is color name, last 3 strings are tuple
        color_components = space_separated_color_string.split()
        self.name = color_components[0]
        a = int(color_components[1])
        b = int(color_components[2])
        c = int(color_components[3])
        print(a,b,c)
        self.tuple = (a,b,c)
        print(self.name + ' initialized.\n')   


#blue = Color('blue 0 255 255')
#print(blue.name + '\n' + str(blue.tuple))

def grab_color(name_str):
    print('grab_color(): ' + name_str)
    for color in color_object_list:
        if color.name.lower() == name_str.lower():
            return color
    print('color not found')
    

def initialize_colors():
    global color_object_list
    temp_color_list = []
    with open (color_file, 'r') as file:
        raw_color_strings = file.readlines()

    for raw_color in raw_color_strings:
        print(raw_color)
        temp_color = Color(raw_color)
        temp_color_list.append(temp_color)

    color_object_list = temp_color_list
    print('raw_color_strings: ' + str(len(raw_color_strings)))
    print('temp_color_list: ' + str(len(temp_color_list)))
    print('color_object_list: ' + str(len(color_object_list)))


initialize_colors()

