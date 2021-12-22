This program will scan a file against OPSWAT metadefender.opswat.com API. Since it is costly to multi-scan a file, before the website API is used
a hash lookup using SHA 265 is performed on all files in the directory. They're all stored in hash_lookup_table.txt and only the requested file information
is printed out. 

To run this program:

Download and extract the zip folder.

Make sure request module is installed on your computer. 
To install: 
    ```pip install requests```
                or
    ```python -m pip install requests```

Once the module is installed:

    Enter your API key on line 9 of metadefender.py.
    run the file ```main.py```.
    Once program is running, try inputting the file ```sample.txt``` to show the results.




A couple things to note:
     
     Main.py will upload a file but may not show the scan results on the first run. 
     If this happens run the program again with the same file upload and the results will be displayed. 
     This program will only scan files that are in the SAME directory. 
     When running the program it is important that all the files are together. 


     
