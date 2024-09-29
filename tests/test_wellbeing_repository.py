from lib.wellbeing_repository import WellbeingRepository
from lib.wellbeing import Wellbeing
from datetime import datetime

"""
When we call WellbeingRepository #all
We get a list of Wellbeing objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = WellbeingRepository(db_connection)

    wellbeing = repository.all()

    assert wellbeing == [
        Wellbeing(1, 1, datetime(2023, 9, 15).date(), 2500, 2000, 7, 5, '08:00', True),
        Wellbeing(2, 1, datetime(2023, 9, 16).date(), 2200, 1800, 6, 4, '07:30', True),
        Wellbeing(3, 1, datetime(2023, 9, 17).date(), 2700, 2100, 8, 6, '06:45', False),
        Wellbeing(4, 1, datetime(2023, 9, 18).date(), 2600, 1900, 7, 5, '07:00', True),
        Wellbeing(5, 1, datetime(2023, 9, 19).date(), 2400, 2000, 6, 4, '07:15', False),
    ]

"""
When we call WellbeingRepository #find_by_date, we get all wellbeing entries for the specified date.
"""
def test_find_by_date(db_connection):
    db_connection.seed("seeds/fitness_data.sql")

    repository = WellbeingRepository(db_connection)
    target_date = datetime(2023, 9, 15).date()
    expected_wellbeing = [
        Wellbeing(1, 1, target_date, 2500, 2000, 7, 5, '08:00', True)
    ]
    
    wellbeing_entries = repository.find_by_date(target_date)
    assert wellbeing_entries == expected_wellbeing


"""
When we call WellbeingRepository #find_by_id, we get all wellbeing entries for the specified id.
"""
def test_find_by_id(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = WellbeingRepository(db_connection)

    id = 1  
    expected_wellbeing = Wellbeing(
        id,
        1,
        datetime(2023, 9, 15).date(),
        2500,
        2000,
        7,
        5,
        '08:00',
        True
        
    )
    
    wellbeing = repository.find_by_id(id)
    assert wellbeing == expected_wellbeing

"""
When we call RunRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = WellbeingRepository(db_connection)

    new_wellbeing = Wellbeing(
        id=0,  
        person_id=1,
        date=datetime.strptime('2023-09-15', '%Y-%m-%d').date(),
        calories_in=2500,
        calories_out=2000,
        mood=7,
        stress_level=5,
        hours_of_sleep='08:00',
        worked_out=True

    )
    
    id = repository.create(new_wellbeing)

    assert id is not None  # Ensure a new id was generated
    result = repository.all()
    assert len(result) > 0

"""
When we call WellbeingRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = WellbeingRepository(db_connection)
    repository.delete(5) 

    wellbeing = repository.all()
    assert wellbeing == [
        Wellbeing(1, 1, datetime(2023, 9, 15).date(), 2500, 2000, 7, 5, '08:00', True),
        Wellbeing(2, 1, datetime(2023, 9, 16).date(), 2200, 1800, 6, 4, '07:30', True),
        Wellbeing(3, 1, datetime(2023, 9, 17).date(), 2700, 2100, 8, 6, '06:45', False),
        Wellbeing(4, 1, datetime(2023, 9, 18).date(), 2600, 1900, 7, 5, '07:00', True)
    ]