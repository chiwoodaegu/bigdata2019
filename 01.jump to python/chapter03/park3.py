# coding: cp949

age=input("���̸� �Է��ϼ���:")

if age>=0 and age<4: 
    print("���ϴ� ���Ƶ���̸� ����� 0�� �Դϴ�")
elif age>=4 and age<14: 
    print("���ϴ� ��̵���̸� ����� 2000�� �Դϴ�") 
elif age>=14 and age<=19: 
    print("���ϴ� û�ҳ����̸� ����� 3000�� �Դϴ�")
elif age>=19 and age<=66: 
    print("���ϴ� ���ε���̸� ����� 5000�� �Դϴ�")
elif age>=66: 
    print("���ϴ� ���ε���̸� ����� 0�� �Դϴ�")

elif age<=0:
    print("�ٽ� �Է��ϼ���")
    exit()


