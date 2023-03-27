import multiprocessing.pool, requests, bs4, lxml, re, json
from random import randint
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

def _poisk_net(query, z=1):
	try:
		for j in search(query, tld="co.in", num=z, stop=z, pause=2):
			yield j
	except:
		return

def bot_poisk(query, words, otv=5):
	zap = otv
	ojid = ["погоди", "думаю", "ищю", "просматриваю варианты", "работаю"]
	TF_poisk = True
	while TF_poisk:
		#bot.send_message(message.from_user.id, ojid[randint(0, len(ojid) - 1)])
		#print("\n", ojid[randint(0, len(ojid) - 1)])
		otv1 = []
		for i in _poisk_net(query, zap):
			if i is None:
				continue
			otv1.append(i)
		words = [re.compile(w) for w in words]
		urls = [line.strip() for line in otv1 if line.strip()]
		def Match(url):
			try:
				text = requests.get(url).text
				soup = bs4.BeautifulSoup(text, 'lxml')
				for word in words:
					if len(soup(text=word)) > 0:
						return url, True
				return url, False
			except Exception as ex:
				return url, str(ex)
			finally:
				pass
		with multiprocessing.pool.ThreadPool(20) as pool:
			d = dict(list(pool.imap_unordered(Match, urls)))
		ln_d = len(d)
		if ln_d < otv:
			zap += 10
		else:
			TF_poisk = False
	return [str(i) for i in d]