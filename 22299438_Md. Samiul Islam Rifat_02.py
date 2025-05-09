# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random
# import time
#
#
# W_Width,W_Height = 800,600
# diamond_size = 15
# catcher_width, catcher_height = 80,10
# button_size = 20
# init_fall_speed = 1.75
# speed_increase = 1.05
# point_size = 2
#
#
# class GameState:
#     def __init__(self):
#         self.reset()
#         self.key_states = {'left': False, 'right': False}
#
#     def reset(self):
#         self.score = 0
#         self.game_over = False
#         self.paused = False
#         self.fall_speed = init_fall_speed
#         self.diamond_pos = [0, 0]
#         self.diamond_color = [1, 1, 1]
#         self.catcher_pos = W_Width // 2
#         self.last_time = time.time()
#         self.mouse_x = 0
#         self.mouse_y = 0
#         self.mouse_clicked = False
#         self.generate_new_diamond()
#
#     def generate_new_diamond(self):
#         self.diamond_pos[0] = random.randint(diamond_size, W_Width - diamond_size)
#         self.diamond_pos[1] = W_Height - diamond_size
#         self.diamond_color = [random.random(), random.random(), random.random()]
#         # bright color
#         for i in range(3):
#             if self.diamond_color[i] < 0.5:
#                 self.diamond_color[i] += 0.5
#
#
# game_state = GameState()
#
# def draw_pixel(x, y):
#     glBegin(GL_POINTS)
#     glVertex2f(x, y)
#     glEnd()
#
# # midpoint line algorithm
# def draw_line(x1, y1, x2, y2):
#     x1, y1, x2, y2 = int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2))
#
#     zone = find_zone(x1, y1, x2, y2)
#     x1_z0, y1_z0 = convert_to_zone0(x1, y1, zone)
#     x2_z0, y2_z0 = convert_to_zone0(x2, y2, zone)
#
#     dx = x2_z0 - x1_z0
#     dy = y2_z0 - y1_z0
#
#     # vertical lines
#     if dx == 0:
#         if y2_z0 > y1_z0:
#             step = 1
#         else:
#             step = -1
#
#         for y in range(y1_z0, y2_z0 + step, step):
#             px, py = convert_from_zone0(x1_z0, y, zone)
#             draw_pixel(px, py)
#         return
#
#     d = 2 * dy - dx
#     dE = 2 * dy
#     dNE = 2 * (dy - dx)
#     y = y1_z0
#
#     if x2_z0 > x1_z0:
#         step = 1
#     else:
#         step = -1
#     for x in range(x1_z0, x2_z0 + step, step):
#         px, py = convert_from_zone0(x, y, zone)
#         draw_pixel(px, py)
#         if d > 0:
#             d += dNE
#             y += 1
#         else:
#             d += dE
#
#
# def find_zone(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#
#     if abs(dx) >= abs(dy):
#         if dx >= 0 and dy >= 0:
#             return 0
#         elif dx <= 0 and dy >= 0:
#             return 3
#         elif dx <= 0 and dy <= 0:
#             return 4
#         else:
#             return 7
#     else:
#         if dx >= 0 and dy >= 0:
#             return 1
#         elif dx <= 0 and dy >= 0:
#             return 2
#         elif dx <= 0 and dy <= 0:
#             return 5
#         else:
#             return 6
#
#
# def convert_to_zone0(x, y, zone):
#     if zone == 0:
#         return x, y
#     elif zone == 1:
#         return y, x
#     elif zone == 2:
#         return y, -x
#     elif zone == 3:
#         return -x, y
#     elif zone == 4:
#         return -x, -y
#     elif zone == 5:
#         return -y, -x
#     elif zone == 6:
#         return -y, x
#     elif zone == 7:
#         return x, -y
#
#
# def convert_from_zone0(x, y, zone):
#     if zone == 0:
#         return x, y
#     elif zone == 1:
#         return y, x
#     elif zone == 2:
#         return -y, x
#     elif zone == 3:
#         return -x, y
#     elif zone == 4:
#         return -x, -y
#     elif zone == 5:
#         return -y, -x
#     elif zone == 6:
#         return y, -x
#     elif zone == 7:
#         return x, -y
#
#
# def draw_diamond(x, y, size, color):
#     glColor3f(*color)
#     draw_line(x, y - size, x + size, y)
#     draw_line(x + size, y, x, y + size)
#     draw_line(x, y + size, x - size, y)
#     draw_line(x - size, y, x, y - size)
#
#
# def draw_catcher(x, width, height, game_over=False):
#     if game_over:
#         color = [1, 0, 0]
#     else:
#         color = [1, 1, 1]
#     glColor3f(*color)
#     draw_line(x - width // 2, height, x + width // 2, height)
#     draw_line(x - width // 2, height, x - width // 2 + 10, 0)
#     draw_line(x + width // 2, height, x + width // 2 - 10, 0)
#     draw_line(x - width // 2 + 10, 0, x + width // 2 - 10, 0)
#
#
# def draw_button(x, y, size, shape, color):
#     glColor3f(*color)
#     if shape == "left_arrow":
#         draw_line(x + size/0.5, y, x, y)
#         draw_line(x, y, x + size, y - size)
#         draw_line(x, y, x + size, y + size)
#     if shape == "play_pause":
#         if game_state.paused:
#             draw_line(x, y - size, x, y + size)
#             draw_line(x, y + size, x + size, y)
#             draw_line(x + size, y, x, y - size)
#         else:
#             draw_line(x, y - size, x, y + size)
#             draw_line(x + size, y - size, x + size, y + size)
#     if shape == "cross":
#         draw_line(x - size, y - size, x + size, y + size)
#         draw_line(x - size, y + size, x + size, y - size)
#
#
# def check_collision(diamond_pos, catcher_pos):
#     #diamond bounding box
#     diamond_left = diamond_pos[0] - diamond_size
#     diamond_right = diamond_pos[0] + diamond_size
#     diamond_top = diamond_pos[1] + diamond_size
#     diamond_bottom = diamond_pos[1] - diamond_size
#
#     #catcher bounding box
#     catcher_left = catcher_pos - catcher_width // 2
#     catcher_right = catcher_pos + catcher_width // 2
#     catcher_top = catcher_height
#     catcher_bottom = 0
#
#     return (diamond_left < catcher_right and
#             diamond_right > catcher_left and
#             diamond_bottom < catcher_top and
#             diamond_top > catcher_bottom)
#
#
# def update_game(value):
#     current_time = time.time()
#     delta_time = current_time - game_state.last_time
#     game_state.last_time = current_time
#
#     if not game_state.paused and not game_state.game_over:
#         #movement keys
#         move_left = game_state.key_states['left']
#         move_right = game_state.key_states['right']
#
#         if move_left:
#             game_state.catcher_pos = max(catcher_width // 2, game_state.catcher_pos - 300 * delta_time)
#         if move_right:
#             game_state.catcher_pos = min(W_Width - catcher_width // 2, game_state.catcher_pos + 300 * delta_time)
#
#         # move diamond
#         game_state.diamond_pos[1] -= game_state.fall_speed * 60 * delta_time
#
#         # Check collision
#         if check_collision(game_state.diamond_pos, game_state.catcher_pos):
#             game_state.score += 1
#             game_state.fall_speed *= speed_increase
#             print(f"Score: {game_state.score}")
#             game_state.generate_new_diamond()
#         elif game_state.diamond_pos[1] < 0:
#             game_state.game_over = True
#             print(f"Game Over! Final Score: {game_state.score}")
#
#     #button clicks
#     if game_state.mouse_clicked:
#         left_button_x, play_button_x, cross_button_x = 50, W_Width // 2, W_Width - 50
#         buttons_y = W_Height - 50
#
#         if (left_button_x - button_size <= game_state.mouse_x <= left_button_x + button_size and
#                 buttons_y - button_size <= game_state.mouse_y <= buttons_y + button_size):
#             game_state.reset()
#             print("Starting Over")
#         if (play_button_x - button_size <= game_state.mouse_x <= play_button_x + button_size and
#               buttons_y - button_size <= game_state.mouse_y <= buttons_y + button_size):
#             game_state.paused = not game_state.paused
#         if (cross_button_x - button_size <= game_state.mouse_x <= cross_button_x + button_size and
#               buttons_y - button_size <= game_state.mouse_y <= buttons_y + button_size):
#             print(f"Goodbye! Final Score: {game_state.score}")
#             glutLeaveMainLoop()
#
#         game_state.mouse_clicked = False
#
#     glutPostRedisplay()
#     glutTimerFunc(16, update_game, 0)
#
#
# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#
#     # draw diamond
#     if not game_state.game_over:
#         draw_diamond(*game_state.diamond_pos, diamond_size, game_state.diamond_color)
#
#     # draw catcher
#     draw_catcher(game_state.catcher_pos, catcher_width, catcher_height, game_state.game_over)
#
#     # draw buttons
#     draw_button(50, W_Height - 50, button_size, "left_arrow", [0, 1, 1])
#     draw_button(W_Width // 2, W_Height - 50, button_size, "play_pause", [1, 0.75, 0])
#     draw_button(W_Width - 50, W_Height - 50, button_size, "cross", [1, 0, 0])
#
#     glutSwapBuffers()
#
# def special_key(key, x, y):
#     if key == GLUT_KEY_LEFT:
#         game_state.key_states['left'] = True
#     elif key == GLUT_KEY_RIGHT:
#         game_state.key_states['right'] = True
#
#
# def special_key_up(key, x, y):
#     if key == GLUT_KEY_LEFT:
#         game_state.key_states['left'] = False
#     elif key == GLUT_KEY_RIGHT:
#         game_state.key_states['right'] = False
#
#
# def mouse(button, state, x, y):
#     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
#         game_state.mouse_x, game_state.mouse_y = x, W_Height - y
#         game_state.mouse_clicked = True
#
#
# glutInit()
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
# glutInitWindowSize(W_Width, W_Height)
# glutCreateWindow(b"Catch the Diamonds!")
# gluOrtho2D(0, W_Width, 0, W_Height)
#
#
# glutDisplayFunc(display)
# glutTimerFunc(0, update_game, 0)
# glutSpecialFunc(special_key)
# glutSpecialUpFunc(special_key_up)
# glutMouseFunc(mouse)
#
# glClearColor(0, 0, 0, 1)
# glPointSize(point_size)
#
# glutMainLoop()
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, radians
import random


