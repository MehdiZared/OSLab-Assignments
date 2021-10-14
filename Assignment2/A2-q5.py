
s = int(input("seconds : "))
h =int( s / 3600)
s = s % 3600
m = int(s / 60)
s = s % 60
print('Time  : ',h,':',m,':',s)


