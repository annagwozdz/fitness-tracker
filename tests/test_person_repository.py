from lib.person_repository import PersonRepository
from lib.person import Person

"""
When we call PersonRepository #all
We get a list of Person objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = PersonRepository(db_connection)

    people = repository.all()

    assert people == [
        Person(1, 'John', 'Doe', 180, 75.0, 'male', 33, 'intermediate', 'moderately_active')
    ]

"""
When we call PersonRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = PersonRepository(db_connection)

    repository.create(Person(2, 'John', 'Doe', 180, 75.0, 'male', 33, 'intermediate', 'moderately_active'))

    result = repository.all()
    assert result == [
        Person(1, 'John', 'Doe', 180, 75.0, 'male', 33, 'intermediate', 'moderately_active'),
        Person(2, 'John', 'Doe', 180, 75.0, 'male', 33, 'intermediate', 'moderately_active'),
        
    ]

"""
When we call RuunRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = PersonRepository(db_connection)
    repository.delete(1) 

    runs = repository.all()
    assert runs == []