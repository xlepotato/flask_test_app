from flask import Flask
from selenium import webdriver

app = Flask(__name__)
app.config["DEBUG"] = True

# def hello_world():
#     return 'Hello World!'


def web_scrape():
    driver = webdriver.Chrome(r'C:\Users\WNG056\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get('https://cashchanger.co/singapore')

# if __name__ == '__main__':
#     app.run()
#     web_scrape()
