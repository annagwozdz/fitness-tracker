from lib.run import Run
from decimal import Decimal

class RunRepository:
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all runs
    def all(self):
        rows = self._connection.execute('SELECT * FROM runs')
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