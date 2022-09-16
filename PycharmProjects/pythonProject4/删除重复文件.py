# -*- coding: cp936 -*-
import hashlib
import os
import time


def getmd5(filename):
    """
    ��ȡ�ļ� md5 ��
    :param filename: �ļ�·��
    :return: �ļ� md5 ��
    """
    file_txt = open(filename, 'rb').read()
    # ����һ��md5����
    m = hashlib.md5(file_txt)
    # hexdigest()��������ȡժҪ�����ܽ����
    return m.hexdigest()


def main():
    # �ļ���·��
    path = input("path: ")
    # ��Ϊ�ļ���С, ֵΪ�б��ļ�·����md5��
    all_size = {}
    total_file = 0
    total_delete = 0
    # ��ʼʱ��
    start = time.time()
    # �����ļ����µ������ļ�
    for file in os.listdir(path):
        # �ļ������� 1
        total_file += 1
        # �ļ���·��
        real_path = os.path.join(path, file)
        # �ж��ļ��Ƿ����ļ�
        if os.path.isfile(real_path) == True:
            # ��ȡ�ļ���С
            size = os.stat(real_path).st_size
            # md5(Ĭ��Ϊ��)
            size_and_md5 = [""]
            # ����ļ���С�Ѵ���
            if size in all_size.keys():
                # ��ȡ�ļ���md5��
                new_md5 = getmd5(real_path)
                # ��С��ͬ��md5 Ϊ�գ����md5
                if all_size[size][0] == "":
                    all_size[size][0] = new_md5
                # md5 �Ѵ��ڣ�ɾ��
                if new_md5 in all_size[size]:
                    print('ɾ��', real_path)
                    # os.remove(real_path)
                    total_delete += 1
                else:
                    # md5 �����ڣ��������
                    all_size[size].append(new_md5)
            else:
                # ����ļ���С�����ڣ��򽫴��ļ���С��ӵ� all_size �ֵ���
                all_size[size] = size_and_md5
    # ����ʱ��
    end = time.time()
    time_last = end - start
    print('�ļ�������', total_file)
    print('ɾ��������', total_delete)
    print('��ʱ��', time_last, '��')


if __name__ == '__main__':
    main()
