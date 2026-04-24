class User:
    def __init__(self, username, role="Viewer"):
        self.username = username [cite: 88]
        self.role = role [cite: 89]

    def login(self): [cite: 91]
        print(f"{self.username} logged in as {self.role}.")

class Admin(User): [cite: 135]
    def __init__(self, username):
        super().__init__(username, role="Admin")
    
    def can_modify(self): [cite: 138]
        return True 
