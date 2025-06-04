
class Expense:
    def __init__(self, date, category, description, amount, user_name):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.user_name = user_name  # 사용자 이름 추가

    def __str__(self):
        return f"{self.date} | {self.category} | {self.description} | {self.amount}원 | {self.user_name}"