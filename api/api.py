import flask
from flask import request, jsonify
from bs4 import BeautifulSoup
import urllib.request
import re
import requests
from selenium import webdriver




#find: Get a single match result
#findall: Return all matched results


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# driver = webdriver.Chrome(r'C:\Users\WNG056\Downloads\chromedriver_win32\chromedriver.exe')
# driver.get('https://cashchanger.co/singapore')


# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

url2 = "https://en.wikipedia.org/wiki/Artificial_intelligence"
url = "https://www.dataquest.io/blog/web-scraping-beautifulsoup/"
URL = "https://cashchanger.co/singapore"


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/currency/all', methods=['GET'])
def api_currencies():
    try:
        page = urllib.request.urlopen(url) # conntect to website
    except:
        print("An error occured.")
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.prettify) # gives the visual representation of the parse tree created from the raw HTML content.
    regex = re.compile('^tocsection-')
    content_lis = soup.find_all('li', attrs={'class': regex})
    print(content_lis)
    content = []
    for li in content_lis:
        content.append(li.getText().split('\n')[0])
    print(content)
    return jsonify(content)

    # # Getting the keywords section
    # keyword_section = soup.find(class_="keywords-section")
    # # Same as: soup.select("div.article-wrapper grid row div.keywords-section")
    #
    # # Getting a list of all keywords which are inserted into a keywords list in line 7.
    # keywords_raw = keyword_section.find_all(class_="keyword")
    # keyword_list = [word.get_text() for word in keywords_raw]

@app.route('/api/v1/resources/currency/bestrate/all', methods=['GET'])
def api_bestrate():
    try:
        # page = urllib.request.urlopen(url) # conntect to website
        r = requests.get(URL)
    except:
        print("An error occured.")
        # soup = BeautifulSoup(page, 'html.parser')
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify) # gives the visual representation of the parse tree created from the raw HTML content.
    best_rate_container = soup.find('div', class_='container bestrate-container')
    print(best_rate_container.prettify)


    # regex = re.compile('^tocsection-')
    #     # content_lis = soup.find_all('li', attrs={'class': regex})
    #     # print(content_lis)
    #     # content = []
    #     # for li in content_lis:
    #     #     content.append(li.getText().split('\n')[0])
    #     # print(content)
    #     # return jsonify(content)
    return 'nyan'

    # # Getting the keywords section
    # keyword_section = soup.find(class_="keywords-section")
    # # Same as: soup.select("div.article-wrapper grid row div.keywords-section")
    #
    # # Getting a list of all keywords which are inserted into a keywords list in line 7.
    # keywords_raw = keyword_section.find_all(class_="keyword")
    # keyword_list = [word.get_text() for word in keywords_raw]


@app.route('/api/v1/resources/currency/buy/bestrate/all', methods=['GET'])
def sell_bestrate():
    try:
        # page = urllib.request.urlopen(url) # conntect to website
        r = requests.get(URL)
    except:
        print("An error occured.")
        # soup = BeautifulSoup(page, 'html.parser')
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify) # gives the visual representation of the parse tree created from the raw HTML content.
    best_rate_container = soup.find('div', class_='container bestrate-container')
    # print(best_rate_container.prettify)
    currencies = []

    # bestrate_table = best_rate_container.find_all('div', class_='bestrate')
    for row in best_rate_container.find_all('div', class_='bestrate'):
        print(row.prettify)
        currency = {}
        currency['country_currency'] = row.find('span', class_='country-currency').text
        currency['currency_code'] = row.find('span', class_='currency-code float-left').text
        currency['rate'] = row.find('div', class_='text-big text-center').text
        currencies.append(currency)
    # print(bestrate_table.prettify)


    # regex = re.compile('^tocsection-')
    #     # content_lis = soup.find_all('li', attrs={'class': regex})
    #     # print(content_lis)
    #     # content = []
    #     # for li in content_lis:
    #     #     content.append(li.getText().split('\n')[0])
    #     # print(content)
    #     # return jsonify(content)
    return jsonify(currencies)
    # return 'nyan'

    # # Getting the keywords section
    # keyword_section = soup.find(class_="keywords-section")
    # # Same as: soup.select("div.article-wrapper grid row div.keywords-section")
    #
    # # Getting a list of all keywords which are inserted into a keywords list in line 7.
    # keywords_raw = keyword_section.find_all(class_="keyword")
    # keyword_list = [word.get_text() for word in keywords_raw]


