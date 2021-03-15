import re
import json
import argparse
import cloudscraper

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = ""

def parse():
	parser = argparse.ArgumentParser(description='Check if your email has been pwned')
	parser.add_argument('-email', metavar="email", type=str, required=True, help='Email to check for breaches')
	args = parser.parse_args()
	return args


def scrap_and_store(email):
	url = "https://haveibeenpwned.com/unifiedsearch/"+email
	scraper = cloudscraper.create_scraper()
	result = scraper.get(url)
	print("Info: Done Scrapping!")
	if(result.text!=""):
		print("Info: Breach found!")
		with open("data/{}.json".format(email), "w") as f:
			json.dump(result.json(), f , sort_keys=True, indent=4)
		print("Info: Data saved at {}.json".format(email))
	else:
		print("Info: No breach found for this email.")
    
if __name__ == "__main__":
	email = parse().email
	if(re.search(regex,email)):  
		scrap_and_store(email)
	else:
		print("Error: Invalid Email please try again with valid mail!")


