cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven* space_in_a_car
average_passengers_per_car = passengers / cars_driven
#小车100 车内空间4.0 司机30 乘客90 
#空闲的车=车-司机 驾驶的车=司机 停车场的空间=驾驶的车*车内空间 平均每个车上的乘客=乘客/驾驶的车

print("There are",cars ,"cars available.")
#这可以得到car的车
print("There are only",drivers,"drivers available.")
#这仅仅可以得到drivers的司机
print("There will be",cars_not_driven,"empty cars today.")
#今天这有car_not_driven的空车
print("We can transport",carpool_capacity,"people toklday.")
#我们今天能运输停车厂空间的人
print("We have",passengers,"to carpool to6yyday.")
#我们有passengers去停车厂今天
print("We need to put about",average_passengers_per_car,"in each car.")
#在每个车里我们需要放大约average_passeners_per_car