from lib.run import Run
from decimal import Decimal
from datetime import datetime # timedelta
 
"""
Run constructs with a personal_info_id, date, run_type, distance, duration, and satisfaction
"""
def test_run_constructs():
    run = Run(1, 1, datetime(2023, 9, 16).date(), 'sprint', Decimal('2.50'), '00:15:00', 7)
    assert run.date == datetime(2023, 9, 16).date()
"""
We can format runs to strings nicely
"""
def test_runs_format_nicely():
    run = Run(1, 1, '2023-09-16', 'sprint', Decimal('2.51'), '00:15:00', 7)
    assert str(run) == "Run(1, 1, 2023-09-16, sprint, 2.51, 00:15:00, 7)"
"""
We can compare two identical runs
And have them be equal
"""
def test_runs_are_equal():
    run1 = Run(1, 1, '2023-09-16', 'sprint', Decimal('2.51'), '00:15:00', 7)
    run2 = Run(1, 1, '2023-09-16', 'sprint', Decimal('2.51'), '00:15:00', 7)
    assert run1 == run2