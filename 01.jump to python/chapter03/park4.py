# coding: cp949

age=int(input("���̸� �Է��ϼ���:"))
grade=int()
fee=str()

if age>=0 and age<4 
    grade='����'
    fee='����'
elif age>=4 and age<14: 
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


paytype=int(input('��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ� ī��):'))

if paytype=1:
   fee=int(input('����� �Է��ϼ���:'))
    if pay==fee:
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    elif pay<fee:
        print("%d���� ���ڶ��ϴ�. �Է� �Ͻ� %d���� ��ȯ�մϴ�."%((fee-pay),pay))
    else:
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ �մϴ�."%(pay-fee))
elif paytype=2:
    print('%s�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.'%(fee*0.9))
elif paytype=2 and age<60:
    print('%s�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.'%((fee*0.9)*0.95))

else: print("�����մϴ�. Ƽ���� �����մϴ�.")

if 

free

freeticket =-1

    print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%d freeticket)

dcticket =-1

else:
    print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%d dcticket)
