temps = [25.2,16.8, 31.4, 23.9, 28, 22.5]
tamthoi = 19.6
t = temps.append(tamthoi)
#cau b
a = temps.sort()
print('Thứ tự tăng dần:',temps)
#cau c
#1
cool_temps =[]
warm_temps =[]
for i in temps: 
      if i > 20:
          cool_temps.append(i)
print(cool_temps)
for i in temps: 
      if i < 20:
          warm_temps.append(i)
print(warm_temps)

