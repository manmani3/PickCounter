import win32gui
from PIL import ImageGrab, Image

def captureClient() :
    
    window = win32gui.FindWindow(None, r'League of Legends')
    win32gui.SetForegroundWindow(window)

    position = win32gui.GetWindowRect(window)

    image = ImageGrab.grab(position)

    return image

def cropImages(image) :

    width, height = image.size
    print(width, height)

    p_1600 = {'start_x' : 83, 'start_y' : 144, 'size' : 50, 'margin' : 100, 'enemy_x': 1504}
    p_1280 = {'start_x' : 66, 'start_y' : 116, 'size' : 36, 'margin' : 80, 'enemy_x': 1203}
    p_1024 = {'start_x' : 53, 'start_y' : 92, 'size' : 32, 'margin' : 64, 'enemy_x': 963}
    
    b_1600 = {'start_x' : 20, 'start_y' : 40, 'size' : 33, 'margin' : 50, 'enemy_x': 1346}
    b_1280 = {'start_x' : 17, 'start_y' : 32, 'size' : 26, 'margin' : 40, 'enemy_x': 1078}
    b_1024 = {'start_x' : 16, 'start_y' : 24, 'size' : 20, 'margin' : 32, 'enemy_x': 863}

    our_p = list()
    our_b = list()
    enemy_p = list()
    enemy_b = list()

    if width == 1600 and height == 900 :
        p_pos = p_1600
        b_pos = b_1600

    elif width == 1280 and height == 768 :
        p_pos = p_1280
        b_pos = b_1280
        
    elif width == 1024 and height == 576 :
        p_pos = p_1024
        b_pos = b_1280
        
    else :
        return -1

    for i in range(0, 5) :
        our_p.insert(i, image.crop((p_pos['start_x'],
                                    p_pos['start_y'],
                                    p_pos['start_x'] + p_pos['size'],
                                    p_pos['start_y'] + p_pos['size'])))

        our_b.insert(i, image.crop((b_pos['start_x'],
                                    b_pos['start_y'],
                                    b_pos['start_x'] + b_pos['size'],
                                    b_pos['start_y'] + b_pos['size'])))

        enemy_p.insert(i, image.crop((p_pos['enemy_x'],
                                      p_pos['start_y'],
                                      p_pos['enemy_x'] + p_pos['size'],
                                      p_pos['start_y'] + p_pos['size'])))

        enemy_b.insert(i, image.crop((b_pos['enemy_x'],
                                      b_pos['start_y'],
                                      b_pos['enemy_x'] + b_pos['size'],
                                      b_pos['start_y'] + b_pos['size'])))

        p_pos['start_y'] += p_pos['margin']
        b_pos['start_x'] += p_pos['margin']
        b_pos['enemy_x'] += b_pos['margin']

    return our_p, our_b, enemy_p, enemy_b