player_pos = [0, 0]
player_angle = 0
bullets = []
enemies = []
cheat_mode = False
auto_vision = False
life = 10
score = 0
missed = 0
game_over = False
cheat_rotation_angle = 0
pulse_timer = 0

GRID_BOUND = 600
BULLET_SPEED = 10
ENEMY_SPEED = 0.1
max_miss = 10
ENEMY_COUNT = 5
fovY = 120
camera_pos = (0, 500, 500)


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def draw_player():
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], 0)
    if game_over:
        glRotatef(90, 1, 0, 0)
    else:
        glRotatef(player_angle, 0, 0, 1)
    # Legs
    glColor3f(0, 0, 1)
    for i in [-1, 1]:
        glPushMatrix()
        glTranslatef(i * 15, 0, 0)
        gluCylinder(gluNewQuadric(), 5, 8, 30, 10, 10)
        glPopMatrix()

    # Body
    glColor3f(0.2, 0.6, 0.2)
    glPushMatrix()
    glTranslatef(0, 0, 30)
    glScalef(30, 10, 30)
    glutSolidCube(1)
    glPopMatrix()

    # Arms
    glColor3f(1.0, 0.9, 0.89)
    for i in [-1, 1]:
        glPushMatrix()
        glTranslatef(i * 15, 0, 52)
        glRotatef(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 8, 4, 25, 10, 10)
        glPopMatrix()

    # Gun
    glColor3f(0.9, 0.9, 0.9)
    glPushMatrix()
    glTranslatef(0, 0, 50)
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 10, 5, 30, 10, 10)
    glPopMatrix()

    # Head
    glColor3f(0, 0, 0)
    glPushMatrix()
    glTranslatef(0, 0, 60)
    gluSphere(gluNewQuadric(), 10, 10, 10)
    glPopMatrix()

    glPopMatrix()

