from PIL import Image

image = Image.open('example.jpg')
(red, green, blue) = image.split()
coordinates1 = (100, 0, image.width, image.height)
coordinates2 = (50, 0, image.width - 50, image.height)
coordinates3 = (0, 0, image.width - 100, image.height)
blend_red_example = Image.blend(red.crop(coordinates1), red.crop(coordinates2), 0.5)
green_example = green.crop(coordinates2)
blend_blue_example = Image.blend(blue.crop(coordinates3), blue.crop(coordinates2), 0.5)
format_exaple = Image.merge('RGB', (blend_red_example, green_example, blend_blue_example))
format_exaple.save('format_example.jpg')
format_exaple.thumbnail((80, 80))
format_exaple.save('small_format_example.jpg')
