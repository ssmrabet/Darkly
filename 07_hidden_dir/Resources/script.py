import requests
import bs4 as bs

def scrapping_recursive(url):
	r = requests.get(url)
	s = bs.BeautifulSoup(r.text, 'html.parser')

	if (s is not None):
		links = s.find_all("a")
		#f = open("result.txt", "a+")

		for link in links:
			final_link = link.get('href')
			if (final_link == "README"):
				r = requests.get(url + final_link)
				line = r.text.encode('utf-8').strip()
				print(line)
				#f.write(line + "\n");
			elif (final_link != "../"):
				scrapping_recursive(url + final_link)
		#f.close()

if __name__ == "__main__":
	url = "http://192.168.1.40/.hidden/"
	scrapping_recursive(url)
