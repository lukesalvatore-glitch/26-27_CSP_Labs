starting_milliseconds = 10000123
print("starting milliseconds: " + str(starting_milliseconds))
hours = starting_milliseconds // 3600000
print("hours: \t\t" + str(hours))
millisecondsleft1 = starting_milliseconds % 3600000
minutes = millisecondsleft1 // 60000
print("minutes: \t\t" + str(minutes))
millisecondsleft2 = millisecondsleft1 % 60000
seconds = millisecondsleft2 // 1000
print("seconds: \t\t" + str(seconds))
milli_seconds = millisecondsleft2 % 1000
print("milli seconds: \t" + str(milli_seconds))
