#Avant d'utiliser ce code, on admet que le tag <filename> est correct ! 
#Ce code doit être placé au même niveau que le dossier qui contient les XML (pas dedans)

#importing os
import os
import xml.dom.minidom as md
from pathlib import Path

folderPath       = 'bonjour_modifiez_moi_svp_mais_gardez_les_slash\\'      # mettre le path 

suffix_xml       = '.xml'
suffix_xml_upper = '.XML'

# Function to modify XML file tag <name> xxx </name>
def modifyFolderAndPathInXml(xml_file) :

    file = md.parse(xml_file) 
    folderPathWithoutSlash = folderPath[:-1]

    # modifying the value of tag <folder>
    file.getElementsByTagName("folder")[ 0 ].firstChild.nodeValue = folderPathWithoutSlash
    # modifying the value of tag <path>
    file.getElementsByTagName("path")[ 0 ].firstChild.nodeValue = Path(xml_file).absolute()

    # writing the changes in "file" object to  
    # the "xml_file.xml" file 
    with open(xml_file, "w" ) as fs:  
    
        fs.write( file.toxml() ) 
        fs.close()  

    #print success
    print("XML mis à jour")
    

def correctionEnMasse() :

    for count, filename in enumerate(os.listdir(folderPath)): 

        if filename.endswith(suffix_xml) or filename.endswith(suffix_xml_upper) :

            modifyFolderAndPathInXml(folderPath + filename)

  
# Function to rename multiple files in a folder
def main(): 
    correctionEnMasse()
    print("____________________________________________________________________")
    print("fichier(s) mis à jour.")
    print("____________________________________________________________________")
    
    
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 