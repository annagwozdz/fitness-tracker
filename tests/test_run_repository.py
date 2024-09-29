from lib.run_repository import RunRepository
from lib.run import Run
from decimal import Decimal
from datetime import datetime, timedelta

"""
When we call RunRepository #all
We get a list of Run objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = RunRepository(db_connection)

    runs = repository.all()

    assert runs == [
        Run(1, 1, datetime(2023, 9, 15).date(), 'interval', Decimal('5.00'), timedelta(minutes=30), 8),
        Run(2, 1, datetime(2023, 9, 16).date(), 'sprint', Decimal('2.50'), timedelta(minutes=15), 7),
        Run(3, 1, datetime(2023, 9, 17).date(), 'long_distance', Decimal('10.00'), timedelta(hours=1), 9),
        Run(4, 1, datetime(2023, 9, 18).date(), 'race', Decimal('7.00'), timedelta(minutes=45), 9),
        Run(5, 1, datetime(2023, 9, 19).date(), 'interval', Decimal('6.00'), timedelta(minutes=35), 8),
    ]

# """
# When we call RunRepository #find_by_personal_info_id, we get all runs for the specified person.
# """
# def test_find_personal_info_runs(db_connection):
#     db_connection.seed("seeds/fitness_data.sql")

#     repository = RunRepository(db_connection)
#     person_id = 1  
#     expected_runs = [
#         Run(1, person_id, datetime(2023, 9, 15).date(), 'interval', Decimal('5.00'), timedelta(minutes=30), 8),
#         Run(2, person_id, datetime(2023, 9, 16).date(), 'sprint', Decimal('2.50'), timedelta(minutes=15), 7),
#         Run(3, person_id, datetime(2023, 9, 17).date(), 'long_distance', Decimal('10.00'), timedelta(hours=1), 9),
#         Run(4, person_id, datetime(2023, 9, 18).date(), 'race', Decimal('7.00'), timedelta(minutes=45), 9),
#         Run(5, person_id, datetime(2023, 9, 19).date(), 'interval', Decimal('6.00'), timedelta(minutes=35), 8),
#     ]
    
#     runs = repository.find_by_personal_info_id(person_id)
#     assert runs == expected_runs

"""
When we call RunRepository #find_by_date, we get all runs for the specified date.
"""
def test_find_by_date(db_connection):
    db_connection.seed("seeds/fitness_data.sql")

    repository = RunRepository(db_connection)
    target_date = datetime(2023, 9, 15).date()
    expected_runs = [
        Run(1, 1, target_date, 'interval', Decimal('5.00'), timedelta(minutes=30), 8),
    ]
    
    runs = repository.find_by_date(target_date)
    assert runs == expected_runs

def test_find_by_id(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = RunRepository(db_connection)

    id = 1  
    expected_run = Run(
        id,
        1,
        datetime(2023, 9, 15).date(),
        'interval',
        Decimal('5.00'),
        timedelta(minutes=30),
        8
    )
    
    run = repository.find_by_id(id)
    assert run == expected_run

"""
When we call RunRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = RunRepository(db_connection)

    new_run = Run(
        id=0,  
        person_id=1,
        date=datetime.strptime('2023-09-20', '%Y-%m-%d').date(),
        run_type='sprint',
        distance=Decimal('2.50'),
        duration='00:16:00',
        satisfaction=7
    )
    
    id = repository.create(new_run)

    assert id is not None  # Ensure a new id was generated
    result = repository.all()
    assert len(result) > 0

"""
When we call RuunRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/fitness_data.sql")
    repository = RunRepository(db_connection)
    repository.delete(5) 

    runs = repository.all()
    assert runs == [
        Run(1, 1, datetime(2023, 9, 15).date(), 'interval', Decimal('5.00'), timedelta(minutes=30), 8),
        Run(2, 1, datetime(2023, 9, 16).date(), 'sprint', Decimal('2.50'), timedelta(minutes=15), 7),
        Run(3, 1, datetime(2023, 9, 17).date(), 'long_distance', Decimal('10.00'), timedelta(hours=1), 9),
        Run(4, 1, datetime(2023, 9, 18).date(), 'race', Decimal('7.00'), timedelta(minutes=45), 9),
    ]
