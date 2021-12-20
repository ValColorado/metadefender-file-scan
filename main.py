from hash_lookup import hash_lookup
from metadefender import metadefender
from os.path import exists as file_exists

def main():
#Task 1: Calculate the hash of a given file (i.e. samplefile.txt)
        hash_lookup.storeHash() #calls storehash from hash_lookup.py
        print("\nThis program will Calculate the hash all the files in the directory and return the SHA 256 hash of the file")
        while True:#checks if file exists before moving forward.
                filename = input("Enter file name: ")
                if file_exists(filename):
                        hash = hash_lookup.hashLookUp(filename)
                        print(hash) #Gives you SHA256 from file in the directory 
                        break
                else: 
                        print("file does not exist try again")
        '''
        if the file has been previously uploaded task 4 & 6 can be commented out and task 2 can be uncommented.
        '''
# #Task 2: Perform a hash lookup against metadefender.opswat.com and see if there are previously cached results for the file
        # print("\nTask 2: will perform a hash lookup against metadefender.opswat.com and see if there are previously cached results for the previously inputted")
        # metadefender.hash_lookup_API(hash)

#Task 3: If results are found, skip to step 6

#Task 4: uploads a file 
        while True: #checks if file exists before moving forward.
                filename = input("upload_file: ")
                if file_exists(filename):
                        metadefender.file_upload_API(filename) #function will upload sampletext.txt and return the file information.
                        hash = hash_lookup.hashLookUp(filename) #Gives you SHA256 from file in the directory 
                        break
                else:
                        print("file does not exist try again")

#Task 5: Repeatedly pull on the "data_id" to retrieve results.
        metadefender.file_upload_API(filename) #function will upload sampletext.txt and return the file information.
        
 #Task 6 shows the hash look up of the file
        print("Task 6: will perform a hash look up against metadefender API ")
        metadefender.hash_lookup_API(hash)
        print("If the scan_details come back empty run program again with same file name.")

main()
