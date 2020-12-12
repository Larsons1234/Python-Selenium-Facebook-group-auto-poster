from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

def main():
    # Set up Facebook login account name and password
    account = "email/phone number"
    password = "password"

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
    cookieselement = driver.find_element(By.XPATH, '//*[@title="Accept All"]').click()
    loginelement = driver.find_element(By.XPATH,'//*[@name="login"]').click()
    time.sleep(2)

    # Post on each group
    for group in groups_links_list:
        driver.get(group)
        time.sleep(2)
        #Attaches photos to the post
        for photo in images_list:
            photo_element = driver.find_element(By.XPATH,'//input[@type="file"]')
            photo_element.send_keys(photo)
            time.sleep(1)
        post_box = driver.find_element(By.XPATH,"/html[@id='facebook']/body[@class='_6s5d _71pn _-kb segoe']/div[@id='mount_0_0']/div/div[1]/div[@class='rq0escxv l9j0dhe7 du4w35lb']/div[4]/div/div[@class='l9j0dhe7 tkr6xdv7']/div[@class='rq0escxv l9j0dhe7 du4w35lb']/div[@class='h3gjbzrl l9j0dhe7']/div[@class='iqfcb0g7 tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']/div[@class='gs1a9yip rq0escxv j83agx80 cbu4d94t taijpn5t h3gjbzrl dflh9lhu scb9dxdr ir0402vp n7vda9r4']/div[@class='ll8tlv6m j83agx80 taijpn5t hzruof5a']/div[@class='j83agx80 cbu4d94t lzcic4wl ni8dbmo4 stjgntxs oqq733wu l9j0dhe7 du4w35lb cwj9ozl2 ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi nwpbqux9']/div[@class='dbpd2lw6 l9j0dhe7 stjgntxs ni8dbmo4 lzcic4wl idiwt2bm']/div[@class='kr520xx4 pedkr2u6 ms05siws pnx7fd3z b7h9ocf4 pmk7jnqg j9ispegn']/form/div[@class='dbpd2lw6 l9j0dhe7 stjgntxs ni8dbmo4 lzcic4wl idiwt2bm']/div[@class='kr520xx4 pedkr2u6 ms05siws pnx7fd3z b7h9ocf4 pmk7jnqg j9ispegn']/div[@class='k4urcfbm l9j0dhe7 datstx6m rq0escxv']/div[@class='l9j0dhe7']/div[@class='j83agx80 cbu4d94t f0kvp8a6 mfofr4af l9j0dhe7 oh7imozk']/div[@class='q5bimw55 rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos l9j0dhe7 du4w35lb ofs802cu pohlnb88 dkue75c7 mb9wzai9 l56l04vs r57mb794 kh7kg01d c3g1iek1 buofh1pr']/div[@class='j83agx80 cbu4d94t buofh1pr l9j0dhe7']/div[@class='o6r2urh6 buofh1pr datstx6m l9j0dhe7 oh7imozk']/div[@class='rq0escxv buofh1pr df2bnetk hv4rvrfc dati1w0a l9j0dhe7 k4urcfbm du4w35lb o0xt3n8b']/div/div[@class='gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv oo9gr5id t5a262vz jq4qci2q b1v8xokw datstx6m a3bd9o3v lzcic4wl ecm0bbzt rz4wbd8a sj5x9vvc a8nywdso k4urcfbm o8yuz56k']/div[@class='rq0escxv datstx6m k4urcfbm a8c37x1j']/div[@class='_5rp7']/div[@class='_5rpb']/div[@class='notranslate _5rpu']")
        post_box.click()
        time.sleep(1)
        post_box.send_keys(message)
        time.sleep(6)
        post_button = driver.find_element_by_xpath('//div[@aria-label="Post"]')
        clickable = False
        while not clickable:
            cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")
            if cursor == "pointer":
                clickable = True
            break
        post_button.click()
        time.sleep(10)
    # Close driver
    driver.close()

if __name__ == '__main__':
  main()
