def on_button_pressed_a():
    global number
    while number > 0:
        basic.pause(1000)
        number += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global number
    number = 10
input.on_button_pressed(Button.B, on_button_pressed_b)

number = 0
number = 10

def on_forever():
    basic.show_number(number)
basic.forever(on_forever)