def draw_bullets():
    global bullets, missed
    remaining_bullets = []
    for bullet in bullets:
        bullet['x'] += BULLET_SPEED * cos(radians(bullet['angle']))
        bullet['y'] += BULLET_SPEED * sin(radians(bullet['angle']))

        if abs(bullet['x']) > GRID_BOUND or abs(bullet['y']) > GRID_BOUND:
            missed += 1
            continue

        glPushMatrix()
        glColor3f(1, 0, 0)
        glTranslatef(bullet['x'], bullet['y'], 5)
        glutSolidCube(15)
        glPopMatrix()
        remaining_bullets.append(bullet)
    bullets = remaining_bullets

def spawn_enemies():
    global enemies
    enemies = []
    for i in range(ENEMY_COUNT):
        x = random.randint(-GRID_BOUND, GRID_BOUND)
        y = random.randint(-GRID_BOUND, GRID_BOUND)
        enemies.append({'x': x, 'y': y})

def draw_enemies():
    global enemies, life
    updated_enemies = []
    for enemy in enemies:
        dx = player_pos[0] - enemy['x']
        dy = player_pos[1] - enemy['y']
        dist = (dx**2 + dy**2) ** 0.5
        if dist != 0:
            enemy['x'] += ENEMY_SPEED * dx / dist
            enemy['y'] += ENEMY_SPEED * dy / dist

        glPushMatrix()
        glColor3f(1, 0, 0)
        glTranslatef(enemy['x'], enemy['y'], 10)
        scale = 1 + 0.3 * sin(pulse_timer / 10.0)
        glScalef(scale, scale, scale)
        gluSphere(gluNewQuadric(), 20, 20, 20)
        glColor3f(0,0,0)
        glTranslatef(0, 0, 20)
        gluSphere(gluNewQuadric(), 10, 10, 10)
        glPopMatrix()

        if dist < 10:
            life -= 1
            continue

        updated_enemies.append(enemy)

    enemies[:] = updated_enemies
    while len(enemies) < ENEMY_COUNT:
        x = random.randint(-GRID_BOUND, GRID_BOUND)
        y = random.randint(-GRID_BOUND, GRID_BOUND)
        enemies.append({'x': x, 'y': y})

