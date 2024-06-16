import pyautogui as pg
from pyperclip import paste
from keyboard import is_pressed
print("")
print("=== Instruction ===")
print("Firstly you need to download Charles proxy and log in using this data")
roll, sign, required_num = input("roll, sign, required_num = ").split()
#roll, sign, required_num = "d50", ">", 45
required_num=int(required_num)
log=[]
def paste_to_num(clipboard_content):
    log.append(int(clipboard_content[clipboard_content.index('total')+8:-3]))
    return log[-1]
def execute():
    pg.click(1195,991)
    pg.keyDown("Alt")
    pg.press("Tab")
    pg.keyUp("Alt")
    pg.keyDown("Alt")
    pg.press("Tab")
    pg.press("Tab")
    pg.keyUp("Alt")
    print(log)
    exit()
def abort():
    pg.click(526,952)
    pg.click(324,141)
    pg.click(382,161)
    pg.press("delete")
    pg.click(1192,990)
    pg.hotkey("alt","tab")
    pg.hotkey("alt","tab","tab")

def main_func():
    while is_pressed('capslock')==False:
        pg.hotkey("alt", "tab")
        pg.click(1745,953)
        pg.write(f'/roll {roll}')
        pg.click(1797,1005)
        while True:
            r, g, b = pg.pixel(1658, 618)
            if (r, g, b) == (255, 255, 255):
                pg.click(460,116)
                pg.click(480,952)
                pg.doubleClick(382,178)
                pg.click(382,178)
                pg.hotkey("ctrl", "c")
                #clipboard_content = paste()
                #crnt_num = paste_to_num(clipboard_content)
                crnt_num = paste_to_num(paste())
                if sign == ">" and crnt_num>=required_num:
                    execute()
                    break
                elif sign == "<" and crnt_num<=required_num:
                    execute()
                    break
                else:
                    abort()
                    break

if __name__ == "__main__":
    main_func()