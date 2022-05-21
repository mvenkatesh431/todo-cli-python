import datetime

# To-do Status
(
    OPEN,
    COMPLETED,
) = range(2)


class Todo:
    def __init__(self, name, category, priority, status=None, position=None, 
      creation_time=None, completion_time=None):
        self.name = name
        self.category = category
        self.priority = priority
        self.status = status if status is not None else OPEN
        self.position = position if position is not None else None 
        self.creation_time = creation_time if creation_time is not None else datetime.datetime.now().isoformat()
        self.completion_time = completion_time if completion_time is not None else None
        
    def __repr__(self)->str:
        return f"Name:{self.name}, Category:{self.category}, Priority:{self.priority}, " \
            f"Status: {self.status}, Position:{self.position}, Creation_time:{self.creation_time}, " \
            f"Completion_time:{self.completion_time}"

