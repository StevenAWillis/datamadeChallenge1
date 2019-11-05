import csv, datetime
from datetime import timedelta

with open('legislators.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    # d = datetime.date.today()
    # print(type(d))
    # print(d)

    # x = datetime.date(2020, 5, 17)
    # fixeddate = datetime.datetime.year(1974,4,11)
    # # z = 
    # y = fixeddate 
    # print(y)


    for line in csv_reader:
        tday = datetime.date.today()
    
        y = tday 
        fourtyfive = datetime.timedelta(16435,00,00)
        date_time_str = line[27]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
        fourtyfivetest = y - date_time_obj.date()

        if fourtyfivetest <= fourtyfive:
            print("45 or younger")


        print(type(date_time_obj.date()))

        print(fourtyfivetest)

        print(fourtyfive)