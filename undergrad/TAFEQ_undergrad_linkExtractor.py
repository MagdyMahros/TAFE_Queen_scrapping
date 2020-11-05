"""Description:
    * author: Magdy Abdelkader
    * company: Fresh Futures/Seeka Technology
    * position: IT Intern
    * date: 03-11-20
    * description:This script extracts all the courses links and save it in txt file.
"""
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
option.add_argument("headless")
exec_path = Path(os.getcwd().replace('\\', '/'))
exec_path = exec_path.parent.__str__() + '/Libraries/Google/v86/chromedriver.exe'
browser = webdriver.Chrome(executable_path=exec_path, options=option)

# MAIN ROUTINE
courses_page_url = 'https://tafeqld.edu.au/search-results.html?qualification=Bachelor+Degree'
list_of_links = []
browser.get(courses_page_url)
delay_ = 10  # seconds

# CLICK THE LOCATION FILTER
try:
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="search-results-filter"]/div[1]/div[1]/h4/a'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-location"]/div/ul/li[1]/label'))))
except NoSuchElementException:
    print('location NoSuchElement')
    pass

# CLICK THE WAYS TO STUDY FILTER
try:
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="search-results-filter"]/div[2]/div[1]/h4/a'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-ways_to_study"]/div/ul/li[1]/label'))))
except NoSuchElementException:
    print('ways to study NoSuchElement')
    pass

# CLICK THE STUDY AREA FILTER
try:
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="search-results-filter"]/div[3]/div[1]/h4/a'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-study_area_group"]/div/ul/li[1]/label'))))
except NoSuchElementException:
    print('study area NoSuchElement')
    pass

# CLICK THE STUDY MODE FILTER
try:
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="search-results-filter"]/div[4]/div[1]/h4/a'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-study_mode"]/div/ul/li[1]/label'))))
except NoSuchElementException:
    print('study mode NoSuchElement')
    pass

# CLICK THE WORK LOAD FILTER
try:
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="search-results-filter"]/div[5]/div[1]/h4/a'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-workload"]/div/ul/li[1]/label'))))
except NoSuchElementException:
    print('work load NoSuchElement')
    pass

# CLICK THE QUALIFICATION FILTER
try:
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="search-results-filter"]/div[6]/div[1]/h4/a'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[3]/label'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[5]/label'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[6]/label'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[7]/label'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[8]/label'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[11]/label'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[13]/label'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[14]/label'))))

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="filter-qualification"]/div/ul/li[15]/label'))))
except NoSuchElementException:
    print('work load NoSuchElement')
    pass

# CLICK THE FILTER BUTTON
try:
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="searchResults"]/section/div/div[2]/div[2]/div[1]/form/div[3]/input[2]'))))
except NoSuchElementException:
    print('filter button NoSuchElement')
    pass

# KEEP CLICKING UNTIL THERE IS NO BUTTON
condition = True
while len(list_of_links) <= 356:
    # EXTRACT ALL THE LINKS FROM EACH PAGE TO LIST
    result_elements = browser.find_elements_by_css_selector('div.tq-search-result__link > a')
    for element in result_elements:
        link = element.get_property('href')
        list_of_links.append(link)
    try:
        browser.execute_script("arguments[0].click();", WebDriverWait(browser, delay_).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.page-item.next > a'))))
        time.sleep(2)
    except NoSuchElementException:
        print('Next button "NoSuchElementException"')
# SAVE TO FILE
course_links_file_path = os.getcwd().replace('\\', '/') + '/TAFEQ_undergrad_links.txt'
course_links_file = open(course_links_file_path, 'w')
for link in list_of_links:
    if link is not None and link != "" and link != "\n":
        if link == list_of_links[-1]:
            course_links_file.write(link.strip())
        else:
            course_links_file.write(link.strip() + '\n')
course_links_file.close()



