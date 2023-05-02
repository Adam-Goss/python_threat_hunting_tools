# import necessary Python modules
import requests, csv
from bs4 import BeautifulSoup
import argparse

import sys

# command line argument parser 
parser = argparse.ArgumentParser()
parser.add_argument('--csv', action='store_true', help='output in CSV format')
parser.add_argument('--json', action='store_true', help='output in JSON format')
parser.add_argument('--txt', action='store_true', help='output in text format')
args = parser.parse_args()


# print(args.json)
# print(args.txt)


# output functions
def output_csv(vulns):
    # CSV file header row
    header_row = ["Product", "Vendor", "Description", "Published", "CVSS", "CVE", "Reference"]

    # edit filename to be a CSV
    csv_file = FILENAME + ".csv"
    # create a CSV file
    with open(csv_file, "w", encoding='UTF8', newline='') as f:
        # create csv writer to write data to file
        writer = csv.writer(f)
        # write header row
        writer.writerow(header_row)
        # write vulnerabilities
        for vuln in vulns:
            data_row = [vuln['product'], vuln['vendor'], vuln['description'], vuln['published'],vuln['cvss'], vuln["cve"], vuln['reference']]
            writer.writerow(data_row)


def output_json(vulns):
    pass

def output_txt(vulns):
    pass



# download the page 
WEB_PAGE = "https://www.cisa.gov/news-events/bulletins/sb23-100"
page = requests.get(WEB_PAGE)
# parse the page with Beautiful Soup
soup = BeautifulSoup(page.content, "html.parser")

# variables for output
PAGE_TITLE = soup.title.string
a = soup.title.string.split("of")
b = a[1].split("|")
FILENAME = "CISA vulnerabilties - " + b[0].strip()


# capture high vulnerabilities table
table = soup.find("table")
table_body = table.find("tbody")
rows = table_body.find_all("tr")

# list to hold vulnerability dictionaries
vulns = []
# loop through table rows
for row in rows:
    # create table columns
    cols = [x for x in row.find_all("td")]

    # extract relevant fields
    product, vendor = cols[0].text.split("--")
    description = cols[1].text.strip()
    published = cols[2].text.strip()
    cvss = cols[3].text.strip()
    cve = cols[4].find("a").text.strip()
    reference = cols[4].find("a").get("href")

    # store fields as a dictionary object
    vuln = {
        "product": product.strip(),
        "vendor": vendor.strip(),
        "description": description,
        "published": published,
        "cvss": cvss,
        "cve": cve,
        "reference": reference
    }
    
    # append dictionary object to vulnerability list
    vulns.append(vuln)



if args.csv:
    output_csv(vulns)
elif args.json:
    output_json(vulns)
elif args.txt:
    output_txt(vulns)
else:
    print(vulns)





print(f"Printed {PAGE_TITLE}")
print(f"-> see {FILENAME}")
