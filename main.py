# This is a sample Python script.
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print("Welcome to the Social Media HTML Generator for the LSUHSC HDC website!!!")
    print("This application will generate the code for the Facebook and LinkedIn icons with the link destination URLs you specify.")
    print("Add this code to the left page widget area of any page that uses the content management system.")
    print("")
    # Use a breakpoint in the code line below to debug your script.
    with open("social_base.html", encoding="utf-8") as social_base:
        social_base_soup = BeautifulSoup(social_base, features="html.parser")
        facebook_url = input("Enter the Facebook URL, or leave blank if the project has no Facebook page: ")
        facebook_icon = social_base_soup.find(id="facebook-icon")
        if (facebook_url):
            facebook_icon["alt"] = input("Enter alternative text for Facebook icon: ")
            facebook_icon.parent["href"] = facebook_url
        else:
            facebook_icon.find_parent(class_="social-media-icon").decompose()
        instagram_url = input("Enter the Instagram URL, or leave blank if the project has no Instagram page: ")
        instagram_icon = social_base_soup.find(id="instagram-icon")
        if (instagram_url):
            instagram_icon["alt"] = input("Enter alternative text for Instagram icon: ")
            instagram_icon.parent["href"] = instagram_url
        else:
            instagram_icon.find_parent(class_="social-media-icon").decompose()
        linkedin_url = input("Enter the LinkedIn URL, or leave blank if the project has no LinkedIn page: ")
        linkedin_icon = social_base_soup.find(id="linkedin-icon")
        if (linkedin_url):
            linkedin_icon["alt"] = input("Enter alternative text for LinkedIn icon: ")
            linkedin_icon.parent["href"] = linkedin_url
        else:
            linkedin_icon.find_parent(class_="social-media-icon").decompose()
        social_media_div = social_base_soup.find("div", id="social-media-container")
        social_media_div.smooth()
        for string in social_media_div.descendants:
            if type(string) == NavigableString and re.match("^(?:\r?\n){2,}$", str(string)):
                string.replaceWith("\r\n")
        social_media_div["class"] = social_media_div["id"]
        del social_media_div["id"]
        social_base_soup.find("h3").string = input("Enter social media heading: ")
        print("")
        print("Result:")
        print("")
        print(str(social_base_soup.find("h3")))
        print(str(social_media_div))

        # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
