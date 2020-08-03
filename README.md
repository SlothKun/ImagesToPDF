# ImagesToPDF
/!\ The script is written in Python 3.6 and require PIL to work /!\

The whole point of this program is to make a pdf file of your images
It can make a pdf of one image or multiple.

HOW IT WORKS : 
Create a folder of images you want to convert while following the following structure :
  If you want to convert only one file :
    Put the concerned file in the folder
  If you want to convert multiple files :
    Put all concerned files in a folder with the name you want the pdf file to have
    
Then, open the script and give him the path of the folder, and it'll convert every file (images only !) in the folder into a pdf and put them in an PDF_Output folder

example : 

i created a folder "to_convert" in the path : "C:/User/UserName/Desktop"
the folder have to following structure :

to_convert

    |_ Diapositives
        |_ Diap1.png
        |_ Diap2.png
        |_ Diap3.png
        |_ Diap4.png
        
    |_ PlasticLoveImagePartition\n
        |_ Partition1.jpeg
        |_ Partition2.jpeg
        |_ Partition3.jpeg
    |_ dog.jpeg
    |_ CuteSloth.png

The full path is : "C:/User/UserName/Desktop/to_convert"
I give it to the script when asked and the following structure will be created at "C:/User/UserName/Desktop/"

PDF_Output

    |_ Diapositives
        |_ Diapositives.pdf   <- contain Diap1.png, Diap2.png, Diap3.png, Diap4.png
    |_ PlasticLoveImagePartition
        |_ PlasticLoveImagePartition.pdf <- contain Partition1.jpeg, Partition2.jpeg, Partition3.jpeg
    |_ dog.pdf
    |_ CuteSloth.pdf
