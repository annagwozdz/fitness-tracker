from lib.run import Run
from decimal import Decimal
from datetime import datetime, timedelta

"""
Run constructs with a runner_id, date, run_type, distance, duration, and satisfaction
"""
def test_run_constructs():
    run = Run(2, '2023-09-16', 'sprint', Decimal('2.50'), '00:15:00', 7)  # Use string for duration  
    assert run.runner_id == 2
    assert run.date == datetime(2023, 9, 16).date()  # Compare to a datetime.date object
    assert run.run_type == 'sprint'
    assert run.distance == Decimal('2.50')
    assert run.duration == timedelta(hours=0, minutes=15)  # Adjust to compare with timedelta

"""
We can format runs to strings nicely
"""
def test_runs_format_nicely():
    run = Run(2, '2023-09-16', 'sprint', Decimal('2.51'), '00:15:00', 7)
    assert str(run) == "Run(2, 2023-09-16, sprint, 2.51, 00:15:00, 7)"

"""
We can compare two identical runs
And have them be equal
"""
def test_runs_are_equal():
    run1 = Run(2, '2023-09-16', 'sprint', Decimal('2.51'), '00:15:00', 7)
    run2 = Run(2, '2023-09-16', 'sprint', Decimal('2.51'), '00:15:00', 7)
    assert run1 == run2