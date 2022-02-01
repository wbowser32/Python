#We are a going to scrape this site and loop through all of the items=
#in order to obtain the table data on each webpage and link it to the items via an array
#Data Dictionaries 5.80 Main R4 Tables (All)
#username:dbowser password:Spiderman32
#We get the item number from  https://cx.trizetto.com/doc/datadictionaries/index.cfm?prod=1973&dd_detail=t&pg=12&mod=1 (This has them all)
#Then we get titles which is the item, from <a hef title = (X)/a>
#Make that the item= then loop through each webpage
# https://cx.trizetto.com/doc/datadictionaries/itemDetail.cfm?prod=1973&type=t&item=abaact (Change out the last part with what we get)
#tr class="doc" Bgcolor#FFFFFFFFFF This has all the right information. #FFFFFFFFFF color scheme is the differentiating factor
#https://beautiful-soup-4.readthedocs.io/en/latest/ use this as documentation

import mechanize
from bs4 import BeautifulSoup
import http.cookiejar
import configparser
import pymysql

cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
#br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# br.set_cookiejar(cj)
#br.addheaders = [('User-agent', 'Chrome')]
#URL = "https://cx.trizetto.com/doc/datadictionaries/itemDetail.cfm?prod=1973&type=t&item=abaact"
#variable = ['abfdata','abfdatad','abfdath']
URL = "https://cx.trizetto.com/doc/datadictionaries/itemDetail.cfm?prod=1973&type=t&item="
Lurr = "https://cx.trizetto.com/doc/datadictionaries/index.cfm?prod=1973&dd_detail=t&pg=12&mod=1"

br.open(Lurr)
br.select_form(nr=0)
br.form['name'] = 'ddbowser'
br.form['password'] = 'Spiderman32'
br.submit()
html = br.response().read()
soup = BeautifulSoup(html, "html.parser")
# print(soup)
variable = []
y = ""

for row in soup.find_all('tr'):
    if row.find_all('tr', attrs={'bgcolor': 'White'}):
        variable.append([str(tr.text.strip()) for tr in row.find_all('tr')])
        y = " ".join(str(x) for x in variable)
        q = y.replace("'( ... )denotes truncated names.  Hover over link for complete name.\', \'Model: Main Model\\xa0List of\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tTables\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\n\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tPage:\\xa0\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n10\\n11\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\xa0ALL', ", "")
        q = q.replace("\\n", "', ")
        q = q.replace("\\", "', ")
        q = q.replace("'", "")
        q = q.replace("[", "")
        q = q.replace("]", "")
        variable = []
        variable = q.split(", ")
#'( ... )denotes truncated names.  Hover over link for complete name.\', \'Model: Main Model\\xa0List of\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tTables\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\n\\r\\n\\t\\t\\t\\t\\t\\t\t\\t\\t\\tPage:\\xa0\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n10\\n11\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\xa0ALL',

for v in variable[:2]:
    br.open(URL+v)
    html = br.response().read()
    soup = BeautifulSoup(html, "html.parser")
    data = []
    p = ""
    for row in soup.find_all('tr'):
        if row.find_all('tr', attrs={'bgcolor':'#FFFFFF'}):
            data.append([str(tr.text.strip()) for tr in row.find_all('tr')])
        text_file = open("Output_"+v+".txt", "w")
        p = " ".join(str(x) for x in data[1:])

    z = p.replace("\\n\\n\\n\\r", ",Primary Key,")
    z = z.replace("\\n\\", " ")
    z = z.replace("\\t\\", " ")
    z = z.replace("\\r ", " ")
    z = z.replace("\\t", " ")
    z = z.replace(" t ", " ")
    z = z.replace(" r ", " ")
    z = z.replace(" t ", " ")
    z = z.replace(" t ", " ")
    z = z.replace(" t ", ",")
    z = z.replace(" t", ",")
    z = z.replace(",t ", ",")
    z = z.replace("t\\r\\n", " ")
    z = z.replace(",,", ",")
    z = z.replace(" ,,", ",")
    z = z.replace("\\r\\n", ",")
    z = z.replace(" n ", "")
    z = z.replace(" n,", ", ")
    z = z.replace(" ,,", ", ")
    z = z.replace("'Name,Datatype,NULL,Definition,In Views?,Constraints?', ", "")

    config = configparser.RawConfigParser()
    config.read(filenames='my.properties')
    #print(config.sections())

    # h = config.get('EDIApplicationsTest', 'edi3')#'host'
    # u = config.get('EDIApplicationsTest', 'odbcRO')#'user'
    # p = config.get('EDIApplicationsTest', 'odbcRO')#'password'
    # db = config.get('EDIApplicationsTest', 'EDIApplication Test')#'db'
    EdiTest_db = pymysql.connect(host='edi3', user='odbcRO', password='odbcRO', db='EDIApplicationTest')
    EdiTest_db = pymysql.connect(h, u, p, db)
    cursor = EdiTest_db.cursor()
    sql = """CREATE TABLE WIKI2 (
    RANKINGINT,
    MARKETCHAR(50),
    RETAIL_VALUECHAR(20),
    PHYSICALINT,
    DIGITALINT,
    PERFORMANCE_RIGHTSINT,
    SYNCHRONIZATIONINT
    )"""
    cursor.execute(sql)
    # EdiTest_db = pymysql.connect(h, u, p, db)
    #
    # mySql_insert_query = """INSERT"""
    #
    # records_to_insert = z
    #
    # cursor = EdiTest_db.cursor()
    # cursor.executemany(mySql_insert_query, records_to_insert)
    # EdiTest_db.commit()
    # EdiTest_db.close()
print("Record inserted successfully into table")

#     n = text_file.write(z)
#     text_file.close()
