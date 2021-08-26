import threading, requests, gratient, random, pygame, string, io

banner = """
   ▄███▄   ▄█ ██▄   ████▄ █    ████▄    ▄   
   █▀   ▀  ██ █  █  █   █ █    █   █     █  
   ██▄▄    ██ █   █ █   █ █    █   █ ██   █ 
   █▄   ▄▀ ▐█ █  █  ▀████ ███▄ ▀████ █ █  █ 
   ▀███▀    ▐ ███▀            ▀      █  █ █ 
                    v  e  n  a  x    █   ██ 
"""

print(gratient.purple(banner))
global FREEIMAGEHOST_image_link_valid
FREEIMAGEHOST_image_link_valid = ""
actual_image_link = ""
link_image = False

def FREEIMAGEHOST():
    while True:
        image_code = "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(6))
        FREEIMAGEHOST_image_link = f"https://iili.io/{image_code}.png"
        FREEIMAGEHOST_image = requests.get(FREEIMAGEHOST_image_link)
        if FREEIMAGEHOST_image.status_code == 200:
            print(gratient.blue(f"   [>] FREEIMAGEHOST : {FREEIMAGEHOST_image_link}"), end = "")
            global FREEIMAGEHOST_image_link_valid
            FREEIMAGEHOST_image_link_valid = FREEIMAGEHOST_image_link

threading.Thread(target = FREEIMAGEHOST).start(); threading.Thread(target = FREEIMAGEHOST).start(); threading.Thread(target = FREEIMAGEHOST).start()


pygame.init()
screen = pygame.display.set_mode((950, 600))
pygame.display.set_caption("Eidolon")

while True:
    screen.fill((0, 0, 0))
    if not FREEIMAGEHOST_image_link_valid == "" and not FREEIMAGEHOST_image_link_valid == actual_image_link:
        actual_image_link = FREEIMAGEHOST_image_link_valid
        try:
            link_image = pygame.image.load(io.BytesIO(requests.get(FREEIMAGEHOST_image_link_valid).content))
            link_image = pygame.transform.scale(link_image, (950, 600))
        except:
            pass
    if link_image:
        screen.blit(link_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update() 
