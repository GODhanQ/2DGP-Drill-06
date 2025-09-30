from pico2d import *
import random

# Game object class here

# 1. 객체를 도출 - 추상화
# 2. 속성을 도출 - 추상화
# 3. 행위를 도출
# 4. 클래스를 제작
# 5. 객체를 생성

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(200, 600), 90
        self.frame = random.randint(0, 7)
        self.moving_vec = random.randint(3, 3)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.moving_vec
        if self.x > 800:
            self.x = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 100
        self.frame = random.randint(0, 7)
        self.moving_vec = random.randint(3, 3)
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += self.moving_vec
        if self.x > 800:
            self.x = 0

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0,
                             frame_width, frame_height,
                             self.x, self.y,
                             frame_width // 5, frame_height // 5)

class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(300, 600)
        self.image = load_image('ball21x21.png')
        self.floor = 60
        self.moving_vec = random.randint(3, 8) * -1
        self.is_moving = True
        self.gravity = 1

    def update(self):
        if self.is_moving:
            self.moving_vec -= self.gravity
            self.y += self.moving_vec
            if self.y < self.floor:
                self.y = self.floor
                self.moving_vec *= -0.5
            if abs(self.moving_vec) < 0.1 and self.y <= self.floor:
                self.is_moving = False
                self.moving_vec = 0
                self.y = self.floor

    def draw(self):
        self.image.draw(self.x, self.y)

class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(300, 600)
        self.image = load_image('ball41x41.png')
        self.floor = 70
        self.moving_vec = random.randint(3, 8) * -1
        self.is_moving = True
        self.gravity = 1

    def update(self):
        if self.is_moving:
            self.moving_vec -= self.gravity
            self.y += self.moving_vec
            if self.y < self.floor:
                self.y = self.floor
                self.moving_vec *= -0.8
            if abs(self.moving_vec) < 0.1 and self.y <= self.floor:
                self.is_moving = False
                self.moving_vec = 0
                self.y = self.floor

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

global team, zombies, small_balls
def reset_world():
    global running
    running = True

    global world # 모든 게임 객체의 리스트
    world = [] # 게임 월드 초기화

    # 객체들을 생성
    global grass, team, zombies, small_balls, big_balls
    grass = Grass()
    world.append(grass)

    team = [Boy() for _ in range(11)]
    world += team

    zombies = [Zombie() for _ in range(1)]
    world += zombies

    small_balls = [Small_Ball() for _ in range(10)]
    world += small_balls

    big_balls = [Big_Ball() for _ in range(10)]
    world += big_balls

reset_world()

def update_world():
    for game_object in world:
        game_object.update()

def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()

while running:
    handle_events()
    update_world() # 객체들의 상호작용들을 시뮬레이션 (계산)
    render_world() # 객체들의 모습을 화면에 그린다.

    delay(0.05)

close_canvas()
