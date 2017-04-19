import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import json
import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)

@app.route('/')
def index():
    f = open('copied_html/index.html', 'r')
    html = f.read()
    # result = requests.get('https://laulima.hawaii.edu/portal')
    # Probably Selenium
    soup = BeautifulSoup(html, 'lxml')
    tit = soup.find('span', 'siteTitle').get_text()[:-1]
    OBJ = {
        'nav': [],
        'body': {
            'sections': []
        }
    }
    # Content
    titles = []
    bodies = []
    i = 0
    for div in soup.find_all('div', 'portletTitleWrap'):
        for title in div.find_all('div', 'title'):
            titles.append(title.getText())
    for div in soup.find_all('div', 'portletMainWrap'):
        i = i + 1
        iframe = div.find('iframe')
        if (iframe):
            if(not bool(urlparse.urlparse(iframe.attrs['src']).netloc)):
                iframe.attrs['src'] = 'https://laulima.hawaii.edu' + iframe.attrs['src']
            obj = {'src': iframe.attrs['src']}
            bodies.append(obj)
        else:
            titles.pop(i)

    for idx, val in enumerate(titles):
        obj = {}
        obj[val] = bodies[idx]
        OBJ['body']['sections'].append(obj)
    # Nav Bar
    for li in soup.find_all('li', 'nav-menu'):
        obj = {'text': li.find(text=True, recursive=True), 'a': []}
        for ul in li.find_all('ul'):
            for a in ul.find_all('a'):
                obj['a'].append({'href': a.attrs['href'], 'text': a.getText()})
        OBJ['nav'].append(obj)
    return render_template('pages/index.html',
        title=tit,
        nav=OBJ['nav'],
        body=OBJ['body']
    )

@app.route('/<path:path>')
def static_proxy(path):
  return app.send_static_file(path)

@app.route('/login')
def login():
    return render_template('pages/login.html')

@app.route('/', methods=['POST'])
def handle_data():
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get('https://laulima.hawaii.edu/portal/relogin')

    username = driver.find_element_by_id("eid")
    password = driver.find_element_by_id("pw")

    username.send_keys(request.form['user_name'])
    password.send_keys(request.form['password'])

    driver.find_element_by_name("submit").click()

    elements = driver.find_elements_by_class_name('alertMessage')

    # Check if Logged In ( if elements[0].text == 'Invalid login' )
    # If Valid, grab data from index page and display
    # Else Send Back Response
    if (str(elements[0].text) == 'Invalid login'):
        print 'Invalid Login!'
    else:
        print 'Valid Login!'

    driver.quit()
    return redirect(url_for('index'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='localhost', port=port)
