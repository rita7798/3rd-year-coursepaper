import html
import re
import urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set(style='whitegrid')

PLAIN = 'https://www.proza.ru'


stats = dict()
for elem in ['stats_detectives', 'stats_cyber', 'stats_fantasy', 'stats_scifi', 'stats_horror', 'stats_adventures']:
    stats[elem]=dict()


def detectives():
	with open ('Detectives_2019.txt', 'a', encoding = 'utf-8') as f:
	    request = urllib.request.Request('https://www.proza.ru/texts/list.html?topic=07')
	    with urllib.request.urlopen(request) as response:
	        code = response.read().decode('cp1251')
	    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	    titles = regTitles.findall(code)
	    i_total = 0
	    i_year = 0
	    year = 2019
	    for title in titles:
	        try:
	            page = urllib.request.urlopen(PLAIN + title)
	            c = page.read().decode('cp1251')
	            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	            text = regText.findall(c)
	            f.write(text[0])
	            i_total += 1
	            i_year += 1
	        except:
	            print('Error at '+title)
	    prev_day = re.findall('Произведения раздела &laquo;детективы&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	    while True:
	        if str(year) in prev_day[0]:
	            with open ('Detectives_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;детективы&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	        else:
	            stats['stats_detectives'][year] = i_year
	            print(stats)
	            i_year = 0
	            year -= 1
	            with open ('Detectives_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;детективы&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	    print('detectives done', i_total)
	    stats['stats_detectives']['total'] = i_total
	return stats


def cyber():
	with open ('Cyber_2019.txt', 'a', encoding = 'utf-8') as f:
	    request = urllib.request.Request('https://www.proza.ru/texts/list.html?topic=26')
	    with urllib.request.urlopen(request) as response:
	        code = response.read().decode('cp1251')
	    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	    titles = regTitles.findall(code)
	    i_total = 0
	    i_year = 0
	    year = 2019
	    for title in titles:
	        try:
	            page = urllib.request.urlopen(PLAIN + title)
	            c = page.read().decode('cp1251')
	            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	            text = regText.findall(c)
	            f.write(text[0])
	            i_total += 1
	            i_year += 1
	        except:
	            print('Error at '+title)
	    prev_day = re.findall('Произведения раздела &laquo;киберпанк&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	    while True:
	        if str(year) in prev_day[0]:
	            with open ('Cyber_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;киберпанк&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	        else:
	            stats['stats_cyber'][year] = i_year
	            print(stats)
	            i_year = 0
	            year -= 1
	            with open ('Cyber_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;киберпанк&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	    print('cyber done', i_total)
	    stats['stats_cyber']['total'] = i_total
	return stats


def fantasy():
	with open ('Fantasy_2019.txt', 'a', encoding = 'utf-8') as f:
	    request = urllib.request.Request('https://www.proza.ru/texts/list.html?topic=24')
	    with urllib.request.urlopen(request) as response:
	        code = response.read().decode('cp1251')
	    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	    titles = regTitles.findall(code)
	    i_total = 0
	    i_year = 0
	    year = 2019
	    for title in titles:
	        try:
	            page = urllib.request.urlopen(PLAIN + title)
	            c = page.read().decode('cp1251')
	            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	            text = regText.findall(c)
	            f.write(text[0])
	            i_total += 1
	            i_year += 1
	        except:
	            print('Error at '+title)
	    prev_day = re.findall('Произведения раздела &laquo;фэнтези&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	    while True:
	        if str(year) in prev_day[0]:
	            with open ('Fantasy_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;фэнтези&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	        else:
	            stats['stats_fantasy'][year] = i_year
	            print(stats)
	            i_year = 0
	            year -= 1
	            with open ('Fantasy_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;фэнтези&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	    print('fantasy done', i_total)
	    stats['stats_fantasy']['total'] = i_total
	return stats


def scifi():
	with open ('Scifi_2019.txt', 'a', encoding = 'utf-8') as f:
	    request = urllib.request.Request('https://www.proza.ru/texts/list.html?topic=06')
	    with urllib.request.urlopen(request) as response:
	        code = response.read().decode('cp1251')
	    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	    titles = regTitles.findall(code)
	    i_total = 0
	    i_year = 0
	    year = 2019
	    for title in titles:
	        try:
	            page = urllib.request.urlopen(PLAIN + title)
	            c = page.read().decode('cp1251')
	            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	            text = regText.findall(c)
	            f.write(text[0])
	            i_total += 1
	            i_year += 1
	        except:
	            print('Error at '+title)
	    prev_day = re.findall('Произведения раздела &laquo;фантастика&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	    while True:
	        if str(year) in prev_day[0]:
	            with open ('Scifi_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;фантастика&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	        else:
	            stats['stats_scifi'][year] = i_year
	            print(stats)
	            i_year = 0
	            year -= 1
	            with open ('Scifi_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;фантастика&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	    print('scifi done', i_total)
	    stats['stats_scifi']['total'] = i_total
	return stats


def horror():
	with open ('Horror_2019.txt', 'a', encoding = 'utf-8') as f:
	    request = urllib.request.Request('https://www.proza.ru/texts/list.html?topic=25')
	    with urllib.request.urlopen(request) as response:
	        code = response.read().decode('cp1251')
	    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	    titles = regTitles.findall(code)
	    i_total = 0
	    i_year = 0
	    year = 2019
	    for title in titles:
	        try:
	            page = urllib.request.urlopen(PLAIN + title)
	            c = page.read().decode('cp1251')
	            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	            text = regText.findall(c)
	            f.write(text[0])
	            i_total += 1
	            i_year += 1
	        except:
	            print('Error at '+title)
	    prev_day = re.findall('Произведения раздела &laquo;ужасы&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	    while True:
	        if str(year) in prev_day[0]:
	            with open ('Horror_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;ужасы&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	        else:
	            stats['stats_horror'][year] = i_year
	            print(stats)
	            i_year = 0
	            year -= 1
	            with open ('Horror_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;ужасы&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	    print('horror done', i_total)
	    stats['stats_horror']['total'] = i_total
	return stats


def adventures():
	with open ('Adventures_2019.txt', 'a', encoding = 'utf-8') as f:
	    request = urllib.request.Request('https://www.proza.ru/texts/list.html?topic=23')
	    with urllib.request.urlopen(request) as response:
	        code = response.read().decode('cp1251')
	    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	    titles = regTitles.findall(code)
	    i_total = 0
	    i_year = 0
	    year = 2019
	    for title in titles:
	        try:
	            page = urllib.request.urlopen(PLAIN + title)
	            c = page.read().decode('cp1251')
	            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	            text = regText.findall(c)
	            f.write(text[0])
	            i_total += 1
	            i_year += 1
	        except:
	            print('Error at '+title)
	    prev_day = re.findall('Произведения раздела &laquo;приключения&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	    while True:
	        if str(year) in prev_day[0]:
	            with open ('Adventures_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;приключения&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	        else:
	            stats['stats_adventures'][year] = i_year
	            print(stats)
	            i_year = 0
	            year -= 1
	            with open ('Adventures_{}.txt'.format(year), 'a', encoding = 'utf-8') as f:
	                try:
	                    page = urllib.request.urlopen(PLAIN + prev_day[0])
	                    print(prev_day[0])
	                    code = page.read().decode('cp1251')
	                    regTitles = re.compile('<li><a href=\"(.*)\" class=\"poemlink\">.*</a>.*\"authorlink\">.*</a></em>.*</small></li>')
	                    titles = regTitles.findall(code)
	                    for title in titles:
	                        try:
	                            page = urllib.request.urlopen(PLAIN + title)
	                            c = page.read().decode('cp1251')
	                            regText = re.compile('<div class=\"text\">(.*)</div>\n<br><br>', flags=re.S)
	                            text = regText.findall(c)
	                            f.write(text[0])
	                            i_total += 1
	                            i_year += 1
	                            print(i_total)
	                        except:
	                            print('Error at '+title)
	                    prev_day = re.findall('Произведения раздела &laquo;приключения&raquo; за предыдущий день: <a href=\"(.*)\"><b>', code)
	                    if '1999' in prev_day[0]:
	                        break
	                except:
	                    continue
	    print('adventures done', i_total)
	    stats['stats_adventures']['total'] = i_total
	return stats


def plotting1(stats):
	x = []
	y = []
	for genre , value in stats.items():
	    for year, number in value.items():
	        if year != 'total':
	            continue
	        else:
	            x.append(genre.split('_')[1])
	            y.append(number)
	sns.barplot(x, y, palette = 'vlag').set_title('Общее распределение по жанрам за все время')   
	fig = plt.gcf()
	fig.set_size_inches(12,8)
	plt.savefig('1fig.png', dpi=100)


def plotting2(stats):
	x = [x for x in range (2001, 2020)]
	y = []
	for genre , value in stats.items():
	    for year, number in value.items():
	        if year == 'total':
	            continue
	        else:
	            y.append(number)
	    plt.plot(x, y, linewidth=3., label = genre.split('_')[1])
	    plt.legend(frameon=1, facecolor='white', fontsize='large')
	    y = []
	fig = plt.gcf()
	fig.set_size_inches(15,8)
	plt.title('Распределение произведений по жанрам с 2000 до 2019 года')
	fig.savefig('2fig.png', dpi=100)


detectives()
cyber()
fantasy()
scifi()
horror()
adventures()
plotting1(stats)
plotting2(stats)

