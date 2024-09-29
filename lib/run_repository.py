from lib.run import Run  
from datetime import datetime, date

class RunRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM runs")
        return [
            Run(
                row["id"],  
                row["person_id"],
                row["date"] if isinstance(row["date"], date) else datetime.strptime(row["date"], "%Y-%m-%d").date(),
                row["run_type"],
                row["distance"],
                row["duration"],
                row["satisfaction"]
            ) for row in rows
        ]

    def find_by_personal_info_id(self, person_id):
        rows = self._connection.execute("SELECT * FROM runs WHERE person_id = %s", [person_id])
        return [
            Run(
                row["id"],  
                row["person_id"],
                row["date"],
                row["run_type"],
                row["distance"],
                row["duration"],
                row["satisfaction"]
            ) for row in rows
        ]

    def find_by_date(self, target_date):
        if isinstance(target_date, str):
            target_date = datetime.strptime(target_date, "%Y-%m-%d").date()
        
        rows = self._connection.execute("SELECT * FROM runs WHERE date = %s", [target_date])
        return [
            Run(
                row["id"],  
                row["person_id"],
                row["date"] if isinstance(row["date"], date) else datetime.strptime(row["date"], "%Y-%m-%d").date(),
                row["run_type"],
                row["distance"],
                row["duration"],
                row["satisfaction"]
            ) for row in rows
        ]

    def find_by_id(self, id):
        rows = self._connection.execute("SELECT * FROM runs WHERE id = %s", [id])
        if rows:  # Check if the list is not empty
            row = rows[0]  # Get the first row
            return Run(
                row["id"],
                row["person_id"],
                row["date"],
                row["run_type"],
                row["distance"],
                row["duration"],
                row["satisfaction"]
            )
        return None  

    def create(self, run):
        sql = """
        INSERT INTO runs (person_id, date, run_type, distance, duration, satisfaction)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
        """
        result = self._connection.execute(sql, [
            run.person_id,
            run.date,
            run.run_type,
            run.distance,
            run.duration,
            run.satisfaction
        ])
        
        return result[0]["id"] if result else None
    
     # Delete a run by its id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM runs WHERE id = %s', [id])
        return None