"""Description:
    * author: Magdy Abdelkader
    * company: Fresh Futures/Seeka Technology
    * position: IT Intern
    * date: 02-11-20
    * description:This script extracts the corresponding courses details and tabulate it.
"""

import csv
import re
import time
from pathlib import Path
from selenium import webdriver
import bs4 as bs4
import os
import copy
from CustomMethods import TemplateData
from CustomMethods import DurationConverter as dura

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
option.add_argument("headless")
exec_path = Path(os.getcwd().replace('\\', '/'))
exec_path = exec_path.parent.__str__() + '/Libraries/Google/v86/chromedriver.exe'
browser = webdriver.Chrome(executable_path=exec_path, options=option)

# read the url from each file into a list
course_links_file_path = Path(os.getcwd().replace('\\', '/'))
course_links_file_path = course_links_file_path.__str__() + '/TAFEQ_undergrad_links.txt'
course_links_file = open(course_links_file_path, 'r')

# the csv file we'll be saving the courses to
csv_file_path = Path(os.getcwd().replace('\\', '/'))
csv_file = csv_file_path.__str__() + '/TAFEQ_courses.csv'

course_data = {'Level_Code': '', 'University': 'TAFE Queensland', 'City': '', 'Country': 'Australia',
               'Course': '', 'Int_Fees': '', 'Local_Fees': '', 'Currency': 'AUD', 'Currency_Time': 'year',
               'Duration': '', 'Duration_Time': '', 'Full_Time': '', 'Part_Time': '', 'Prerequisite_1': 'IELTS',
               'Prerequisite_2': '', 'Prerequisite_3': '', 'Prerequisite_1_grade': '5.5',
               'Prerequisite_2_grade': '',
               'Prerequisite_3_grade': '', 'Website': '', 'Course_Lang': '', 'Availability': '', 'Description': '',
               'Career_Outcomes': '', 'Online': '', 'Offline': '', 'Distance': '', 'Face_to_Face': '',
               'Blended': '', 'Remarks': ''}

possible_cities = {'rockhampton': 'Rockhampton', 'cairns': 'Cairns', 'bundaberg': 'Bundaberg',
                   'townsville': 'Townsville',
                   'online': 'Online', 'gladstone': 'Gladstone', 'mackay': 'Mackay', 'mixed': 'Online',
                   'yeppoon': 'Yeppoon',
                   'brisbane': 'Brisbane', 'sydney': 'Sydney', 'queensland': 'Queensland', 'melbourne': 'Melbourne',
                   'albany': 'Albany', 'perth': 'Perth', 'adelaide': 'Adelaide', 'noosa': 'Noosa', 'emerald': 'Emerald',
                   'hawthorn': 'Hawthorn', 'wantirna': 'Wantirna', 'prahran': 'Prahran'}

possible_languages = {'Japanese': 'Japanese', 'French': 'French', 'Italian': 'Italian', 'Korean': 'Korean',
                      'Indonesian': 'Indonesian', 'Chinese': 'Chinese', 'Spanish': 'Spanish'}

course_data_all = []
level_key = TemplateData.level_key  # dictionary of course levels
faculty_key = TemplateData.faculty_key  # dictionary of course levels

