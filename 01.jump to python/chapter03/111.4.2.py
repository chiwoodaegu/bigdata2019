# coding: cp949
is_cash=0
is_card=1

if is_cash+is_card: # 조건식을 사용한 경우
    print("유효한 결제 수단이 있습니다.")
print("택시를 타고 가세요.")
# 해당 프로그램은 결함은 없으나
# 의미상 7번 라인은 5번 라인 if문 statement block에서 처리가 되어야 하므로
# is_cash, is_card가 0인 경우에는 오동작을 하게 된다.
# 따라서 7번 라인도 6번라인과 동일한 indentation을 맞추어야 한다.
