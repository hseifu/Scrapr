#!/usr/bin/python3
#--------------------------------------------
#		USAGE
# ./<this file>.py <user name> <password>
#---------------------------------------------
import time
from bs4 import BeautifulSoup
import os
import sys
from selenium import webdriver  #ensure browser-drivers are installed
#using https://github.com/mozilla/geckodriver/ for firefox

login_url = 'https://campusnet.jacobs-university.de'
browser = webdriver.Firefox()  #Open firefox browser
browser.get(login_url)

time.sleep(1)

browser.find_element_by_id("field_user").send_keys(sys.argv[1])
browser.find_element_by_id("field_pass").send_keys(sys.argv[2])
browser.find_element_by_id("logIn_btn").click()

time.sleep(5)  #login delay

browser.find_element_by_id("link000026").click()  #open Accademic Results
browser.find_element_by_id("link000030").click()  #open course Results
source = browser.page_source  #get source code from selenium
page = BeautifulSoup(source, 'lxml')

table = page.table

th = 1 #table heading

if os.path.isfile('transcript.txt'):
    os.system('cp transcript.txt backup.txt')

transcript = open('transcript.txt', 'w+')

print('-'.rjust(60, '-'))
transcript.write('-'.rjust(60, '-') + '\n')

for course in table.find_all('tr'):

    try:
        entry = course.td.next_sibling.next_sibling
        data = entry.string.rjust(43) + " " + " ".join(
            entry.next_sibling.next_sibling.string.split())
    except AttributeError:
        entry = course.th
        data = entry.string.rjust(43) + " " + " ".join(
            entry.next_sibling.next_sibling.string.split())
        transcript.write('-'.rjust(60, '-') + '\n')
        print('-'.rjust(60, '-'))

    print(data)
    transcript.write(data + '\n')

    if th:
        print('-'.rjust(60, '-'))
        transcript.write('-'.rjust(60, '-') + '\n')
        th = 0

print('-'.rjust(60, '-'))
transcript.write('-'.rjust(60, '-') + '\n')
transcript.close()
print('Updated Courses :')

#-------------------------------------------------------------------------------
#  os.system('sdiff -s transcript.txt backup.txt') OR
#  diff --changed-group-format="%<" --unchanged-group-format="" <FILE1> <FILE1>
#
#    '%<' get lines from FILE1
#
#    '%>' get lines from FILE2
#
#    '' (empty string) for removing lines from both files.
#-------------------------------------------------------------------------------

os.system(
    'diff --changed-group-format="%<" --unchanged-group-format="" transcript.txt backup.txt'
)
