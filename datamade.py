import csv, datetime 
from datetime import timedelta

def csv_data():
    csv_object = {} #variable will ensure that data from the csv file is held in an object
    list_of_csv_objects = [] #variable holds all objects as list items
    with open('legislators.csv','r') as csv_file: 
        csv_object = csv.DictReader(csv_file) #DictReader reads first line of the CSV and using each comma separated value in every line a dictionary key.

        for line in csv_object:
            new_object = {}
            new_object.update(line)
            list_of_csv_objects.append(new_object)
    
    return list_of_csv_objects

def filter_age_45():
    list_of_people = csv_data() #gives me list of people as objects


    younger_than_45_list = []
    for person in list_of_people:
        tday = datetime.date.today()
        fourtyfive = datetime.timedelta(16435,00,00)
        date_time_str = person['birthdate']
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
        calculation_of_age = tday - date_time_obj.date()

        if calculation_of_age < fourtyfive:
            younger_than_45_list.append(person)

    return younger_than_45_list

def filter_republicans_social_media():
    list_of_people = csv_data() #gives me list of people as objects

    social_republicans_list = []
    for person in list_of_people:

        if person['party'] == 'R' and person['twitter_id'] != '' and person['youtube_url'] != '':
            social_republicans_list.append(person)
    return social_republicans_list
filter_republicans_social_media()

def write_to_new_csv_file():
    younger_than_45_list = filter_age_45()
    csv_headers = younger_than_45_list[0].keys()
    csv_headers_list = []

    for header_name in csv_headers:
        csv_headers_list.append(header_name)

    with open('45younger.csv','w')as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames = csv_headers_list)
        csv_writer.writeheader()

        for person in younger_than_45_list:
            csv_writer.writerow(person)


def write_to_new_csv_file2():
    republicans_socialmedia_list = filter_republicans_social_media()
    csv_headers = republicans_socialmedia_list[0].keys()
    csv_headers_list = []

    for header_name in csv_headers:
        csv_headers_list.append(header_name)

    with open('social_Republicans.csv','w')as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames = csv_headers_list)
        csv_writer.writeheader()

        for person in republicans_socialmedia_list:
            csv_writer.writerow(person)

def run():
    write_to_new_csv_file()
    write_to_new_csv_file2()

run()