from decimal import Decimal
from datetime import datetime, date, timedelta

class Run:
    def __init__(self, runner_id, date_input, run_type, distance, duration, satisfaction):
        self.runner_id = runner_id
        # Ensure date_input is converted to a datetime.date object
        if isinstance(date_input, date):
            self.date = date_input
        else:
            self.date = datetime.strptime(date_input, '%Y-%m-%d').date()  # Adjust format as needed
        self.run_type = run_type
        self.distance = Decimal(distance)
        self.duration = self.convert_duration(duration)  # Store duration as timedelta
        self.satisfaction = satisfaction

    def convert_duration(self, duration):
        if isinstance(duration, str):
            # If duration is provided as a string in HH:MM:SS format
            parts = duration.split(':')
            return timedelta(hours=int(parts[0]), minutes=int(parts[1]), seconds=int(parts[2]))
        elif isinstance(duration, timedelta):
            return duration
        else:
            raise ValueError("Duration must be a string in HH:MM:SS format or a timedelta.")

    def __eq__(self, other):
        if isinstance(other, Run):
            return (
                self.runner_id == other.runner_id and
                self.date == other.date and
                self.run_type == other.run_type and
                round(self.distance, 2) == round(other.distance, 2) and
                self.duration == other.duration and  # Compare as timedelta
                self.satisfaction == other.satisfaction
            )
        return False

    def __repr__(self):
        # Format duration to HH:MM:SS
        formatted_duration = self.format_duration(self.duration)
        return f"Run({self.runner_id}, {self.date}, {self.run_type}, {self.distance}, {formatted_duration}, {self.satisfaction})"

    @staticmethod
    def format_duration(duration):
        # Format the timedelta into HH:MM:SS
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"