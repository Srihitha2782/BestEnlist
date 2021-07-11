# Read a jpeg image and print the image file
from PIL import Image 
img = Image.open("study.jpg")
print(img.format)

import matplotlib.pyplot as plt
plt.imshow(img)

# merge two pdf files using python script
import PyPDF2
pdf1File = open('100 Python Interview Questions.pdf', 'rb')
pdf2File = open('Python Cheatsheet.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
pdf3 = open("MergedFiles.pdf",'rb')
pdf3Reader = PyPDF2.PdfFileReader(pdf3)
print(pdf3Reader)
pdf3.close()

#Scrape a website and store the data into DB
import requests
import MySQLdb
from bs4 import BeautifulSoup

#SQL connection data to connect and save the data
HOST = "localhost"
USERNAME = "scraping_user"
PASSWORD = ""
DATABASE = "scraping_sample"

#URL to be scraped
url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")

name_of_class = soup.h3.text.strip()
basic_data_table = soup.find("table", {"summary": "Basic data for the event"}):
basic_data_cells = basic_data_table.findAll('td')

type_of_course = basic_data_cells[0].text.strip()
lecturer = basic_data_cells[1].text.strip()
number = basic_data_cells[2].text.strip()
short_text = basic_data_cells[3].text.strip()
choice_term = basic_data_cells[4].text.strip()
hours_per_week_in_term = basic_data_cells[5].text.strip()
expected_num_of_participants = basic_data_cells[6].text.strip()
maximum_participants = basic_data_cells[7].text.strip()
assignment = basic_data_cells[8].text.strip()
lecture_id = basic_data_cells[9].text.strip()
credit_points = basic_data_cells[10].text.strip()
hyperlink = basic_data_cells[11].text.strip()
language = basic_data_cells[12].text.strip()

db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
cursor = db.cursor()
sql = "INSERT INTO classes(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_wee_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, 'NOW()')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
sql = "SELECT LAST_INSERT_ID()"
try:
    cursor.execute(sql)
    result = cursor.fetchone()
    class_id = result[0]
except:
    db.rollback()
    db.close()
    class_id = -1

dates_tables = soup.find_all("table", {"summary": "Overview of all event dates"}):
for table in dates_tables:
    for row in table.select("tr"):
        cells = row.findAll("td")
        if(len(cells)>0):
            duration = cells[0].text.split("to")
            start_date = duration[1].strip()
            end_date = duration[1].strip()
            day = cells[1].strip()
            time = cells[2].strip()
            start_time = time[0].strip()
            end_date = time[1].strip()
            frequency = cells[3].strip()
            room = cells[4].strip()
            lecturer_for_date = cells[5].strip()
            status = cells[6].strip()
            remarks = cells[7].strip()
            cancelled_on = cells[8].strip()
            max_participants = cells[9].strip()

            db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
            cursor = db.cursor()
            sql = "INSERT INTO events(class_id, start_date, end_date, day, start_tie, end_time, frequency, room, lecture_for_date, status, remarks, cancelled_on, max_participants, created_at) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(class_id, start_date, end_date, day, start_tme, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, 'NOW()')
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
            db.close()
