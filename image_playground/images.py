from PIL import Image

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.convert('L')

crooked = filtered_img.rotate(90)
crooked.save("./images/gray.png", 'png')

crooked.show()
