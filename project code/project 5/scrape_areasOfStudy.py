from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.hamilton.edu/academics/areas-of-study').text                 # get the page
soup = BeautifulSoup(source, 'html.parser')                                                     # make it a beautiful soup object
extList = []
links = soup.find_all('a', class_="resources_link")                                             # get all a tags (departments)
depts = []
for link in links:
    depts.append(link.text)                                                                     # add text to a list of departments
exts = []
for link in links:                                                                              # link["href"] gets the actual link in that a tag
    exts.append("https://www.hamilton.edu{}".format(link["href"]))                              # get the link to that department's site 
department = input("Enter an area of study: ")                                                  # ask user for an area of study
loc = depts.index(department)                                                                   # get the link to that department
link = exts[loc]
source1 = requests.get(link).text                                                               # go to that page
soup1 = BeautifulSoup(source1, "lxml")                                                          # make it a beautiful soup object

# SAMPLING OF COURSES: IN LAB 5A
next2 = soup1.find_all("h3", class_="course_heading")
for item in next2:
    print(item.text)

# GO TO MEET OUR FACULTY & GET ALL PROFS & TITLES: COULD BE A PROJECT
next = soup1.find_all('a', class_="sub_nav_child_link")                                         # get all a tags with class "sub_nav_child_link"
new = []                                                                                        # gets all links in RHS menu on this page
links2 = []
for item in next:                                                                               # get the title of that link & the link itself
    links2.append(item["href"])
    new.append(item.text)
loc = new.index("Meet Our Faculty")                                                             # find the link to the faculty page
important_link = "{}{}".format("https://www.hamilton.edu",links2[loc])                          # format that link

new_source = requests.get(important_link).text                                                  # get that page from the link                                     
new_soup = BeautifulSoup(new_source, "lxml")                                                    # make it a beautiful soup object
profs = new_soup.find_all("h3", class_="topic_block_title")                                     # get all prof names and titles

for prof in profs:                                                                              # print out all profs
    print(prof.text)                                                                            # you could go further an go to the page for that prof, find their courses, etc.
    print()
    
