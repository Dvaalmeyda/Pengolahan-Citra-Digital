# PROGRAM KONVERSI RGB KE GRAYSCALE #

# Memanggil modul Pyhton Image Library sebagai pil dengan menggunakan Image dan ImageOps\
from PIL import Image, ImageOps

# Membuat variabel citraAsli untuk menjadi wadah gamabr yang akan dikonversi;
gambar_Asli = Image.open('seal.jpg')
# Melakukan konversi RGB ke Grayscale dengan fungsi ImageOps.grayscale()
gambar_Grayscale = ImageOps.grayscale(gambar_Asli)
gambar_Grayscale.save('sealGS.jpg')
