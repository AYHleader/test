def on_button_pressed_a():
    global _true
    _true = _true + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global _false
    _false = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global _true
    _true = _true - 1
input.on_button_pressed(Button.B, on_button_pressed_b)

_true = 0
_false = 0
_false = 0
_true = 0
for index in range(1e+37):
    basic.show_number(_true)
    if _false == 1:
        basic.show_icon(IconNames.YES)
        break