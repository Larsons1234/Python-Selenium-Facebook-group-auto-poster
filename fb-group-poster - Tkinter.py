from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from tkinter import *
import json

# Start Window
class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
    def initialize(self):
        self.geometry("250x250")

if __name__ == "__main__":
    window = Window(None)

#Stores the credentials in a json file
def storecreds():
    account = emailinput.get()
    password = passinput.get()
    login = {
        'account': account,
        'password': password
        }
    with open ("credentials.json", "w") as creds:
        json.dump(login, creds)
        creds.close()

def login(file_path):
    # Get a file object with write permission.
    file_object = open(file_path, 'r')
    global account
    global password
    # Load JSON file data to a python dict object.
    dict_object = json.load(file_object)
    if var2.get() == 1:
        account = dict_object['account']
        password = dict_object['password']
    else:
        account = emailinput.get()
        password = passinput.get()

def main():
    login("credentials.json")
    if var1.get() == 1:
        storecreds()

    # Set up Facebook groups to post, you must be a member of the group
    groups_links_list = [
        "https://www.facebook.com/groups/sample1", "https://www.facebook.com/groups/sample2"
    ]

    # Set up text content to post
    message = "Checkout an amazing selenium script for posting automatically on Facebook groups! https://github.com/ethanXWL/Python-Selenium-Facebook-group-poster"

    # Set up paths of images to post
    images_list = ['C:/Users/OEM/Pictures/sample1.jpg','C:/Users/OEM/Pictures/sample2.jpg']

    # Login Facebook
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.facebook.com')
    emailelement = driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(account)
    passelement = driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys(password)
    #Pauses the code to let the page load, adjust for slower internet connections
    time.sleep(1)
    #Accepts all cookies
    try:
        cookieselement = driver.find_element(By.XPATH, '//*[@title="Accept All"]').click()
        time.sleep(2)
    except:
        pass
    loginelement = driver.find_element(By.XPATH,'//*[@name="login"]').click()
    time.sleep(4)

    # Post on each group
    for group in groups_links_list:
        driver.get(group)
        time.sleep(4)
        #Goes onto the next group if the group is deleted
        try:
            driver.find_element(By.XPATH,'//span[text()="Visit Help Centre"]')            
        except:
            pass
        try:
            driver.find_element(By.XPATH,'//span[text()="Leave Group"]').click()
        except:
            pass
        #Clicks the join button if the user is not a member of the group
        try:
            driver.find_element_by_xpath('//span[text()="Join Group"]').click()
        except:
            pass
        #Attaches photos to the post
        for photo in images_list:
            photo_element = driver.find_element(By.XPATH,'//input[@type="file"]')
            photo_element.send_keys(photo)
            time.sleep(5)
        #Does not attach a message if it is blank
        if message != "":
        #Finds and selects the text field in the post
            post_box = driver.find_element(By.XPATH,'//form[@method]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[@role="textbox"]')
            post_box.click()
            time.sleep(2)
            post_box.send_keys(message)
            time.sleep(6)
        #Finds the button to send the post
        post_button = driver.find_element_by_xpath('//div[@aria-label="Post"]')
        clickable = False
        while not clickable:
            cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")
            if cursor == "pointer":
                clickable = True
            break
        try:
            post_button.click()
        except:
            pass
        time.sleep(10)
        
    # Close driver
    driver.close()


#TKinter/GUI
#Vars for the credentials
emailvar = StringVar()
passvar = StringVar()

#email input
Label(text="Account:").pack()
emailinput = Entry(textvariable=emailvar)
emailinput.pack()


#password input
Label(text="Password:").pack()
passinput = Entry(textvariable=passvar)
passinput.pack()

#Save login checkbutton
var1 = IntVar()
savlogckbt = Checkbutton(text="Remeber login details?", variable=var1, onvalue=1, offvalue=0)
savlogckbt.pack()

#Load login checkbutton
var2 = IntVar()
savlogckbt = Checkbutton(text="Load saved login?", variable=var2, onvalue=1, offvalue=0)
savlogckbt.pack()

#Start button
button = Button(text="Start", command=main).pack()

#Runs tkinter
window.mainloop()

