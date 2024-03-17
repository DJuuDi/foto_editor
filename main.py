from PIL import Image, ImageFilter

with Image.open('1670041383_1-pibig-info-p-krasivii-fon-s-oblakami-pinterest-1.jpg') as original:
    pic_gray = original.convert('L')
    pic_blur = original.filter(ImageFilter.BLUR)
    pic_gray.save('bw_pic.jpg')
    pic_blur.save('blur_pic.jpg')
    pic_gray.show()