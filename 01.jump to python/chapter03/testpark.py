# coding: cp949

age=input("나이를 입력하세요:")

if age>=0 and age<=3 
    grade='유아'
    fee='무료'
elif age>=4 and age<=13: 
    grade='어린이'
    fee='2000원'
elif age>=14 and age<=19: 
    grade='청소년'
    fee='3000원'
elif age>=19 and age<=66: 
    grade='성인'
    fee='5000원'
elif age>=66: 
    grade='노인'
    fee='무료'
elif age<=0:
    print("다시 입력하세요")
    exit()

if fee='무료':
    print('귀하는 %s 등급이며, 요금은 무료 입니다.'%grade)
    print('감사합니다. 티켓을 발행합니다.')   

else:
    print('귀하는 %s 등급이며, 요금은 %s 입니다.'%(grade,fee))

