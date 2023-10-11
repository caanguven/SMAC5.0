from lewansoul_servo_bus import ServoBus

servo_bus = ServoBus('/dev/ttyUSB0')

#servo_bus.move_time_write(1, 90, 1.0)
servo_1 = servo_bus.get_servo(1)
servo_1.move_time_write(45, 2)

# Move servo with ID 2 to 180 degrees in 2.0 seconds
servo_2 = servo_bus.get_servo(2)
servo_2.move_time_write(45, 2)
