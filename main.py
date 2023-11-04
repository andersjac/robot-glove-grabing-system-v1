serial.redirect_to_usb()

def on_forever():
    basic.show_string("P0=")
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
    basic.show_string("P1=")
    basic.show_number(pins.analog_read_pin(AnalogPin.P1))
    basic.show_string("P2=")
    basic.show_number(pins.analog_read_pin(AnalogPin.P2))
    basic.show_string("avg=")
    basic.show_number((pins.analog_read_pin(AnalogPin.P0) + pins.analog_read_pin(AnalogPin.P2) + pins.analog_read_pin(AnalogPin.P1)) / 3)
basic.forever(on_forever)

def on_forever2():
    serial.write_number(0)
    basic.show_number(0)
basic.forever(on_forever2)
