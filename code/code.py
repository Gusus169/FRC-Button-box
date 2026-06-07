import time
import board
import digitalio
import busio
import usb_hid
import keypad
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

# --- CUSTOM 32-BUTTON GAMEPAD DRIVER ---
class FRCGamepad:
    def __init__(self, devices):
        for device in devices:
            if device.usage == 0x05 and device.usage_page == 0x01:
                self._device = device
                break
        else:
            raise ValueError("Could not find Gamepad HID device. Check boot.py")
        self._report = bytearray(4) # 32 bits for 32 buttons
        
    def press(self, button):
        bit = button - 1
        self._report[bit // 8] |= 1 << (bit % 8)
        self._device.send_report(self._report)
        
    def release(self, button):
        bit = button - 1
        self._report[bit // 8] &= ~(1 << (bit % 8))
        self._device.send_report(self._report)

gp = FRCGamepad(usb_hid.devices)

# --- SETUP STATUS LED ---
led = digitalio.DigitalInOut(board.GP22)
led.direction = digitalio.Direction.OUTPUT
led.value = True # Solid glowing when connected and idle

# --- SETUP OLED DISPLAY ---
displayio.release_displays()
i2c = busio.I2C(scl=board.GP13, sda=board.GP12)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Create text layout for OLED
splash = displayio.Group()
display.root_group = splash
oled_text = label.Label(terminalio.FONT, text="READY", color=0xFFFFFF, x=20, y=30, scale=3)
splash.append(oled_text)

# --- SETUP 5x6 HARDWARE MATRIX ---
# Rows: GP2 to GP6 | Cols: GP7 to GP11, plus GP15
row_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6)
col_pins = (board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP15)

# The keypad library runs in the background in C, making it incredibly fast and handles debouncing naturally
matrix = keypad.KeyMatrix(
    row_pins, col_pins,
    columns_to_anodes=False # Matches your 1N4148W diode orientation
)

print("FRC Button Box Initialized.")

# --- MAIN EVENT LOOP ---
while True:
    event = matrix.events.get()
    
    if event:
        # event.key_number maps the grid from 0 to 29. 
        # You requested buttons to output as 2 through 31.
        button_num = event.key_number + 2 
        
        if event.pressed:
            gp.press(button_num)
            oled_text.text = f"BTN {button_num}"
            # Turn LED off momentarily to create a "blink" effect when working
            led.value = False 
            
        elif event.released:
            gp.release(button_num)
            
            # If no other buttons are currently being held down, return to idle
            if matrix.pressed_count == 0:
                oled_text.text = "READY"
                led.value = True # Return to solid glow

    time.sleep(0.002) # Tiny delay to keep the loop stable