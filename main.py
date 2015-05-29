import multiprocessing
import sys
from selenium import webdriver
import time
import os


def main():

    links = get_youtube_links()
    print links


    driver_name = 'chromedriver.exe'

    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    exe_path = os.path.join(application_path, driver_name)
    #__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    print exe_path

    chromeOptions = webdriver.ChromeOptions()
    import getpass
    username = getpass.getuser()

    if not os.path.exists('C:/Users/' + username + '/music/new'):
        os.makedirs('C:/Users/' + username + '/music/new')

    prefs = {"download.default_directory" : 'C:/Users/' + username + '/music/new'}
    chromeOptions.add_experimental_option("prefs",prefs)

    browser = webdriver.Chrome(executable_path=exe_path, chrome_options=chromeOptions)

    #browser = webdriver.Chrome(exe_path) # Get local session of firefox

    browser.get("http://www.youtube-mp3.org/") # Load page

    link_input = browser.find_element_by_id('youtube-url')
    submit_button = browser.find_element_by_id('submit')


    for link in links:
        link_input.clear()
        link_input.send_keys(link)
        submit_button.submit()
        browser.implicitly_wait(5)
        time.sleep(5)

        download_div = browser.find_element_by_id('dl_link')
        a_hrefs = download_div.find_elements_by_tag_name('a')
        for a_href in a_hrefs:
            if 'ab=' in a_href.get_attribute("href"):
                a_href.click()
                break

        time.sleep(5)




def get_youtube_links():
    with open ("songs.txt", "r") as myfile:
        data = myfile.read()
    links = data.split("\n")
    return links




if  __name__ =='__main__':
    multiprocessing.freeze_support()
    main()