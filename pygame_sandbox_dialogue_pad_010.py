import pygame
import pygame_sandbox_text_010 as t

pygame.init()

print('pygame_sandbox_dialogue_pad.py open')
green, black,blue,white = (0,255,0),(0,0,0),(0,0,255),(255,255,255)




def nip_front_line_from(whole_string, goal_wrap):
    wrap = goal_wrap
    print("wrap = " + str(wrap))
    if(wrap >= len(whole_string)):
        print("wrap longer than whole_string")
        wrap = len(whole_string) - 1
        nipped_string = whole_string
        nipped_line = ''
    else:
        while(whole_string[wrap].isspace() != True):
            wrap -= 1   
    
        nipped_string = whole_string[:wrap]
        nipped_line = whole_string[wrap+1:]
    return nipped_string, nipped_line


def wrap_string(raw_str, max_wrap):
    print("original format: " + raw_str)
    new_text = []
    current_raw = raw_str
    while (len(current_raw) >= 1):
        next_line, new_raw = nip_front_line_from(current_raw, max_wrap)
        new_text.append(next_line)
        current_raw = new_raw
    return new_text


def read_list(list_in_question):
    for item in list_in_question:
        print(item)





class T_Frame(pygame.sprite.Sprite):
    def __init__(self, Color, X, Y, Pos_X, Pos_Y, Border):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([X, Y])
        self.image.fill(Color)
        self.x = Pos_X
        self.y = Pos_Y
        self.rect = self.image.get_rect(center = (Pos_X + X//2, Pos_Y + Y//2))

    def confirm(self):
        print('T_Frame instantiated')


class I_Frame(T_Frame):
    def __init__(self, Color, X, Y, Pos_X, Pos_Y, Border):
        T_Frame.__init__(self, Color, X, Y, Pos_X, Pos_Y, Border)
        self.rect = self.image.get_rect(center = (Pos_X + X//2 + Border//2, Pos_Y + Y//2 + Border//2))

    def confirm(self):
        print('I_Frame instantiated')


class P_Frame(T_Frame):
    def __init__(self, Color, X, Y, Pos_X, Pos_Y, Border):
        T_Frame.__init__(self, Color, X, Y, Pos_X, Pos_Y, Border)
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def confirm(self):
        print('P_Frame instantiated')


class D_Text(pygame.sprite.Sprite):
    def __init__(self, X, Y, Pos_X, Pos_Y, Font_Size, Text, Border, Y_offset):
        pygame.sprite.Sprite.__init__(self)
        self.full_text = Text
        font_start = 'broadway'
        font_name = pygame.font.match_font(font_start)
        self.font = pygame.font.Font(font_name, Font_Size)
        self.image = self.font.render(self.full_text, True, white)
        self.rect = self.image.get_rect(topleft = (Pos_X + Border, Pos_Y + Y_offset))
        print(len(self.full_text))






def new_create_D_text(dialogue, wrap, X, Y, Pos_X, Pos_Y, Font_Size, Border, Y_offset):
    line_hght = Font_Size
    d_lines = wrap_string(dialogue, wrap)
    dialogue_holder = []
    for i in range(len(d_lines)):
        line_y = Pos_Y + (i * line_hght)
        d_l = D_Text(X, Y, Pos_X, line_y, Font_Size, d_lines[i], Border, Y_offset)
        dialogue_holder.append(d_l)
    return dialogue_holder


def load_sprite_images(image_list, width, height):
    #print('load_sprite_images')
    interim_list = []
    for item in image_list:
        image = pygame.image.load(item)
        big_image = pygame.transform.scale(image, (width, height))
        interim_list.append(big_image)
    #print('sprites loaded')
    return interim_list

class D_Portrait(pygame.sprite.Sprite):
    def __init__(self, Img_L, X, Y, Pos_X, Pos_Y,FPS):
        pygame.sprite.Sprite.__init__(self)
        #pre_image = pygame.image.load(Img)
        self.animation_list = load_sprite_images(Img_L, X, Y)
        #self.image = pygame.transform.scale(pre_image, (X, Y))
        self.index = 0
        self.image = self.animation_list[self.index]
        self.fps = FPS
        self.x = Pos_X
        self.y = Pos_Y
        self.rect = self.image.get_rect(center = (self.x, self.y))
        
    def confirm(self):
        print('D_Portrait instantiated')

    def update(self):
        self.image = self.animation_list[self.index//self.fps]
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.index += 1
        if self.index >= len(self.animation_list)*self.fps:
            self.index = 0

        

def make_text_frame_g(dialogue, wrap, m_x, m_y, m_pos_x, m_pos_y,FPS): #(Main_F, Sec_F, Portrait, Text)
    print('begin-make_text_frame_g()')
    border = 15
    temp_border = T_Frame(blue, m_x + border, m_y + border, m_pos_x, m_pos_y,border)
    temp_border.confirm()
    temp_inner = I_Frame(green, m_x, m_y, m_pos_x , m_pos_y, border)
    temp_inner.confirm()
    temp_portrait_f = P_Frame(blue, 50, 50, m_pos_x, m_pos_y, border)
    temp_portrait_f.confirm()
    temp_speaker = D_Portrait(['seahorse_001_0.png','seahorse_001_1.png'],50, 50, m_pos_x, m_pos_y,FPS)
    temp_speaker.confirm()

    text_used = dialogue

    #new_create_D_text(dialogue, wrap, X, Y, Pos_X, Pos_Y, Font_Size, Border, Y_offset)    
    text_obj_list = new_create_D_text(text_used,wrap,m_x, m_y, m_pos_x, m_pos_y, 14, border, m_y//2)
    
    holder_frame_g = pygame.sprite.Group([temp_border, temp_inner, temp_portrait_f,temp_speaker])
    holder_frame_g.add(text_obj_list)
    print('end-make_text_frame_g()')
    return holder_frame_g



#make_text_frame_g(50,100,50,150,20)





