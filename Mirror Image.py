from PIL import Image

img = Image.open(input("Enter Image Path:  "))
My_Mirror_Image = img.transpose(Image.FLIP_LEFT_RIGHT)
My_Mirror_Image.show()