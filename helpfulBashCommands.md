Some commands for the Bash Terminal and notes for future reference

**which** _[program/tool]_
- Locates the program or tool in search of and prints out it's directory location

      Ex. which python
          which which

`echo $PATH` - shows all paths to the previous typed command

**brew search** _[toolName]_
  - Helps find certain tools and technologies that can be installed through _**brew**_
            
        Ex. brew search sql
            brew search pip


**history**
  - Provides last 500 inputs that were used in the terminal. Using the pipe method `|` you can apply `grep` to filter that data into certain commands containing the text

        Ex. history | grep pip

  **`[folder/fileName]* du -sh`** 
  - Gives the file size of the folder or file requested

        ex. ENV* du -sh
            du -sh .  // for everything in current directory
           



----
To get into `virtualenv` inside the project:
**virtualenv [envName]**

Then to activate it:
      
    . ENV/bin/activate
    OR
    source ENV/bin/activate

To get out of the environment of `virtualenv` just type `deactivate`

----
To remove a folder:
`rm -rf [folderName]`



