from lib.person import Person

"""
Person constructs with an id, first_name, last_name, height, weight, sex, age, fitness_level, activity_level
"""
def test_person_constructs():
    person = Person(1, "John", "Doe", 180, 75.0, "male", 33, "intermediate", "moderately_active")
    assert person.id == 1
    assert person.first_name == "John"
    assert person.last_name == "Doe"
    assert person.height == 180
    assert person.weight == 75.0
    assert person.sex == 'male'
    assert person.age == 33
    assert person.fitness_level == 'intermediate'
    assert person.activity_level == 'moderately_active'

"""
We can format person to string nicely
"""
def test_person_format_nicely():
    person = Person(1, "John", "Doe", 180, 75.0, "male", 33, "intermediate", "moderately_active")
    assert str(person) == "Person(1, John, Doe, 180, 75.0, male, 33, intermediate, moderately_active)"

"""
We can compare two identical people
And have them be equal
"""
def test_people_are_equal():
    person1 = Person(1, "John", "Doe", 180, 75.0, "male", 33, "intermediate", "moderately_active")
    person2 = Person(1, "John", "Doe", 180, 75.0, "male", 33, "intermediate", "moderately_active")
    assert person1 == person2