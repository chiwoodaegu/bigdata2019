# coding: cp949

age=input("���̸� �Է��ϼ���:")

if age>=0 and age<=3 
    grade='����'
    fee='����'
elif age>=4 and age<=13: 
    grade='���'
    fee='2000��'
elif age>=14 and age<=19: 
    grade='û�ҳ�'
    fee='3000��'
elif age>=19 and age<=66: 
    grade='����'
    fee='5000��'
elif age>=66: 
    grade='����'
    fee='����'
elif age<=0:
    print("�ٽ� �Է��ϼ���")
    exit()

if fee='����':
    print('���ϴ� %s ����̸�, ����� ���� �Դϴ�.'%grade)
    print('�����մϴ�. Ƽ���� �����մϴ�.')   

else:
    print('���ϴ� %s ����̸�, ����� %s �Դϴ�.'%(grade,fee))