# GET EACH COURSE LINK
for each_url in course_links_file:
    actual_cities = []
    remarks_list = []
    browser.get(each_url)
    pure_url = each_url.strip()
    each_url = browser.page_source

    soup = bs4.BeautifulSoup(each_url, 'lxml')
    time.sleep(1)

    # SAVE COURSE URL
    course_data['Website'] = pure_url

    # SAVE COURSE TITLE
    title = soup.find('h1', class_='tq-internal-banner__caption--title')
    if title:
        course_data['Course'] = title.get_text().strip()
        print('COURSE TITLE: ', title.get_text().strip())

    # DECIDE THE LEVEL CODE
    for i in level_key:
        for j in level_key[i]:
            if j in course_data['Course']:
                course_data['Level_Code'] = i
    print('COURSE LEVEL CODE: ', course_data['Level_Code'])

    # DECIDE THE FACULTY
    for i in faculty_key:
        for j in faculty_key[i]:
            if j.lower() in course_data['Course'].lower():
                course_data['Faculty'] = i
    print('COURSE FACULTY: ', course_data['Faculty'])

    # COURSE LANGUAGE
    for language in possible_languages:
        if language in course_data['Course']:
            course_data['Course_Lang'] = language
        else:
            course_data['Course_Lang'] = 'English'
    print('COURSE LANGUAGE: ', course_data['Course_Lang'])

    # COURSE DESCRIPTION
    description = soup.find('div', class_='tq-introduction')
    if description:
        description_p = description.find('p')
        if description_p:
            course_data['Description'] = description_p.get_text().strip()
        print('COURSE DESCRIPTION: ', course_data['Description'])

    # DURATION & DURATION_TIME / PART-TIME & FULL-TIME
    duration = soup.find('td', attrs={'data-th': 'Duration'})
    work_load = soup.find('td', attrs={'data-th': 'Workload'})
    if duration:
        converted_duration = dura.convert_duration(duration.get_text().strip())
        if converted_duration is not None:
            duration_list = list(converted_duration)
            if duration_list[0] == 1 and 'Years' in duration_list[1]:
                duration_list[1] = 'Year'
            elif duration_list[0] == 1 and 'Months' in duration_list[1]:
                duration_list[1] = 'Month'
            course_data['Duration'] = duration_list[0]
            course_data['Duration_Time'] = duration_list[1]
            print('DURATION/DURATION-TIME', str(course_data['Duration']) + ' / ' + course_data['Duration_Time'])
    if work_load:
        if 'part-time' in work_load.get_text().lower() or 'part time' in work_load.get_text().lower():
            course_data['Part_Time'] = 'yes'
        else:
            course_data['Part_Time'] = 'no'
        if 'full-time' in work_load.get_text().lower() or 'full time' in work_load.get_text().lower():
            course_data['Full_Time'] = 'yes'
        else:
            course_data['Full_Time'] = 'no'
        print('FULL-TIME/PART-TIME: ', course_data['Full_Time'] + ' / ' + course_data['Part_Time'])

    # DELEVERY
    delivery = soup.find('td', attrs={'data-th': 'Study Mode'})
    course_data['Online'] = 'no'
    if delivery:
        delivery_text = delivery.get_text().lower()
        # print(delivery_text)
        if 'classroom' in delivery_text or 'recognition of prior learning' in delivery_text:
            course_data['Face_to_Face'] = 'yes'
            course_data['Offline'] = 'yes'
        else:
            course_data['Face_to_Face'] = 'no'
            course_data['Offline'] = 'no'
        if 'mixed mode' in delivery_text:
            course_data['Online'] = 'yes'
            course_data['Face_to_Face'] = 'yes'
            course_data['Offline'] = 'yes'
            course_data['Blended'] = 'yes'
        else:
            course_data['Blended'] = 'no'
        if 'mobile' in delivery_text:
            course_data['Distance'] = 'yes'
        else:
            course_data['Distance'] = 'no'
    else:
        course_data['Online'] = 'yes'
    print('DELIVERY: online: ' + course_data['Online'] + ' offline: ' + course_data['Offline'] + ' face to face: ' +
          course_data['Face_to_Face'] + ' blended: ' + course_data['Blended'] + ' distance: ' +
          course_data['Distance'])

    # AVAILABILITY
    heading_list = soup.find_all('div', class_='tq-accordion-item__heading')
    if heading_list:
        avi_list = []
        for element in heading_list:
            avi_list.append(element.get_text().strip().lower())
        avi_list = ' '.join(avi_list)
        if 'by location' in avi_list:
            course_data['Availability'] = 'D'
        if 'international students' in avi_list:
            course_data['Availability'] = 'I'
        if 'by location' in avi_list and 'international students' in avi_list:
            course_data['Availability'] = 'A'
    print('AVAILABILITY: ' + course_data['Availability'])

    # CITY
    city_list = soup.find_all('a', class_='r-tabs-anchor')
    if city_list:
        temp_cities = []
        for city in city_list:
            temp_cities.append(city.get_text().strip().lower())
        temp_cities = ' '.join(temp_cities)
        print(temp_cities)
        if 'brisbane' in temp_cities:
            actual_cities.append('brisbane')
        if 'gold coast' in temp_cities:
            actual_cities.append('queensland')
        if 'darling downs' in temp_cities:
            actual_cities.append('queensland')
        if 'queensland' in temp_cities:
            actual_cities.append('queensland')
    else:
        actual_cities.append('online')
    print('CITY: ', actual_cities)

    # FEES
    fee_header = soup.find_all('td', attrs={'data-th': 'Cost'})
    if fee_header:
        course_data['Int_Fees'] = ''
        course_data['Local_Fees'] = ''
        for element in fee_header:
            fee_text = element.get_text().lower()
            if 'international' in fee_text:
                int_fee = re.search(r"\d+(?:,\d+)|\d+", fee_text)
                if int_fee is not None:
                    course_data['Int_Fees'] = int_fee.group()
            else:
                loc_fee = re.search(r"\d+(?:,\d+)|\d+", fee_text)
                if loc_fee is not None:
                    course_data['Local_Fees'] = loc_fee.group()
    print('INTERNATIONAL FEE', course_data['Int_Fees'])
    print('LOCAL FEE', course_data['Local_Fees'])

    # duplicating entries with multiple cities for each city
    for i in actual_cities:
        course_data['City'] = possible_cities[i]
        course_data_all.append(copy.deepcopy(course_data))
    del actual_cities

    # TABULATE THE DATA
    desired_order_list = ['Level_Code', 'University', 'City', 'Course', 'Faculty', 'Int_Fees', 'Local_Fees',
                          'Currency', 'Currency_Time', 'Duration', 'Duration_Time', 'Full_Time', 'Part_Time',
                          'Prerequisite_1', 'Prerequisite_2', 'Prerequisite_3', 'Prerequisite_1_grade',
                          'Prerequisite_2_grade', 'Prerequisite_3_grade', 'Website', 'Course_Lang', 'Availability',
                          'Description', 'Career_Outcomes', 'Country', 'Online', 'Offline', 'Distance', 'Face_to_Face',
                          'Blended', 'Remarks']

    course_dict_keys = set().union(*(d.keys() for d in course_data_all))

    with open(csv_file, 'w', encoding='utf-8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, course_dict_keys)
        dict_writer.writeheader()
        dict_writer.writerows(course_data_all)

    with open(csv_file, 'r', encoding='utf-8') as infile, open('TAFEQ_courses_ordered.csv', 'w', encoding='utf-8',
                                                               newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=desired_order_list)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)










