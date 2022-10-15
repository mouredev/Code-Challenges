
from urllib.request import urlopen
from PIL import Image
from fractions import Fraction

url1 = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'
url2 = 'https://fondosmil.com/fondo/29364.jpg'
url3 = 'https://www.teahub.io/photos/full/210-2107522_black-space-wallpapers001-star.jpg'


def read_image(url):
    try:
        image = Image.open(urlopen(url))
        return image
    except Exception:
        pass
    finally:
        pass


def get_width_height(image):
    try:
        width, height = image.size
        return width, height
    except Exception:
        pass
    finally:
        pass


def get_aspect_ratio(image):
    try:
        width, height = get_width_height(image)
        print(width, height)
        # Fracionar el el ancho / alto, y lo guardamos en una tupla
        fraction = Fraction(width, height).as_integer_ratio()
        aspect_ratio = f"{fraction[0]}:{fraction[1]}"
        print(f'El aspect ratio de la imagen es: {aspect_ratio}')
        
    except Exception:
        pass
    finally:
        pass


if __name__ == '__main__':

    image1 = read_image(url1)
    image2 = read_image(url2)
    image3 = read_image(url3)

    print(get_aspect_ratio(image1))  # 128:41
    print(get_aspect_ratio(image2))  # 16:9
    print(get_aspect_ratio(image3))  # 3:1

