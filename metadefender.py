'''
This file handles all the API request.
'''
import requests #pacakge to connect to the api.
import json

from hash_lookup import hash_lookup

API_KEY = "{API}"

class metadefender:

    def hash_lookup_API(hash):
        url_hash = "https://api.metadefender.com/v4/hash/"+hash

        url = url_hash
        headers = {
        "apikey": API_KEY,
        }
        response = requests.request("GET", url, headers=headers)
        response_json = response.json()

        print("file_name: ",response_json['file_info']['display_name']) #print out the file name 
        scan_results =  response_json['scan_results']['scan_details'] #print out scan results from all the engines
        scan_results = json.dumps(scan_results,indent=2) #format the scan details
        print(scan_results)



    def file_upload_API(filename):
        
        url = "https://api.metadefender.com/v4/file"
        files = {'file': open(filename,'rb')}
        headers = {
        "apikey": API_KEY,
        "filename": filename,
        }
        response = requests.request("POST", url, headers=headers,files=files)
        response_json = response.json()

        response_str = json.dumps(response_json, indent =2,sort_keys=True) #format the file upload 
       # print("filename",headers["filename"],response_str)
        