@app.route('/api/v1/resources/moneychanger/profile', methods=['GET'])
def get_profile():
    MONEYCHANGER_URL = "https://cashchanger.co/singapore/mc/simlim-exchange-and-trading/189"
    try:
        r = requests.get(MONEYCHANGER_URL)
    except:
        print("An error occured.")
        # soup = BeautifulSoup(page, 'html.parser')
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify) # gives the visual representation of the parse tree created from the raw HTML content.
    profile = soup.find('div', class_='mc-detail')
    # print(profile.prettify)
    details = []

    # bestrate_table = best_rate_container.find_all('div', class_='bestrate')
    for row in profile.find_all('div', class_='profile-card box'):
        print(row.prettify)
        detail = {}
        detail['name'] = row.find('h1', class_='text-black').text
        detail['operating_hours'] = row.find('p', class_='js-intro-openinghours-container').text
        detail['tel_No'] = row.find('p', class_='js-intro-mc-phone-container contact').a['href']
        detail['mrt'] = row.find_all('p')[2].text
        detail['address'] = row.find('p', class_='js-intro-mc-address-container').text

        # Clean data
        detail['mrt'] = (detail['mrt'].replace("\n", "")).strip()
        detail['address'] = (detail['address'].replace("\n", "")).strip().partition("      ")[0]
        detail['operating_hours'] = (detail['operating_hours'].replace("\n", "")).strip().replace("  ", "")
        # .replace("  ","")

        details.append(detail)
    # print(bestrate_table.prettify)
    return jsonify(details)



