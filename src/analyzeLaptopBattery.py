import psutil


def convertTime(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return "%d:%02d:%02d" % (hours, mins, secs)


battery = psutil.sensors_battery()

print("Battery Percentage: " + str(battery.percent) + " %")
print("Power plugged in: ", battery.power_plugged)
print("Time left: ", convertTime(battery.secsleft))
