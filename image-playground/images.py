from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("sharpen.png",'png')

# filtered_img = img.convert('L')
# filtered_img.save("grey.png",'png')
# # filtered_img.show()
# # crooked = filtered_img.rotate(180)
# # crooked.save('rotate.png', 'png')

# # resize = filtered_img.resize((300, 300))
# # resize.save('resized.png', 'png')

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('croped.png', 'png')


img = Image.open('./astro.jpg')
print(img.size)
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)