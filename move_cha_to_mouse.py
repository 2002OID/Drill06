from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mx, my = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
running = True
arrow = 1
end_num = 1
xs = [x]
ys = [y]
line_frame = 0
temp_x, temp_y = 0, 0
def handle_events():
    global running
    global mx, my, end_num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                xs.append(event.x)
                ys.append(TUK_HEIGHT - event.y)
                end_num += 1

    pass

def move_cha():
    global x, y, xs, ys, line_frame, temp_x, temp_y, end_num
    t = line_frame / 100
    x = (1 - t) * x + t * xs[0]
    y = (1 - t) * y + t * ys[0]
    if line_frame == 100:
        temp_x, temp_y = x, y
        if end_num > 1:
            for i in range(1, end_num):
                xs[i - 1], ys[i - 1] = xs[i], ys[i]
            end_num -= 1
    pass

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for i in range(0, end_num):
        if xs[i] != x and ys[i] != y:
            hand_arrow.draw(xs[i], ys[i])
    if xs[0] > x:
        arrow = 1
    else:
        arrow = 0
    line_frame = (line_frame + 5) % (100 + 1)
    move_cha()
    if line_frame == 100:
        line_frame = 0
    character.clip_draw(frame * 100, 100 * arrow, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    handle_events()
    delay(0.1)
close_canvas()
