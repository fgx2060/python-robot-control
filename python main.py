import event, time, cyberpi, mbuild, mbot2

@event.is_press('a')
def is_btn_press():
    while True:
      if (mbuild.quad_rgb_sensor.is_color("black","L2",1)):
        mbot2.drive_speed(-50, -20)

      else:
        mbot2.drive_speed(30, -30)

      if (mbuild.quad_rgb_sensor.is_color("black","R2",1)):
        mbot2.drive_speed(20, 50)

      else:
        mbot2.drive_speed(30, -30)

@event.is_press('b')
def is_btn_press1():
    mbot2.forward(0)
