from PIL import Image

img = Image.open('./images/astro.jpg')

img.thumbnail((400, 400))

img.save('thumbnail.jpg')
