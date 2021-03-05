#Mode d'emploi :
#1 - Mettre ce script au même niveau que le dossier images
#2 - L'ouvrir avec VSC
#3 - Sur VSC aller dans Extensions, télécharger l'extension Python, de Microsoft
#4 - Mettre ce fichier en fenêtre active dans VSC, et aller dans l'onglet Run (à droite le bouton play avec un ptit insecte)
#5 - Créer un launcher.json
#6 - En bas à gauche de VSC, cliquer sur Select Python Interpreter, et sélectionner la version python (par ex. 3.7)
#7 - Run avec le path de train, puis run en modifiant [folderPath] avec le path de test


# importing os module 
import os 

folderPath   = 'images\\test\\' # mettre le path de train, run, puis mettre le path de test, run

suffix_xml          = '.xml'
suffix_xml_upper    = '.XML'

suffix_jpg          = '.jpg'
suffix_jpg_upper    = '.JPG'

suffix_jpeg         = '.jpeg'
suffix_jpeg_upper   = '.JPEG'

prefix_img          = "species_img_" #Le préfixe des images


  
# Function to rename multiple files in a folder
def main(): 
  
    for count, filename in enumerate(os.listdir(folderPath)): 

        dst = " "
        #if file is a .jpg or .JPG
        if  filename.endswith(suffix_jpg) :
            dst = prefix_img    + str(count) + suffix_jpg
        elif filename.endswith(suffix_jpg_upper) : 
            dst = prefix_img    + str(count) + suffix_jpg_upper
        #if file is a .jpeg or .JPEG
        elif filename.endswith(suffix_jpeg) :
            dst = prefix_img    + str(count) + suffix_jpeg
        elif filename.endswith(suffix_jpeg_upper) : 
            dst = prefix_img    + str(count) + suffix_jpeg_upper
        #if file is a .xml or .XML
        elif filename.endswith(suffix_xml) or filename.endswith(suffix_xml_upper) :
            count = count-1
            dst   = prefix_img    + str(count) + suffix_xml

        src = folderPath + filename 
        dst = folderPath + dst 
          
        if not filename.endswith('.gitkeep') :
            os.rename(src, dst) 
            print(src + '  -->  ' + dst)
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 