@app.route('/api/v1/resources/moneychanger/profile2', methods=['GET'])
def get_profile2():
    driver = webdriver.Chrome(r'C:\Users\WNG056\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get('https://cashchanger.co/singapore/sgd-to-aud')
    # pika = driver.find_element_by_id('currencyresult-area')
    #
    # clean_list = pika.text.split('\n')

    # clean_list
    # clean_list = [clean_list[i::6] for i in range(6)]


    # pika2 = driver.find_element_by_id('currencyresult-area2')
    # clean_list2 = pika2.text.split('\n')


    test = driver.find_elements_by_class_name('result-box')
    # clean_list = test.text.split('\n')
    # print(test)



    # clean_list3 = clean_list.extend(clean_list2)


    # clean_list = [i.split('\t') for i in clean_list]

    details = []
    # print(pika)
    # nyo = driver.find_element_by_class_name('currency-item')
    # print(nyo.text)
    # c = []
    location = driver.find_elements_by_class_name('item-location1')
    train = driver.find_elements_by_class_name('item-location2')
    for ll in location:
        print(ll.text)
    for kk in train:
        print(kk.text)


    details = []
    n = 0
    first = True;
    for i in test:
        if first:
            first = False
        else:
            a = i.text.split('\n')
            detail = {}
            if a[0] != '':
                # c.append(a)
                detail['currency_name'] = a[0]
                detail['exchange_rate'] = a[1]
                detail['rate'] = a[2]
                detail['last_update'] = a[3]
                detail['moneychanger_name'] = a[4]

                detail['location'] = location[n].text
                detail['mrt'] = train[n].text
                details.append(detail)
                n += 1
    for k in details:
        print(k)

    #     detail = {}
    #     detail['name'] = row.find('h1', class_='text-black').text
    #     detail['operating_hours'] = row.find('p', class_='js-intro-openinghours-container').text
    #     detail['tel_No'] = row.find('p', class_='js-intro-mc-phone-container contact').a['href']
    #     detail['mrt'] = row.find_all('p')[2].text
    #     detail['address'] = row.find('p', class_='js-intro-mc-address-container').text


    # content []

    # c = c.partition("      ")[0]

    # clean_list = [clean_list[x:x + 7] for x in range(0, len(clean_list), 7)]
    # clean_list2 = [clean_list2[x:x + 7] for x in range(0, len(clean_list2), 7)]

    # print(clean_list)
    # print(clean_list2)



    # for j in nyo:
    #     print(j)

    # bestrate_table = best_rate_container.find_all('div', class_='bestrate')
    # for row in profile.find_all('div', class_='profile-card box'):
    #     print(row.prettify)
    #     detail = {}
    #     detail['name'] = row.find('h1', class_='text-black').text
    #     detail['operating_hours'] = row.find('p', class_='js-intro-openinghours-container').text
    #     detail['tel_No'] = row.find('p', class_='js-intro-mc-phone-container contact').a['href']
    #     detail['mrt'] = row.find_all('p')[2].text
    #     detail['address'] = row.find('p', class_='js-intro-mc-address-container').text
    #
    #     # Clean data
    #     detail['mrt'] = (detail['mrt'].replace("\n", "")).strip()
    #     detail['address'] = (detail['address'].replace("\n", "")).strip().partition("      ")[0]
    #     detail['operating_hours'] = (detail['operating_hours'].replace("\n", "")).strip().replace("  ", "")
    #     # .replace("  ","")
    #
    #     details.append(detail)
    # print(bestrate_table.prettify)
    return jsonify(details)







@app.route('/api/v1/resources/moneychanger/moneychanger2', methods=['GET'])
def get_moneychanger2():
    driver = webdriver.Chrome(r'C:\Users\WNG056\Downloads\chromedriver_win32\chromedriver.exe')
    details = []

    for i in range(1,3):
        driver.get('https://cashchanger.co/singapore/mc/firman-hah-international-exchange/' + str(i))
        mc_detail = driver.find_elements_by_class_name('mc-detail')
        detail = {}
        detail['img'] = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/section[2]/div/div[1]/div/div/div[1]/img').get_attribute('src')  # get the img src
        for row in mc_detail:
            currencies = []
            col = row.text.split('\n')
            if col[0] != '':  # check if there is empty data
                try:
                    # if operating hours info is available
                    driver.find_element_by_class_name('js-intro-openinghours-container')
                    detail['moneychanger_name'] = col[0]
                    detail['operating_hours'] = col[1]
                    detail['tel_No'] = col[2]
                    detail['mrt'] = col[3]
                    detail['address'] = col[4]
                except:
                    # if operating hours info is unavailable
                    detail['moneychanger_name'] = col[0]
                    detail['operating_hours'] = '-'
                    detail['tel_No'] = col[1]
                    detail['mrt'] = col[2]
                    detail['address'] = col[3]
        try:
            currency_table = driver.find_element_by_class_name('mc-currencyratetable')
            currency_data = currency_table.find_elements_by_class_name(' currencybox-rate')
            for row in currency_data:
                currency = {}
                col = row.text.split('\n')
                if col[0] != '':
                    inverse_rate = row.find_elements_by_class_name('inverserate')
                    if inverse_rate[0].text != '':  # check if the rate display info for buy is available
                        currency['currency_code'] = col[0]
                        currency['currency_name'] = col[1]
                        currency['exchange_rate_buy'] = col[2]
                        currency['rate_buy'] = col[3]
                        currency['last_update_buy'] = col[4]
                        currency['exchange_rate_sell'] = col[5]
                        if inverse_rate[1].text != '': # check if the rate display info for sell is available
                            currency['rate_sell'] = col[6]
                            currency['last_update_sell'] = col[7]
                        else:  # rate display info for sell is missing
                            currency['rate_sell'] = '-'
                            currency['last_update_sell'] = col[6]
                    else:  # rate display info for buy is missing
                        currency['currency_code'] = col[0]
                        currency['currency_name'] = col[1]
                        currency['exchange_rate_buy'] = col[2]
                        currency['rate_buy'] = '-'
                        currency['last_update_buy'] = col[3]
                        currency['exchange_rate_sell'] = col[4]
                        if inverse_rate[1].text != '':   # check if the rate display info for sell is available
                            currency['rate_sell'] = col[5]
                            currency['last_update_sell'] = col[6]
                        else: # rate display info for sell is missing
                            currency['rate_sell'] = '-'
                            currency['last_update_sell'] = col[5]
                    currencies.append(currency)  # append all the available currencies offered by a particular money changer to a list
            detail['currency_table'] = currencies
            details.append(detail)
        except Exception as e:
            print(e)
            pass  # skip the page if the relevant info of the money changer is not available to scrape
    for k in details:
        print(k)
    print(len(details)) # print the length of the data scrapped
    return jsonify(details)  # return the data in json format




@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


if __name__ == '__main__':
    app.run()
