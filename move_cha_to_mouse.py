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
start_num, end_num = 0, 1
xs = [x]
ys = [y]
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

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    for i in range(start_num, end_num):
        hand_arrow.draw(xs[i], ys[i])
    #if xs[0] > x:
        #arrow = 1
    #else:
        #arrow = 0
    character.clip_draw(frame * 100, 100 * arrow, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()



    delay(0.1)
close_canvas()
