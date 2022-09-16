import base64

#ython—PDF、WORD和Base64互转
def pdf_to_base64(pdf_path):
    """
        将pdf转为Base64流
    :param pdf_path: PDF文件路径
    :return:
    """
    with open(pdf_path, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())
    return encoded_string


def base64_to_pdf(base64_data, pdf_save_path):
    """
        将 base64流 转为PDF
    :param base64_data: base64流
    :param pdf_save_path: PDF保存路径
    :return:
    """
    with open(pdf_save_path, 'wb') as f:
        f.write(base64.b64decode(base64_data))


if __name__ == '__main__':
    pdf_path = "../data/pdfdemo.pdf"
    base64code = pdf_to_base64(pdf_path)
    # print(base64code)

    pdf_save_path = "../data/pdf_save.pdf"
    base64_to_pdf(base64code, pdf_save_path)

