## Description ##

A software to maintain highly confidential files which you wanted to protect from other people at any cost.
Basically it is a simple terminal app which will allow you to create your own virtual file system or encrypted files and in that file system only the person having this software plus the key can view those files

## How to Install ##

For windows user
* Download this whole repo on your pc
* run the install.bat file as administrator
* choose the folder where you want to install the software
* after the terminal get close manually add the path of the folder to the environment variable
* If you don't know about environment variable search on internet

For linux user 
just add the two alias in you terminal 
* alias efs="python3 path\to\ultimate.py"
* alias fast_encryption1="python3 path\to\fast_encryption.py"

make sure to name the aliases exactly the same name
If you don't know about aliases search on internet

## Usage ##

After you have perform the above step Now you can use this software as much as you want. 
* choose any empty directory on your pc
* open that directory in the terminal/cmd
* Type efs
* Then enter the full path of a file. This file will act as a key so make sure nobody else knows about this file. This file could be any file you want but make sure to never delete this file because otherwise all the encrypted data will be lost. After this everytime you want to access you saved file you will use this file as key. 
* For the first time it will take some time to intialise
* Now you will se "type something" on your prompt


After this you have four types of command which you can type anytime
 * **add_new** : to add new content to the file system. It will prompt you with a empty directory move all the files (**remember only files can be pasted into this empty folder no directories allowed**) which you want to encrypt to this folder. After moving go back to terminal/cmd and Now you have two option. Either you can add files to already existing folders in virtual file system. For that choose any number from the shown list. Intially it would only be 0. main folder there. Otherwise you can make a new directory for that just write any name you want to give to the directory. After that press enter. It will take some time for encrption. 
 
 * **show_folders** : by typing this you can see all the folder which are currently present on you efs. type the number to go inside the folder. Then it will show you all the files choose any file with the index . 
 
 * **search** : after type search you can search via any substring which your file may have. it will give you the list of the files.
 * **quit** : To quit never use ctrl+c or cross button. Always use quit as it will clean the decrypted file.

Now whenever a files is selected three options are there 
* **decrypt** : to decrypt the file
* **rename**: to rename the file 
* **delete** : to delete the file



I hope this much description is enough.
Also as you will use this thing you will get use to it.




