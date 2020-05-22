import pygame, pyautogui, json, os

# initiating pygame/window
pygame.init()
import trig
running = True
width = int(pyautogui.size()[1]/1.2)
height = int(width*0.71)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("trigonometry")

# initiating colors
colors_file = "colors.json"
if os.path.exists(colors_file):
    with open(colors_file) as f:
        colors = json.load(f)
else:
    colors = {
        "light":{
            "bg":(255, 255, 255),
            "lines" : (204, 204, 204),
            "button_bg":(235, 235, 235),
            "text":(150, 150, 150)
        },
        "dark":{
            "bg":(28, 24, 28),
            "lines" : (68, 64, 68),
            "button_bg":(38, 34, 38),
            "text":(104, 100, 104)
        }
    }
    with open(colors_file, "w") as f:
        json.dump(colors, f)

buttons_bottom = height/8
switchY = height-(height/8)
switchX = width-(width/5)
theme = colors["dark"]
clicked = False
circle = trig.trig(width, height, pygame.mouse.get_pos(), theme)

#circle = trig.trig(width, height, pygame.mouse.get_pos())

while running:
    ### events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### logic
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    circle.update(mouse)
    if not click:
        clicked = False

    # button logic
    if click and not clicked:
        if mouse[1] < buttons_bottom:
            pass
        elif mouse[1] > switchY:
            if mouse[0] > switchX:
                    if theme == colors["dark"]:
                        theme = colors["light"]
                    else:
                        theme = colors["dark"]
                    circle.changeTheme(theme)
        clicked = True

    #trig.update(mouse, state)

    ### drawing

    # background
    screen.fill(theme["bg"])

    # top buttons
    """ pygame.draw.rect(screen, theme["button_bg"], [0, 0, width, buttons_bottom])
    pygame.draw.line(screen, theme["lines"], [0, buttons_bottom], [width, buttons_bottom], height//150)
    for i in range(1, 4):
        pygame.draw.line(screen, theme["lines"], [width/4*i, 0], [width/4*i, buttons_bottom], height//150) """

    # theme switch button
    pygame.draw.line(screen, theme["lines"], [switchX, switchY], [width, switchY], height//150)
    pygame.draw.line(screen, theme["lines"], [switchX, switchY], [switchX, height], height//150)
    pygame.draw.rect(screen, theme["button_bg"], [switchX, switchY, width, height])
    font = pygame.font.SysFont('Calibri', height//18, False, False)
    if theme == colors["dark"]:
        text = font.render("light theme", True, theme["text"])
    else:
        text = font.render("dark theme", True, theme["text"])
    screen.blit(text, [switchX+height//25, switchY+height//25])
    
    circle.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()