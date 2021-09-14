import math
import random
import time
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.speed = 4
        self.center_x = random.randint(0 , w)
        self.center_y = h
        self.angle = 180
        self.width = 80
        self.height = 80

    def move(self):
        self.center_x -= self.speed * math.sin(self.angle)
        self.center_y += self.speed * math.cos(self.angle)
    
class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png") 
        self.speed = 4
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y
    
    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

class SpaceCraft(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.width = 48
        self.height = 48
        self.center_x = w // 2
        self.center_y =48
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = [] 
        self.speed = 4

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))

# class FlyingSprite(arcade.Sprite):

#     def update(self):
#         super().update()

#         if self.up < 0:
#             self.remove_from_sprite_lists()



        
class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        super().__init__(width=self.w,height=self.h,title="silver SpaceCraft YASAMIN")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image=arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        self.me = SpaceCraft(self.w, self.h)
        self.enemy_list =[]
        self.cloud_list=[]
        #self.start_time = time.time()
    def add_enemy(self, delta_time: float):    

        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png")
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)


    def add_cloud(self, delta_time: float):
   
        self.cloud = ("OIP.jpg" )
        self.width = 48
        self.height = 48
        self.center_x =random.randint(self.width,self.width + 30)
        self.center_y =random.randint(10, 10)

        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,self.w,self.h, self.background_image)
        self.me.draw()

        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()
            
        for i in range(len(self.cloud_list)):
            self.cloud_list[i].draw()
    
    def on_update(self, delta_time):

        #self.end_time = time.time()
        # r = random.randrange( 0, 20, 2)
        # if self.end_time - self.start_time > r :

        self.enemy_list.append(Enemy(self.w , self.h))
        #     self.start_time = time.time()
        arcade.schedule(self.add_enemy,4)
        arcade.schedule(self.add_cloud, 1.5)
        self.me.rotate()
    
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()

        for i in range(len(self.cloud_list)):
            self.cloud_list[i].move()

        for b in self.enemy_list:
            for e in self.me.bullet_list:
                if arcade.check_for_collision(b,e):
                    self.enemy_list.remove(b)
                    self.me.bullet_list.remove(e)

    def on_key_press(self, key, modifires):
        if key ==arcade.key.RIGHT:
            self.me.change_angle = -1
        elif key == arcade.key.LEFT:
            self.me.change_angle = 1
        elif key == arcade.key.SPACE:
            self.me.fire()
        


    def on_key_release(self, key, modifiers):
       self.me.change_angle = 0


game=Game()

arcade.run()
