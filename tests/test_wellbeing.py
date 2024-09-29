from lib.wellbeing import Wellbeing
from datetime import datetime

"""
Wellbeing constructs with an id, person_id, date, calories_in, calories_out, mood, stress_level, hours_of_sleep, worked_out
"""
def test_wellbeing_constructs():
    wellbeing = Wellbeing(1, 1, datetime(2023, 9, 15).date(), 2500, 2000, 7, 5, '08:00', True)
    assert wellbeing.id == 1
    assert wellbeing.person_id == 1
    assert wellbeing.date == datetime(2023, 9, 15).date()
    assert wellbeing.calories_in == 2500
    assert wellbeing.calories_out == 2000
    assert wellbeing.mood == 7
    assert wellbeing.stress_level == 5
    assert wellbeing.hours_of_sleep == '08:00'
    assert wellbeing.worked_out == True

"""
We can format wellbeing to strings nicely
"""
def test_wellbeing_format_nicely():
    wellbeing = Wellbeing(1, 1, '2023-09-15', 2500, 2000, 7, 5, '08:00', True)
    assert str(wellbeing) == "Wellbeing(1, 1, 2023-09-15, 2500, 2000, 7, 5, 08:00, True)"

"""
We can compare two identical wellbeing entries
And have them be equal
"""
def test_wellbeing_entries_are_equal():
    wellbeing1 = Wellbeing(1, 1, '2023-09-15', 2500, 2000, 7, 5, '08:00', True)
    wellbeing2 = Wellbeing(1, 1, '2023-09-15', 2500, 2000, 7, 5, '08:00', True)
    assert wellbeing1 == wellbeing2
    