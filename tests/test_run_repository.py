from lib.run_repository import RunRepository
from lib.run import Run
from decimal import Decimal
from datetime import datetime

"""
When we call RunRepository #all
We get a list of Run objects reflecting the seed data.
"""

def test_get_all_records(db_connection):
    db_connection.seed("seeds/fitness_data.sql")  # Seed our database with some test data
    repository = RunRepository(db_connection)  # Create a new RunRepository

    runs = repository.all()  
    
    assert runs == [
        Run(1, datetime(2023, 9, 15).date(), 'interval', Decimal('5.00'), '00:30:00', 8),
        Run(2, datetime(2023, 9, 16).date(), 'sprint', Decimal('2.50'), '00:15:00', 7),
    ]
# """
# When we call BookRepository#find
# We get a single Book object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/fitness_data.sql")
#     repository = BookRepository(db_connection)

#     book = repository.find(3)
#     assert book == Book(3, "Bluets", "Maggie Nelson")

# """
# When we call BookRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/fitness_data.sql")
#     repository = BookRepository(db_connection)

#     repository.create(Book(None, "The Great Gatsby", "F. Scott Fitzgerald"))

#     result = repository.all()
#     assert result == [
#         Book(1, "Invisible Cities", "Italo Calvino"),
#         Book(2, "The Man Who Was Thursday", "GK Chesterton"),
#         Book(3, "Bluets", "Maggie Nelson"),
#         Book(4, "No Place on Earth", "Christa Wolf"),
#         Book(5, "Nevada", "Imogen Binnie"),
#         Book(6, "The Great Gatsby", "F. Scott Fitzgerald"),
#     ]

# """
# When we call BookRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/fitness_data.sql")
#     repository = BookRepository(db_connection)
#     repository.delete(3) # Apologies to Maggie Nelson fans

#     result = repository.all()
#     assert result == [
#         Book(1, "Invisible Cities", "Italo Calvino"),
#         Book(2, "The Man Who Was Thursday", "GK Chesterton"),
#         Book(4, "No Place on Earth", "Christa Wolf"),
#         Book(5, "Nevada", "Imogen Binnie"),
#     ]
