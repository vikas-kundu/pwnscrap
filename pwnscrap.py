import re
import json
import argparse
import cloudscraper


def parse():
	parser = argparse.ArgumentParser(description='Check if your email has been pwned')
	parser.add_argument('-email', metavar="email", type=str, required=True, help='Email to check for breaches')
	args = parser.parse_args()
	return args


def scrap_and_store(email):
	url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
	scraper = cloudscraper.create_scraper()
	try:
		result = scraper.get(url)
	except Exception as e:
		print(f"Error: Following exception occured!\n{e}\nPlease retry once more!")

	else:
		print('Info: Done Scrapping!')
		if result.text!='':
			print('Warning: Breach found!')
			with open("data/{}.json".format(email), "w") as f:
				json.dump(result.json(), f , sort_keys=True, indent=4)
			print(f"Info: Data saved at /data/{email}.json")
		else:
			print('Info: No breach found for this email.')
    
if __name__ == "__main__":
	email = parse().email
	scrap_and_store(email)

