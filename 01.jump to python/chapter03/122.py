# coding: cp949
feel = "ȣ��"
#feel = ""
Hit_on_count = 0

while feel and hit_on_count<10:
    Hit_on_count = Hit_on_count + 1
    print("%d�� ����Ʈ ��û�մϴ�."%Hit_on_count)
    if(hit_on_count == 10):
        print("������ ���� �ٰ� �Գ׿�.")
        break
    feel = input("���� �׳࿡ ���� ����� ������ �����? ")
    if(feel == "��ȣ��"):
        print("�׷� �ܳ��ϼ���")
        break