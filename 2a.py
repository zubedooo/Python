class vehicle:
    def __init__(self):
        print('Class Vehicle')
class bike(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        print('Class Bike')
class car(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        print('Class Car')
class pedal_bike(bike):
    def __init__(self):
        bike.__init__(self)
        print('Class Pedal bike')
class motor_bike(bike):
    def __init__(self):
        bike.__init__(self)
        print('Class Motor bike')
obj = pedal_bike()
#obj = motor_bike()
#obj = bike()
#obj = car()
#obj = vehicle()