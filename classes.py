class C:
    var = 10

    def test(self):
        print(vars(self))

class Car:
    cars = 0

    def __init__(self, speed=0, heading=0):
        self.speed = speed
        self.heading = heading

    def accelerate(self, inc):
        self.speed += inc
    
    def brake(self):
        self.speed -= 1

    def turn(self, angle):
        heading = self.heading
        heading += angle
        if heading > 360:
            heading -= 360
        elif heading < 0:
            heading += 360
        self.heading = heading
    
    def __setattr__(self, name, value):
        if name == "speed" and value > 20:
            print("too fast")
        super().__setattr__(name, value)        

    def __str__(self):
        return "Car@speed %d" %self.speed

class Convertible(Car): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top = 'soft'
        self.closed = True
    
    def open_top(self):
        self.closed = False
    
    def close_top(self):
        self.closed = True

class Person:
    def __init__(self):
        self.fname = ""
        self.surname = ""
        self.age = 0
    
    @property
    def name(self):
        return self.fname + ' ' + self.surname
    @name.setter
    def name(self, value):
        if ' ' in value:
            self.fname, self.surname = value.split()
        else:
            self.fname, self.surname = value, '' 
            
    # name = property(getName, setName)

    def talk(self):
        return "hello my name is {}".format(self.name)
    
    def walk(self):
        age = self.age
        if age < 1:
            return "crawl"
        elif age < 75:
            return "walk"
        else:
             return "hobble"