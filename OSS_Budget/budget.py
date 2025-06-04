import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
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

    def convert_currency(self, currency):
            total_krw = sum(e.amount for e in self.expenses)
            # 2025.06.04 기준 환율 적용
            rates = {
                'USD': 0.00074,  # 달러
                'JPY': 0.12,     # 엔화
                'CNY': 0.0054    # 위안
                    }

            currency_names = {
                'USD': '달러',
                'JPY': '엔화',
                'CNY': '위안'
                }

            if currency not in rates:
               print("지원하지 않는 통화입니다.\n")
               return

            converted = total_krw * rates[currency]
            print(f"\n총 지출: {total_krw}원")
            print(f"→ {currency_names[currency]} 기준 환산: {converted:.2f} {currency}\n")




