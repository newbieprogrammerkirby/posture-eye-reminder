work_minutes = int(input("Minutes worked so far: "))
water = input("")

eyer_alarm_time = 20
water_alarm_time = 30
posture_alarm_time = 60


if work_minutes >= posture_alarm_time:
    print("ALARM: Be conscious of your neck posture")
elif work_minutes >= eyer_alarm_time:
    print("ALARM: Look away from the computer and slow blinks")
elif work_minutes >= water_alarm_time:
    print("ALARM: Hydrate")
else:
    print("No alarm yet.")
