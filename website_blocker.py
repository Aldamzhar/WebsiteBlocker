import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect = "Your IP address" # subject to change depending on a user 
website_lst = ["vk.com", "instagram.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 23) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 24):
        print("Working hours....")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_lst:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines() # list of lines as strings
            file.seek(0) # point the pointer at the beginning of the file
            for line in content:
                if not any(website in line for website in website_lst):
                    file.write(line)
            file.truncate() # make the text after the pointer deleted
        print("Resting Hours...")
    time.sleep(5) # every 5 seconds
