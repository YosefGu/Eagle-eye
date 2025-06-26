
class Agent():

    def __init__(self, id, code_name, real_name, location, status, missions_completed):
        self._id = id
        self._code_name = code_name
        self._real_name = real_name
        self._location = location
        self._status = status
        self._missions_completed = missions_completed
    
    def __str__(self):
        return f'ID: {self._id}, Code name: {self._code_name}, Real name: {self._real_name}, Location: {self._location}, Status: {self._status}, Missions completed: {self._missions_completed}'

    def __repr__(self):
        return f'Agent({self._id}, {self._code_name}, {self._real_name}, {self._location}, {self._status}, {self._missions_completed})'    