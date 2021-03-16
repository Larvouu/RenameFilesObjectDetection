#importing os
import os
#importing minidom in order to modify XML files
import xml.dom.minidom as md 

folderPath       = 'Test\\'                             # mettre le path 

suffix_xml       = '.xml'
suffix_xml_upper = '.XML'

new_label        = "Entrez le nouveau label ici"        #Le label qui va être écrit à la place de l'ancien


# Function to modify XML file tag <name> xxx </name>
def modifyNameInXml(xml_file, new_name) :

    file = md.parse(xml_file) 

    old = file.getElementsByTagName("name")[ 0 ].firstChild.nodeValue

    # modifying the value of tag <name>
    file.getElementsByTagName("name")[ 0 ].firstChild.nodeValue = new_name

    # writing the changes in "file" object to  
    # the "xml_file.xml" file 
    with open(xml_file, "w" ) as fs:  
  
        fs.write( file.toxml() ) 
        fs.close()  

    #print success
    print("Maj : "+old+" --> "+new_name)

def correctionEnMasse() :

    for count, filename in enumerate(os.listdir(folderPath)): 

        if filename.endswith(suffix_xml) or filename.endswith(suffix_xml_upper) :

            modifyNameInXml(folderPath + filename, new_label)

  


# Function to rename multiple files in a folder
def main(): 
    correctionEnMasse()
    
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 