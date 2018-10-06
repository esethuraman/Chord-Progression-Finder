import requests
from bs4 import BeautifulSoup

lyrics=""

def get_chords():
	f = open("parsedLyrics.txt", 'r')
	lines = f.readlines()
	for line in lines:
		# print line
		# line = line.strip()
		if line:
			print line
			# print "-----"

def write_into_file(lyrics):
	f = open("parsedLyrics.txt", 'w')
	f.write(lyrics)
	f.close

def main():
	# resp = requests.get("https://tabs.ultimate-guitar.com/tab/ed_sheeran/perfect_chords_1956589")
	resp = requests.get("https://www.mychordbook.com/chords/ed-sheeran/afire-love")
	soup = BeautifulSoup(resp.content, 'html.parser')
	lyrics = soup.find('body').find('pre').get_text().encode('utf-8')
	write_into_file(lyrics)
	get_chords()



if __name__=="__main__":
	main()

