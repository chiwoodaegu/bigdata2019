# coding: cp949

age=input("나이를 입력하세요:")

if age>=0 and age<4: 
    print("귀하는 유아등급이며 요금은 0원 입니다")
elif age>=4 and age<14: 
    print("귀하는 어린이등급이며 요금은 2000원 입니다") 
elif age>=14 and age<=19: 
    print("귀하는 청소년등급이며 요금은 3000원 입니다")
elif age>=19 and age<=66: 
    print("귀하는 성인등급이며 요금은 5000원 입니다")
elif age>=66: 
    print("귀하는 노인등급이며 요금은 0원 입니다")

elif age<=0:
    print("다시 입력하세요")
    exit()


