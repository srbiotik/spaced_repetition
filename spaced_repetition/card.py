import datetime

class Card:
    def __init__(self, repetitions=0, interval=1.0, ease_factor=2.5, due_time=None):
        self.repetitions = repetitions
        self.interval = interval
        self.ease_factor = ease_factor
        if due_time is not None:
            self.due_time = due_time

    def update(self, grade):
        if grade >= 3:
            if self.repetitions == 0:
                self.interval = 1
            elif self.repetitions == 1:
                self.interval = 6
            else:
                self.interval *= self.ease_factor

            self.repetitions += 1
        else:
            self.repetitions = 0
            self.interval = 1

        self.ease_factor = max(1.3, self.ease_factor + 0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02))

        # Convert interval to next due time
        current_time = datetime.datetime.now()
        self.due_time = current_time + datetime.timedelta(days=self.interval)

    def is_due(self):
        current_time = datetime.datetime.now()
        return self.due_time <= current_time
