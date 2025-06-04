from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 지출 분석")
        print("5. 지출 통계")
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
                user_name = input("이름: ")  # 사용자 이름 입력 받기
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount, user_name)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()
        
        elif choice == "4":
            try:
                target = int(input("목표 지출 금액을 입력하세요(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.analyze_budget(target)

        elif choice == "5":
            budget.show_statistics()  # 통계 보기 기능 추가

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
