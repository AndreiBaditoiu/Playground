from PIL import Image, ImageFilter

# img = Image.open('./pikachu.jpg')
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))

# filtered_img = img.filter(ImageFilter.BLUR)  # apply different filters to image
# filtered_img.save('blur.png', 'png')  # save the image under a different name and format.
#
# filtered_img = img.filter(ImageFilter.SMOOTH)  # apply different filters to image
# filtered_img.save('smooth.png', 'png')  # save the image under a different name and format.
#
# filtered_img = img.filter(ImageFilter.SHARPEN)  # apply different filters to image
# filtered_img.save('sharp.png', 'png')  # save the image under a different name and format.
#
# converted_img = img.convert('L')  # concert image (from colored to b/w)
# converted_img.save('grey.png', 'png')  # save new image
#
# converted_img.show()  # shows new image
# filtered_img.show()  # shows new image
#
# filtered_img.rotate(90).save('rot90.png', 'png')
#
# resize_img = img.resize((300, 300))
# resize_img.save('resize.png', 'png')

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)