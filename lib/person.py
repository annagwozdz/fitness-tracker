class Person:
    def __init__(self, id, first_name, last_name, height, weight, sex, age, fitness_level, activity_level):
        self.id = id 
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.age = age
        self.fitness_level = fitness_level
        self.activity_level = activity_level

    def __repr__(self):
        return f"Person({self.id}, {self.first_name}, {self.last_name}, {self.height}, {self.weight}, {self.sex}, {self.age}, {self.fitness_level}, {self.activity_level})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

