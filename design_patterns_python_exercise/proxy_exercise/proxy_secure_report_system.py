import time


class Report:
    def read(self):
        print("Loading report...")
        time.sleep(3)
        print("Top SECRET Financial Data")


class ReportProxy:
    def __init__(self, user):
        self.name = user["name"]
        self.role = user["role"]
        self.report = None

    def read(self):
        if self.role == "manager":
            if self.report is None:
                self.report = Report()
            return self.report.read()
        else:
            print("Access Denied")


class LoggingReportProxy:
    def __init__(self, report):
        self.report = report

    def read(self):
        print(f"[LOG] User {self.report.name} tries to access the report")
        self.report.read()


user = {"name": "John", "role": "employee"}
proxy = LoggingReportProxy(ReportProxy(user))

# proxy.read()
# Output:
# [LOG] User John tries to access the report
# Access Denied

user = {"name": "Alice", "role": "manager"}
proxy = LoggingReportProxy(ReportProxy(user))
proxy.read()
# Output:
# [LOG] User Alice tries to access the report
# Loading report...
# Report content: Top Secret Financial Data