def check_line_of_sight(angle):
    ax = cos(radians(angle))
    ay = sin(radians(angle))
    for enemy in enemies:
        dx = enemy['x'] - player_pos[0]
        dy = enemy['y'] - player_pos[1]
        dot = dx * ax + dy * ay
        if dot < 0:
            continue
        cross = abs(dx * ay - dy * ax)
        if cross < 15 and (dx**2 + dy**2)**0.5 < 200:
            return True
    return False

def update_cheat_mode():
    global cheat_rotation_angle, bullets
    if cheat_mode:
        cheat_rotation_angle = (cheat_rotation_angle + 5) % 360
        if check_line_of_sight(cheat_rotation_angle):
            bullets.append({
                'x': player_pos[0] + 10 * cos(radians(cheat_rotation_angle)),
                'y': player_pos[1] + 10 * sin(radians(cheat_rotation_angle)),
                'angle': cheat_rotation_angle})

def draw_game_over():
    draw_text(30,770,f"Game is Over. Your Score is {score}.")
    draw_text(30,740,"Press \"R\" to RESTART the Game.")

def reset_game():
    global life, score, missed, game_over, bullets, enemies, player_pos, player_angle
    life = 5
    score = 0
    missed = 0
    game_over = False
    bullets = []
    player_pos = [0.0, 0.0]
    player_angle = 0
    spawn_enemies()

def keyboardListener(key, x, y):
    global player_pos, player_angle, cheat_mode, auto_vision, game_over
    if game_over:
        if key == b'r':
            reset_game()
        return
    if key == b'w':
        player_pos[0] += 5 * cos(radians(player_angle))
        player_pos[1] += 5 * sin(radians(player_angle))
    elif key == b's':
        player_pos[0] -= 5 * cos(radians(player_angle))
        player_pos[1] -= 5 * sin(radians(player_angle))
    elif key == b'a':
        player_angle = (player_angle + 5) % 360
    elif key == b'd':
        player_angle = (player_angle - 5) % 360
    elif key == b'c':
        cheat_mode = not cheat_mode
    elif key == b'v':
        auto_vision = not auto_vision


def specialKeyListener(key, x, y):
    global camera_pos
    cx, cy, cz = camera_pos
    if key == GLUT_KEY_UP:
        cz += 5
    elif key == GLUT_KEY_DOWN:
        cz -= 5
    elif key == GLUT_KEY_LEFT:
        cx -= 5
    elif key == GLUT_KEY_RIGHT:
        cx += 5
    camera_pos = (cx, cy, cz)


