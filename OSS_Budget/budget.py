import datetime
from expense import Expense
from collections import defaultdict

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, user_name):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount, user_name)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def analyze_budget(self, target_amount):
        total = sum(e.amount for e in self.expenses)
        print(f"\n[지출 분석]")
        print(f"목표 지출: {target_amount}원")
        print(f"실제 지출: {total}원")

        if total == target_amount:
            print("예산을 정확히 지켰습니다! 훌륭합니다.\n")
        elif total < target_amount:
            diff = target_amount - total
            print(f"예산보다 {diff}원 적게 지출했습니다! 절제된 모습이 아름답습니다.\n")
        else:
            diff = total - target_amount
            print(f"예산보다 {diff}원 초과 지출했습니다.. 좀 더 노력하세요!\n")

    def show_statistics(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        user_totals = defaultdict(int)

        # 사용자별로 지출 금액 합산
        for expense in self.expenses:
            user_totals[expense.user_name] += expense.amount

        # 가장 많이 쓴 사람과 적게 쓴 사람 찾기
        most_spent_user = max(user_totals, key=user_totals.get)
        least_spent_user = min(user_totals, key=user_totals.get)

        print("\n[지출 통계]")
        print(f"가장 많이 쓴 사람은 {most_spent_user}님 입니다. 총 {user_totals[most_spent_user]}원을 쓰신 부자시군요?")
        print(f"가장 적게 쓴 사람은 {least_spent_user}님 입니다. 단 {user_totals[least_spent_user]}원 밖에 쓰지않은 절약왕 입니다!\n")


