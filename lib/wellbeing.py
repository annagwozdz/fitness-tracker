
class Wellbeing:
    def __init__(self, id, person_id, date, calories_in, calories_out, mood, stress_level, hours_of_sleep, worked_out):
        self.id = id 
        self.person_id = person_id
        self.date = date
        self.calories_in = calories_in
        self.calories_out = calories_out
        self.mood = mood
        self.stress_level = stress_level
        self.hours_of_sleep = hours_of_sleep
        self.worked_out = worked_out

    def __repr__(self):
        return f"Wellbeing({self.id}, {self.person_id}, {self.date}, {self.calories_in}, {self.calories_out}, {self.mood}, {self.stress_level}, {self.hours_of_sleep}, {self.worked_out})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__