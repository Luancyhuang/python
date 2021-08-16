#!/usr/bin/python3
#from pptx import Presentation
#prs = Presentation() 
#title_slide_layout = prs.slide_layouts[0]
#slide = prs.slide.add_slide(title_slede_layout)
#title = slide.shape.title
#subtitle = slide.placeholders[1]
#tile.txt = "hello,python!"
#subtitle.txt = "python-pptx was here!"
#prs.save('test.pptx')   
#Import Library 
from PIL import Image
import qrcode 
#Generate QR Code
img = qrcode.make('大笨蛋,❤️❤️ ')
img.save('七夕快乐.png')

#qr = qrcode.QRCode
#( 
#    version = 1,
#    error_correction = qrcode.constants.ERROR_CORRECT_L,
#    box_size = 10,
#    border = 4,
#)        
#
#qr.add_data("http://abhijithchandrads.medium.com/")
#qr.make(fit True)
#img = qr.make_image(fill_color="red",back_color = "black")
#img.save(medium.png)
