work_minutes = int(input("Minutes worked so far: "))

eyer_alarm_time = 20
posture_alarm_time = 60

if work_minutes >= posture_alarm_time:
    print("ALARM: Be concious of your neck posture")
elif work_minutes >= eyer_alarm_time:
    print("ALARM: Look away from the computer and slow blinks")
else:
    print("No alarm yet.")
