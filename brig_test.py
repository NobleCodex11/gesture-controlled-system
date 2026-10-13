import screen_brightness_control as sbc

print("Current Brightness:")
print(sbc.get_brightness())

sbc.set_brightness(80)

print("Brightness changed to 80")