class Report:
    def __init__(self, analyzer_obj, user_obj):
        self.results = analyzer_obj [cite: 96]
        self.user = user_obj

    def generate_report(self): [cite: 98, 149]
        print(f"\n--- Report for {self.user.username} ---")
        # Conditional Logic for permissions [cite: 154]
        if self.user.role == "Admin":
            print(f"Full Data: Mean={self.results.calculate_mean()}, Max={self.results.find_max()}") [cite: 150]
        else:
            print(f"Limited Data: Mean={self.results.calculate_mean()}") [cite: 150]
