import numpy as np
from PIL import Image
import math


# Define the bicubic interpolation kernel function
def bicubic(x, a=-0.5):
    abs_x = abs(x)
    if abs_x <= 1:
        return (a + 2) * abs_x ** 3 - (a + 3) * abs_x ** 2 + 1
    elif 1 < abs_x < 2:
        return a * abs_x ** 3 - 5 * a * abs_x ** 2 + 8 * a * abs_x - 4 * a
    return 0


def biCubic_interpolation(image_path, output_path, scale):
    img = np.array(Image.open(image_path))
    width, height, _ = img.shape
    n_width = int(width * scale)
    n_height = int(height * scale)
    n_img = np.zeros((n_width, n_height, 3))

    for k in range(3):
        for i in range(n_width):
            for j in range(n_height):
                src_x = i / scale
                src_y = j / scale
                x = math.floor(src_x)
                y = math.floor(src_y)
                x = int(x)
                y = int(y)
                u = src_x - x
                v = src_y - y
                pix = 0
                for ii in range(-1, 3):
                    for jj in range(-1, 3):
                        if 0 <= x + ii < width and 0 <= y + jj < height:
                            pix += img[x + ii, y + jj, k] * bicubic(ii - u) * bicubic(jj - v)
                n_img[i, j, k] = np.clip(pix, 0, 255)

    result_img = Image.fromarray(np.uint8(n_img))
    result_img.save(output_path)


# Example usage:
default_image_path = 'C:/Users/admin/Desktop/999.jpg'
default_output_path = 'san.jpg'
scale_factor = 2

biCubic_interpolation(default_image_path, default_output_path, scale_factor)
