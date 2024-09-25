from decimal import Decimal
from datetime import datetime, date

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
        self.duration = duration
        self.satisfaction = satisfaction

    def __eq__(self, other):
        if isinstance(other, Run):
            return (
                self.runner_id == other.runner_id and
                self.date == other.date and
                self.run_type == other.run_type and
                round(self.distance, 2) == round(other.distance, 2) and
                self.duration == other.duration and
                self.satisfaction == other.satisfaction
            )
        return False

    def __repr__(self):
        return f"Run({self.runner_id}, {self.date}, {self.run_type}, {self.distance}, {self.duration}, {self.satisfaction})"
