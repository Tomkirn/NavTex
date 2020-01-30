import ui
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url490 = 'http://www.dwd.de/DE/fachnutzer/schifffahrt/funkausstrahlung/navtex/490_emd.html'
url518 = 'http://www.dwd.de/DE/fachnutzer/schifffahrt/funkausstrahlung/navtex/518_emd.html'
urlDWD = 'http://www.dwd.de/DE/leistungen/kuestenseewetterbericht/kuestenseewetterbericht.html'

def get_content(url):
	text = requests.get(url, headers=headers)
	soup = BeautifulSoup(text.text, 'html5lib')

	output = soup.body.pre.contents
	inhalt = ''
	
	for entry in output:
		inhalt += entry

	return inhalt

def get_content_wetter(url):
	text = requests.get(url, headers=headers)
	soup = BeautifulSoup(text.text, 'html5lib')

	output = soup.body.pre.text

	return output

def refresh(choice):
	if choice == 0:
		v['textview1'].text = get_content(url490)
	elif choice == 1:
		v['textview1'].text = get_content(url518)
	else:
		v['textview1'].text = get_content_wetter(urlDWD)

def segctl1act(sender):
	refresh(sender.selected_index)

def btn1act(sender):
	refresh(v['segmentedcontrol1'].selected_index)


v = ui.load_view()
v.present('fullscreen',hide_title_bar=True)
refresh(v['segmentedcontrol1'].selected_index)
