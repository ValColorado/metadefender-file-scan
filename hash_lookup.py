'''
This program will scan all the files in the directory, store all the values and allow a user to look up a file just from the hash value.
Developed by: Valentina Colorado

'''
import hashlib # Secure hashes and message digests
import os #operating system interface
class hash_lookup:
    def hashfile(filename):#takes file name and looks up the hash value for it using sha256
            text = open(filename,"rb") #open the file to read in binary format. This is so no encoding is needed for hashlib to accept data.
            data = text.read() #read the content of the file and store it in string
            text.close() #close the file
            hash_value = hashlib.sha256(data).hexdigest() #get the hash of the file and convert it into hexa
            #print(hash_value)
            return hash_value

    def storeHash():#function that will store all the files in the directory with their hash values
        
        for root, dir,files in os.walk(".", topdown=False): #os function that will look at the current directory and 
            try:
                for name in files: #searches all files in current directory 
                    file_name= name #print all the names found.
                    file_hash = hash_lookup.hashfile(name) #find the hash of all the values. 
                    
                    myfile = open("hash_lookup_table.txt","r") 
                    if (file_hash in myfile.read()): #check if FILEHASH has already been written in the hash table
                        myfile.close()
                    else: #if file is not in table write file name + hash value
                        newFile = open("hash_lookup_table.txt","a+")
                        newFile.write("\n")
                        newFile.write(file_name)
                        newFile.write(" ")
                        newFile.write(file_hash)
                        newFile.close()
            except FileNotFoundError:
                continue


    def hashLookUp(filename):   
            for root, dir,files in os.walk(".", topdown=True): #os function that will look at the current directory and 
                for name in files: #searches all files in current directory 
                    file_name= name #print all the names found.
                    file_hash = hash_lookup.hashfile(name) #find the hash of all the values. 
                    myfile = open("hash_lookup_table.txt","r") 
                    if (filename in myfile.read() and filename == file_name ): #check if filename has already been written in the hash table                    print(file_name,file_hash)
                        print(file_name,"SHA 256: ",file_hash)
                        return file_hash
                    myfile.close()
