from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    emp_id: str
    shifts_worked: int = 0
    ratings: list[int] = field(default_factory=list)

    def log_shift(self, rating: int):
        self.shifts_worked += 1
        self.ratings.append(rating)

    def avg_rating(self) -> float:
        if self.shifts_worked == 0:
            return 0.0
        return sum(self.ratings) / self.shifts_worked

@dataclass
class Department:
    dept_name: str
    manager: str
    headcount: int
    employees: list[Employee] = field(default_factory=list)
    staff_count: int = field(init=False)

    def __post_init__(self):
        self.staff_count = len(self.employees)

    def hire(self, employee: Employee) -> bool:
        if self.staff_count >= self.headcount:
            return False
        self.employees.append(employee)
        self.staff_count = len(self.employees)
        return True

    def star_employee(self) -> str:
        if self.staff_count == 0:
            return "No data"

        best_employee = None
        best_avg = 0.0

        for employee in self.employees:
            current_avg = employee.avg_rating()
            if current_avg > best_avg:
                best_avg = current_avg
                best_employee = employee

        if best_employee is None:
            return "No data"
        return best_employee.name

    def dept_stats(self) -> str:
        lines = f"{self.dept_name} ({self.manager}):\n"
        for employee in self.employees:
            lines += f"  {employee.name} - {employee.shifts_worked} shifts, avg {employee.avg_rating():.1f} rating\n"
        lines += f"Staff: {self.staff_count}/{self.headcount}"
        return lines

e1 = Employee("Maya", "E201")
e2 = Employee("Ryan", "E202")
e3 = Employee("Zara", "E203")

e1.log_shift(4)
e1.log_shift(5)
e1.log_shift(3)
e2.log_shift(5)
e2.log_shift(5)
e3.log_shift(2)

d = Department("Engineering", "Dr. Patel", 3)
print(d.hire(e1))
print(d.hire(e2))
print(d.hire(e3))
print(d.hire(Employee("Leo", "E204")))
print(d.staff_count)
print(d.star_employee())
print(d.dept_stats())