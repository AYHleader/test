input.onButtonPressed(Button.A, function () {
    _true = _true + 1
})
input.onButtonPressed(Button.AB, function () {
    _false = 1
})
input.onButtonPressed(Button.B, function () {
    _true = _true - 1
})
let _true = 0
let _false = 0
basic.showString("on")
_false = 0
_true = 0
for (let index = 0; index < 1e+37; index++) {
    basic.showNumber(_true)
    if (_false == 1) {
        basic.showIcon(IconNames.Yes)
        break;
    }
}
