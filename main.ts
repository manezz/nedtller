input.onButtonPressed(Button.A, function () {
    while (number > 0) {
        basic.pause(1000)
        number += -1
    }
})
input.onButtonPressed(Button.B, function () {
    number = 30
})
let number = 0
number = 30
basic.forever(function () {
    basic.showNumber(number)
})
