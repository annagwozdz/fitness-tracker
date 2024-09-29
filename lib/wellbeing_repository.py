from lib.wellbeing import Wellbeing
from datetime import datetime, date

class WellbeingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM wellbeing_diary")
        return [
            Wellbeing(
                row["id"],
                row["person_id"],
                row["date"] if isinstance(row["date"], date) else datetime.strptime(row["date"], "%Y-%m-%d").date(),
                row["calories_in"],
                row["calories_out"],
                row["mood"],
                row["stress_level"],

                # Convert the hours_of_sleep INTERVAL to 'HH:MM' format
                str(row["hours_of_sleep"])[:-3] if isinstance(row["hours_of_sleep"], str) else f'{row["hours_of_sleep"].seconds // 3600:02}:{(row["hours_of_sleep"].seconds // 60) % 60:02}',
                row["worked_out"]
            ) for row in rows
        ]
    
    def find_by_date(self, target_date):
        if isinstance(target_date, str):
            target_date = datetime.strptime(target_date, "%Y-%m-%d").date()
        
        rows = self._connection.execute("SELECT * FROM wellbeing_diary WHERE date = %s", [target_date])
        return [
            Wellbeing(
                row["id"],  
                row["person_id"],
                row["date"] if isinstance(row["date"], date) else datetime.strptime(row["date"], "%Y-%m-%d").date(),
                row["calories_in"],
                row["calories_out"],
                row["mood"],
                row["stress_level"],
                str(row["hours_of_sleep"])[:-3] if isinstance(row["hours_of_sleep"], str) else f'{row["hours_of_sleep"].seconds // 3600:02}:{(row["hours_of_sleep"].seconds // 60) % 60:02}',
                row["worked_out"]
            ) for row in rows
        ]
    
    def find_by_id(self, id):
        rows = self._connection.execute("SELECT * FROM wellbeing_diary WHERE id = %s", [id])
        if rows:  
            row = rows[0]  
            return Wellbeing(
                row["id"],
                row["person_id"],
                row["date"],
                row["calories_in"],
                row["calories_out"],
                row["mood"],
                row["stress_level"],
                str(row["hours_of_sleep"])[:-3] if isinstance(row["hours_of_sleep"], str) else f'{row["hours_of_sleep"].seconds // 3600:02}:{(row["hours_of_sleep"].seconds // 60) % 60:02}',
                row["worked_out"]


            )
        return None  

    def create(self, wellbeing):
        sql = """
        INSERT INTO wellbeing_diary (person_id, date, calories_in, calories_out, mood, stress_level, hours_of_sleep, worked_out)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
        """
        result = self._connection.execute(sql, [
            wellbeing.person_id,
            wellbeing.date,
            wellbeing.calories_in,
            wellbeing.calories_out,
            wellbeing.mood,
            wellbeing.stress_level,
            wellbeing.hours_of_sleep,
            wellbeing.worked_out
        ])
        
        return result[0]["id"] if result else None
    
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM wellbeing_diary WHERE id = %s', [id])
        return None
