from datetime import timedelta

class Run:
    def __init__(self, id, person_id, date, run_type, distance, duration, satisfaction):
        self.id = id 
        self.person_id = person_id
        self.date = date
        self.run_type = run_type
        self.distance = distance
        self.satisfaction = satisfaction

        # Convert duration from string to timedelta
        if isinstance(duration, str):
            hours, minutes, seconds = map(int, duration.split(':'))
            self.duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        else:
            self.duration = duration

    @staticmethod
    def format_duration(duration):
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'{hours:02}:{minutes:02}:{seconds:02}'

    def __repr__(self):
        formatted_duration = self.format_duration(self.duration)
        return f"Run({self.id}, {self.person_id}, {self.date}, {self.run_type}, {self.distance}, {formatted_duration}, {self.satisfaction})"
    
    def __eq__(self, other):
        return (
            self.id == other.id and
            self.person_id == other.person_id and
            self.date == other.date and
            self.run_type == other.run_type and
            self.distance == other.distance and
            self.duration == other.duration and
            self.satisfaction == other.satisfaction
        )