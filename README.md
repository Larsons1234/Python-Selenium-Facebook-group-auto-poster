# Python-Selenium-Facebook-group-auto-poster
A Python script use Selenium to achieve automatically posting images with text on multiple Facebook groups that you are the member of but if you aren't it will join the group instead.

Setup
----------
 - You need to [disable 2 factor authetnication](https://www.alphr.com/facebook/1006409/two-factor-authentication-2FA-facebook) on Facebook for this to work
 - First of all, install [Python 3](https://www.python.org/downloads/) into your machine
 
 - Then insall selenium:
   ```
   pip install selenium
   ```
 - You also need to install JSON for the TKinter/GUI version
   ```
   pip install json
   ```
 - Download the [Chrome Driver](http://chromedriver.chromium.org/downloads), which matches your [version of Google Chrome](https://www.businessinsider.com/what-version-of-google-chrome-do-i-have), and place it in the same directory with the script.
 
Configure the script
----------
You need to edit the script to provide your Facebook account name and password, the message you want to post, whether you want to attach an image, along with its path and the links of the Facebook groups you are the member of:
``` 
def main():
    # Set up Facebook login account name and password
    account = "sample@gmail.com"
    password = "sample"

    # Set up Facebook groups to post, you must be a member of the group
    groups_links_list = [
        "https://www.facebook.com/groups/sample1", "https://www.facebook.com/groups/sample2"
    ]

    # Set up text content to post
    message = "Checkout an amazing selenium script for posting automaticaaly on Facebook groups! https://github.com/ethanXWL/Python-Selenium-Facebook-group-poster"

    # Set up paths of images to post
    images_list = ['C:/Users/OEM/Pictures/sample1.jpg','C:/Users/OEM/Pictures/sample2.jpg']
 ```
 
After that, run the script by double click on it. Enjoy!
