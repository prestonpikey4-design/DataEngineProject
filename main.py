from user import User, Admin
from dataset import DataSet
from analyzer import Analyzer
from report import Report

admin = Admin("Alice")
my_data = DataSet("Student Marks")

my_data.add_data([70, 80, 90]) [cite: 125, 126]
engine = Analyzer(my_data) [cite: 127]

final_report = Report(engine, admin)
final_report.generate_report() [cite: 128]
