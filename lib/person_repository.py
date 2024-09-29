from lib.person import Person  

class PersonRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM personal_info")
        return [
            Person(
                row["id"],  
                row["first_name"],
                row["last_name"],
                row["height"],
                row["weight"],
                row["sex"],
                row["age"],
                row["fitness_level"],
                row["activity_level"],
            ) for row in rows
        ]
    
    def create(self, person):
        self._connection.execute('INSERT INTO personal_info (id, first_name, last_name, height, weight, sex, age, fitness_level, activity_level) VALUES ( %s, %s, %s,  %s,  %s,  %s,  %s,  %s,  %s)', [
            person.id, person.first_name, person.last_name, person.height, person.weight, person.sex, person.age, person.fitness_level, person.activity_level])
        return None
    
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM personal_info WHERE id = %s', [id])
        return None
