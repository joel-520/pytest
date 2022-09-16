import os


def read_label_txt(data_dir):
    filenames = []
    labels = []
    with open(data_dir) as f:
        dir_labels = [line.strip().split(' ') for line in f.readlines()]
        # 一定要用strip,因为原txt文件每行后面会带‘\n‘字符；

    for filename, label in dir_labels:
        filenames.append(filename)
        labels.append(label)

    return filenames, labels


def main():
    data_dir = './creat_txt1.txt'
    image_dir, labels = read_label_txt(data_dir)
    # print('image_dir: ', image_dir[0:5])
    print('labels: ', labels[0:5])


if __name__ == '__main__':
    main()
