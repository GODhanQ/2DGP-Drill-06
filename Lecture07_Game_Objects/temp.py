class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 600
        self.image = load_image('ball21x21.png')

        self.moving_vec = random.randint(3, 8) * -1
        self.moving_direction = -1
        self.gravity = 1

        self.floor_y = 60
        # self.ceiling_y = 600
        self.is_moving = True

    def update(self):
        if self.is_moving:
            self.moving_vec -= self.gravity

            self.y += self.moving_vec

            if self.y < self.floor_y:
                self.moving_vec *= -0.8
                self.y = self.floor_y
            if abs(self.moving_vec) < 1.0 and self.y == self.floor_y:
                self.is_moving = False
                self.moving_vec = 0
                self.y = self.floor_y

    def draw(self):
        self.image.draw(self.x, self.y)

class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 600
        self.image = load_image('ball41x41.png')

        self.moving_vec = random.randint(3, 8) * -1
        self.moving_direction = -1
        self.gravity = 1

        self.floor_y = 70
        # self.ceiling_y = 600
        self.is_moving = True

    def update(self):
        if self.is_moving:
            self.moving_vec -= self.gravity

            self.y += self.moving_vec

            if self.y < self.floor_y:
                self.moving_vec *= -0.8
                self.y = self.floor_y
            if abs(self.moving_vec) < 1.0 and self.y == self.floor_y:
                self.is_moving = False
                self.moving_vec = 0
                self.y = self.floor_y

    def draw(self):
        self.image.draw(self.x, self.y)