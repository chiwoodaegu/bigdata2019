#coding: cp949

age = int(input("���̸� �Է��ϼ���:"))
fee = '����'
if age<0: 
    print("�ٽ� �Է��ϼ���")
    quit()
elif age<=3 : 
    grade='����'
elif age>=4 and age<=13: 
    fee='2000��'  
    grade='���' 
elif age>=14 and age<=18: 
    fee='3000��' 
    grade='û�ҳ�'
elif age>=19 and age<=65:
    fee='5000��' 
    grade='����'
else: 
    grade='����'

print("���ϴ� %s ����̸� ����� %s �Դϴ�."%(grade,fee))

if fee!='����':
    ifee=int(fee[:4])
    select = int(input("��� ������ �����ϼ���. (1:����, 2:���� ���� �ſ�ī��)"))

    if select==1:

            sfee = int(input("����� �Է��ϼ���:"))

            if ifee==sfee:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif ifee>sfee:
                print("%d���� ���ڶ��ϴ�. �Է� �Ͻ� %d���� ��ȯ�մϴ�."%((ifee-sfee),sfee))
            else:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ �մϴ�."%(sfee-ifee))

    elif select==2:
         dfee=ifee*0.9
         if age>=60 and age<=65: dfee*=0.95

         print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%dfee)


else: print("�����մϴ�. Ƽ���� �����մϴ�.")


if

    print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%d freeticket)

else:
    print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%d dcticket)

