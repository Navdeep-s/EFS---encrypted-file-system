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
* Then enter the full path of a file. This file will act as a key so make sure nobody else knows about this file. This file could be any file you want but make sure to never delete this file because otherwise all the encrypted data will be lost.
* For the first time it will take some time to intialise
* Now you will se "type something" on your prompt


After this you have three types of command which you can type anytime
 * add_new : to add new content to the file system. It will prompt you with a empty directory move all the files which you want to encrypt to this 
 * show_folders
 * search
 * quit



