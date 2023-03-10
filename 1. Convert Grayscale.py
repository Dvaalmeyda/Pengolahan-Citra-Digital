# PROGRAM KONVERSI RGB KE GRAYSCALE #

# Memanggil modul Pyhton Image Library sebagai pil dengan menggunakan Image dan ImageOps\
from PIL import Image, ImageOps

# Membuat variabel citraAsli untuk menjadi wadah gamabr yang akan dikonversi;
citraAsli = Image.open("PCD\Diva\Materi\seal.jpg")
# Melakukan konversi RGB ke Grayscale dengan fungsi ImageOps.grayscale()
citraHP = ImageOps.grayscale(citraAsli)
citraHP.save('PCD\Diva\Materi\sealGS.jpg')