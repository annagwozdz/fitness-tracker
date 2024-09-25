from decimal import Decimal
from lib.run import Run

class RunRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all runs
    def all(self):
        rows = self._connection.execute('SELECT * from runs')
        runs = []
        for row in rows:
            item = Run(
                row["runner_id"],
                row["date"],
                row["run_type"],
                Decimal(row["distance"]), 
                row["duration"],
                row["satisfaction"]
            )
            runs.append(item)
        return runs