def mouseListener(button, state, x, y):

    global bullets, player_angle, auto_vision

    if game_over:
        return


    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and not cheat_mode:
        rad = radians(player_angle)
        bx = player_pos[0] + 30 * cos(rad)
        by = player_pos[1] + 30 * sin(rad)
        bullets.append({'x': bx, 'y': by, 'angle': player_angle})


    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        auto_vision = not auto_vision


def bullet_hit():
    global bullets, enemies, score
    new_bullets = []
    for b in bullets:
        hit = False
        for e in enemies:
            dx = b['x'] - e['x']
            dy = b['y'] - e['y']
            if dx**2 + dy**2 < 100:
                enemies.remove(e)
                score += 1
                hit = True
                break
        if not hit:
            new_bullets.append(b)
    bullets = new_bullets

def draw_userinfo():

    if not game_over:
        draw_text(10, 770, f"Player Life Remaining: {life}   ")
        draw_text(10, 750, f"Game Score: {score}")
        draw_text(10, 730, f"Player Bullet Missed: {missed}")

def draw_grid():
    size = 80
    for x in range(-GRID_BOUND, GRID_BOUND, size):
        for y in range(-GRID_BOUND, GRID_BOUND, size):
            glBegin(GL_QUADS)
            if ((x + y) // size) % 2 == 0:
                glColor3f(0.7, 0.5, 0.95)
            else:
                glColor3f(1.0, 1.0, 1.0)
            glVertex3f(x, y, 0)
            glVertex3f(x + size, y, 0)
            glVertex3f(x + size, y + size, 0)
            glVertex3f(x, y + size, 0)
            glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)  # Blue
    glVertex3f(-GRID_BOUND, -GRID_BOUND, 0)
    glVertex3f(-GRID_BOUND, GRID_BOUND, 0)
    glVertex3f(-GRID_BOUND, GRID_BOUND, 60)
    glVertex3f(-GRID_BOUND, -GRID_BOUND, 60)

    glColor3f(0, 0, 1)  # Green
    glVertex3f(GRID_BOUND, -GRID_BOUND, 0)
    glVertex3f(GRID_BOUND, GRID_BOUND, 0)
    glVertex3f(GRID_BOUND, GRID_BOUND, 60)
    glVertex3f(GRID_BOUND, -GRID_BOUND, 60)

    glColor3f(0.0, 1.0, 1.0)  # Cyan
    glVertex3f(-GRID_BOUND, -GRID_BOUND, 0)
    glVertex3f(GRID_BOUND, -GRID_BOUND, 0)
    glVertex3f(GRID_BOUND, -GRID_BOUND, 60)
    glVertex3f(-GRID_BOUND, -GRID_BOUND, 60)
    glEnd()


def setupCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 1500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    px, py = player_pos
    if auto_vision:
        rad = radians(player_angle)
        cx = px + 100 * cos(rad)
        cy = py + 100 * sin(rad)
        gluLookAt(px, py, 100, cx, cy, 70, 0, 0, 1)
    elif auto_vision and cheat_mode:
        cx = px - 200 * cos(radians(player_angle))
        cy = py - 200 * sin(radians(player_angle))
        gluLookAt(cx, cy, 100, px, py, 0, 0, 0, 1)
    else:
        x, y, z = camera_pos
        gluLookAt(x, y, z, 0, 0, 0, 0, 0, 1)


def showScreen():
    global game_over, missed, pulse_timer
    pulse_timer += 0.3
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 800)
    setupCamera()
    draw_grid()
    if not game_over:
        update_cheat_mode()
        draw_bullets()
        draw_enemies()
    draw_player()

    if not game_over:
        bullet_hit()
        if life <= 0 or missed >= max_miss:
            game_over = True
    else:
        draw_game_over()

    if not game_over:
        draw_userinfo()

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Bullet Frenzy 3D")
    glEnable(GL_DEPTH_TEST)
    reset_game()
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutMouseFunc(mouseListener)
    glutSpecialFunc(specialKeyListener)
    glutMainLoop()

if __name__ == '__main__':
    main()
