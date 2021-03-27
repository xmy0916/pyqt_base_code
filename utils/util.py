import cv2


def is_chinese(self, string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def img_resize(image, label):
    '''
    :param image: cv2读取的mat图片
    :param label: 显示在那个label
    :return: 返回处理后适合显示的图片
    '''
    if image is None:
        return
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    width_new = label.width()
    height_new = label.height()
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new