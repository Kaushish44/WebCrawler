'''
Created on 22-Feb-2018

@author: Aditya Kaushish
'''
import os

#Creating directory for the Web site crawled
def create_dir(project_name):
    if not os.path.exists(project_name):
        print("Creating Directory " + project_name + "...")
        os.makedirs(project_name)
        
#create Wait and Complete list files
def create_files(project_name, base_url, QUEUE_FILE, CRAWLED_FILE): 
    queue = QUEUE_FILE
    crawled = CRAWLED_FILE
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Write file 
def write_file(path, data):
    f = open(path,'w')
    f.write(data + '\n')
    f.close

#Append file
def add_to_file(path,data):
    with open(path, 'a') as f:
        f.write(data + '\n')
        
#Delete file
def delete_file_contents(path):
    with open(path, 'w'):
        pass
    
#Extracting file into sets
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#Writing sets to file
def set_to_file(links, file):
    for link in sorted(links):
        add_to_file(file, link)