# coding: cp949

age=int(input("나이를 입력하세요:"))
grade=int()
fee=str()

if age>=0 and age<4 
    grade='유아'
    fee='무료'
elif age>=4 and age<14: 
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


paytype=int(input('요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드):'))

if paytype=1:
   fee=int(input('요금을 입력하세요:'))
    if pay==fee:
        print("감사합니다. 티켓을 발행합니다.")
    elif pay<fee:
        print("%d원이 모자랍니다. 입력 하신 %d원을 반환합니다."%((fee-pay),pay))
    else:
        print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환 합니다."%(pay-fee))
elif paytype=2:
    print('%s원 결제 되었습니다. 티켓을 발행합니다.'%(fee*0.9))
elif paytype=2 and age<60:
    print('%s원 결제 되었습니다. 티켓을 발행합니다.'%((fee*0.9)*0.95))

else: print("감사합니다. 티켓을 발행합니다.")

if 

free

freeticket =-1

    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료티켓을 발행합니다. 잔여 무료티켓 %d장"%d freeticket)

dcticket =-1

else:
    print("축하합니다. 연간회원권 구매 이벤트에 당첨되었습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장"%d dcticket)

