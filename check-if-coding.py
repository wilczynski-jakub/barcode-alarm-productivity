import keyboard
import webbrowser
import subprocess
import time
from barcode import ISBN13
from barcode.writer import ImageWriter
from PIL import Image


# generate the image with barcode to scan (in order to turn off my alarm)
def generate_barcode(num):

    # generate the barcode that I will have to scan in the alarm app
    book_barcode = ISBN13(num, writer=ImageWriter())
    book_barcode.save('barcode')

    # make it look better
    image = Image.open("barcode.png")
    cropped_image = image.crop((0, 0, image.width, image.height - 80))
    cropped_image.save("barcode.png")
    cropped_image.show()

    # delete the .png file, in order not to cheat in the future
    time.sleep(1)
    subprocess.run("del /F /Q barcode.png", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


# detect whether the user is programming or not
def check_programming(input_stream):

    programming_chars = {'{', '}', '(', ')', '=', '.', '<', '>', ';', 'space', 'shift', 'tab', 'ctrl', 'tab', 'enter'}
    count = {char: 0 for char in programming_chars}
    unique_char_count = 0
    MINIMUM_CHARACTERS = 100

    for char in input_stream:
        if char in programming_chars:
            if count[char] == 0:
                unique_char_count += 1
            count[char] += 1

    total_count = sum(count.values())

    if total_count > MINIMUM_CHARACTERS and unique_char_count > len(programming_chars) / 2:
        return True
    else:
        return False


# read the keyboard and check if programming
def read_keyboard_input():

    print("Listening for keyboard input...")
    recorded = []

    def record_key(key):
        recorded.append(key.name)

        if len(recorded) > 1000:
            del recorded[:-1000]

        if check_programming(recorded):
            # this is the barcode number that I saved in the alarm app
            generate_barcode('97845733823443524674256098')
            keyboard.unhook_all()
            subprocess.run('taskkill /F /IM python.exe', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    keyboard.hook(record_key)
    keyboard.wait()


# run the program
read_keyboard_input()
