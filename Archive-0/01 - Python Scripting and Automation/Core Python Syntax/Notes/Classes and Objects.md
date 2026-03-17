
```python
# Base class
class Vehicle:
	# Constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
	
    def vehicle_info(self):
        return f'{self.year} {self.make} {self.model}'
```

```python
# Derived class
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
	
    # Method overloading
    def vehicle_info(self):
        return f'{self.year} {self.make} {self.model} with {self.doors} doors'
```

```python
# Constructor Overloading Example
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar=False):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
	
    def vehicle_info(self):
        sidecar = 'with sidecar' if self.has_sidecar else 'without sidecar'
        return f'{self.year} {self.make} {self.model} {sidecar}'
```

### Creating instances of each class
```python
# Creating instances of each class
car = Car('Toyota', 'Camry', 2020, 4)
motorcycle_with_sidecar = Motorcycle('Harley-Davidson', 'Sportster', 2019, True)
motorcycle_without_sidecar = Motorcycle('Yamaha', 'MT-07', 2022)
```

```python
>>> print(car.vehicle_info())
# 2020 Toyota Camry with 4 doors
>>> print(motorcycle_with_sidecar.vehicle_info())
# 2019 Harley-Davidson Sportster with sidecar
>>> print(motorcycle_without_sidecar.vehicle_info())
# 2022 Yamaha MT-07 without sidecar
```