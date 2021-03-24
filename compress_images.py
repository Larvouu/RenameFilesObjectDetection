from PIL import Image
import PIL
import os
import glob
from pathlib import Path

folderPath       = 'bonjour_changez_moi_mis_laissez_les_slash\\'      # mettre le path 
image_quality    = 20                        # la qualité de la compression, 100 : pas de compression | 20 : grosse compression

suffix_jpg        = '.jpg'
suffix_jpg_upper  = '.JPG'
suffix_jpeg       = '.jpeg'
suffix_jpeg_upper = '.JPEG'
suffix_xml        = '.xml'
suffix_xml_upper  = '.XML'

# Function to compress images
def compressImage(image) :
    picture = Image.open(image)
    picture.save(image,optimize=True,quality=image_quality) #100 - 85 : aucune différence | 65 : max à utiliser pour que l'image reste parfaitement exploitable pareil 
    print(f"Image compressée en qualité {image_quality}")
    
# Function to compress all jpg images in a folder
def compressAllInFolder() :

    for count, filename in enumerate(os.listdir(folderPath)): 

        if filename.endswith(suffix_jpg) or filename.endswith(suffix_jpg_upper) or filename.endswith(suffix_jpeg) or filename.endswith(suffix_jpeg_upper) :

            compressImage(folderPath + filename)

# Function main
def main(): 
    compressAllInFolder()
    print("____________________________________________________________________")
    print("Toutes les images ont été compressées.")
    print("____________________________________________________________________")
    
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 