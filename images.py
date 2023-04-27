from PIL import Image,ImageFilter
###BLUR
img = Image.open('./image-processing/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("./image-processing/blurpikachu.png", "png")

##grey
filtered_img2 = img.convert('L')
filtered_img2.save("./image-processing/grey.png", "png")

####crop image
box = (100, 100, 400, 400)
region = filtered_img2.crop(box)
region.save("./image-processing/crop.png", "png")


##resize
resize_img = img.resize((300, 300))
resize_img.save("./image-processing/resized.png", "png")



img2 = Image.open('./image-processing/astro.jpg')
img2.thumbnail((400, 400))
img2.save('./image-processing/thumbnail.jpg')

print(img2.size)
