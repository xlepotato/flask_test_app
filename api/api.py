import flask
from flask import request, jsonify
from bs4 import BeautifulSoup
import urllib.request
import re
import requests



#find: Get a single match result
#findall: Return all matched results


app = flask.Flask(__name__)
app.config["DEBUG"] = True



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
        detail['mrt'] = row.p.text
        detail['address'] = row.find('p', class_='js-intro-mc-address-container').text

        detail['address'] = (detail['address'].replace("\n", "")).strip()
        detail['operating_hours'] = (detail['operating_hours'].replace("\n", "")).strip()


        details.append(detail)
    # print(bestrate_table.prettify)
    return jsonify(details)





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
