# INSERT INTO runs (runner_id, date, run_type, distance, duration, satisfaction) 
# VALUES (2, '2023-09-16', 2, 2.50, 15, 7);  -- Using runner_id 2, run_type 'Sprint'

from lib.run import Run
from _decimal import Decimal
from datetime import datetime

"""
 Run constructs with a runner_id, date run_type, distance, duration, and satisfaction
"""
def test_run_constructs():
    run = Run(2, '2023-09-16', 2, Decimal('2.50'), 15, 7)
    assert run.runner_id == 2
    assert run.date == datetime(2023, 9, 16).date()  # Compare to a datetime.date object
    assert run.run_type == 2
    assert run.distance == Decimal('2.50')  
    assert run.duration == 15
    assert run.satisfaction == 7

"""
We can format runs to strings nicely
"""
def test_runs_format_nicely():
    run = Run(2, '2023-09-16', 2, Decimal('2.51'), 15, 7)
    assert str(run) == "Run(2, 2023-09-16, 2, 2.51, 15, 7)"


"""
We can compare two identical runs
And have them be equal
"""
def test_runs_are_equal():
    run1 = Run(2, '2023-09-16', 2, Decimal('2.51'), 15, 7)
    run2 = Run(2, '2023-09-16', 2, Decimal('2.51'), 15, 7)
    assert run1 == run2
