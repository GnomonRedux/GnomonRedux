import pygame

welcome_msg = 'pygame_sandbox_lister_000.py open!'
buffer = '\n*************\n'
print(buffer + welcome_msg + buffer)


class Ball(pygame.sprite.Sprite):
    def __init__(self, Color, Size, Win_X, Win_Y):
        #super(Loading_Bar, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Size, Size])
        self.image.fill(Color)
        self.x = Win_X//2
        self.y = 0 + (Size//2) #note that 0 is the top of screen
        self.rect = self.image.get_rect( center= (self.x, self.y))

    def gravity(self):
        #print('gravity!')
        #uh oh! don't fall through the floor
        pass

    def bounce(self):
        #i'd implement this at app.check_collisions()
        pass

    def update(self):
        self.gravity()
        self.rect = self.image.get_rect( center= (self.x, self.y))


class Bat(Ball):
    def __init__(self, Color, Size, Win_X, Win_Y, Side):
        super(Bat, self).__init__(Color, Size, Win_X, Win_Y)
        if Side == 'Left':
            self.x = 0 + (Size//2)
        elif Side == 'Right':
            self.x = Win_X - Size
        self.y = Win_Y//2
        self.image = pygame.Surface([Size, Size*4])
        if Side == 'Bottom':
            self.image = pygame.Surface([Size*4, Size])
            self.x = Win_X//2
            self.y = Win_Y-(Size//2)
        self.image.fill(Color)
        

    def update(self):
        self.rect = self.image.get_rect( center= (self.x, self.y))





