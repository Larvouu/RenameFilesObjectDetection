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
#importing minidom in order to modify XML files
import xml.dom.minidom as md 

folderPath   = 'images\\' # mettre le path de train, run, puis mettre le path de test, run

suffix_xml          = '.xml'
suffix_xml_upper    = '.XML'

suffix_jpg          = '.jpg'
suffix_jpg_upper    = '.JPG'

suffix_jpeg         = '.jpeg'
suffix_jpeg_upper   = '.JPEG'

prefix_img          = "species_img_" #Le préfixe des images

newJpgFileName      = " "

# Function to modify XML file tag <filename> xxx </filename>
def modifyFileNameInXml(xml_file, associated_filename) :

    file = md.parse(xml_file) 

    # modifying the value of a tag(here "age") 
    file.getElementsByTagName( "filename" )[ 0 ].firstChild.nodeValue = associated_filename

    # writing the changes in "file" object to  
    # the "xml_file.xml" file 
    with open(xml_file, "w" ) as fs:  
  
        fs.write( file.toxml() ) 
        fs.close()  

    #print success
    print("Fichier XML mis à jour")

def renameEnMasse() :
    for count, filename in enumerate(os.listdir(folderPath)): 

        dst            = " "
    
        #if file is a .jpg or .JPG
        if  filename.endswith(suffix_jpg) :
            dst            = prefix_img    + str(count) + suffix_jpg
            newJpgFileName = dst
        elif filename.endswith(suffix_jpg_upper) : 
            dst            = prefix_img    + str(count) + suffix_jpg_upper
            newJpgFileName = dst
        #if file is a .jpeg or .JPEG
        elif filename.endswith(suffix_jpeg) :
            dst            = prefix_img    + str(count) + suffix_jpeg
            newJpgFileName = dst
        elif filename.endswith(suffix_jpeg_upper) : 
            dst            = prefix_img    + str(count) + suffix_jpeg_upper
            newJpgFileName = dst
        #if file is a .xml or .XML
        elif filename.endswith(suffix_xml) or filename.endswith(suffix_xml_upper) :
            count          = count-1
            dst            = prefix_img    + str(count) + suffix_xml

        src = folderPath + filename 
        dst = folderPath + dst 
          
        if not filename.endswith('.gitkeep') :
            #Rename le fichier
            os.rename(src, dst) 
            print(src + '  -->  ' + dst)
            #
            if filename.endswith(suffix_xml) or filename.endswith(suffix_xml_upper) :
                modifyFileNameInXml(dst, newJpgFileName)

  


# Function to rename multiple files in a folder
def main(): 
    renameEnMasse()
    
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 