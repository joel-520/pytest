#Word转Base64

import base64


def word_to_base64(word_path):
    """
        将word转为Base64流
    :param word_path: Word文件路径
    :return:
    """
    with open(word_path, "rb") as word_file:
        encoded_string = base64.b64encode(word_file.read())
    return encoded_string


def base64_to_word(base64_data, word_save_path):
    """
        将 base64流 转为 Word
    :param base64_data: base64流
    :param word_save_path: Word保存路径
    :return:
    """
    with open(word_save_path, 'wb') as f:
        f.write(base64.b64decode(base64_data))


if __name__ == '__main__':
    file_path = "xxxx.docx"
    base64code = word_to_base64(file_path)
    print(base64code)

    word_save_path = "xxxx.docx"
    base64_to_word(base64code, word_save_path)



