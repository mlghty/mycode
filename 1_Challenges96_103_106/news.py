from newsapi import NewsApiClient
from flask import Flask
from flask import render_template
import pdfkit

app = Flask(__name__)

bool_print_page = False

@app.route('/news')
def get_news():
    newsapi = NewsApiClient(api_key='c1ef0338326240e8858cfdd024dbca9f')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(country='us', page_size=10)
    
    return render_template('news.html', articles=top_headlines['articles'])

@app.after_request
def after_request_func(response):
    if not bool_print_page:
        website_to_pdf()
    return response
           
# Sometimes fails due to wkhtmltopdf.exe
def website_to_pdf():
    global bool_print_page 
    bool_print_page = True

    path_wkhtmltopdf = r'C:\Users\Joe\AppData\Local\Autodesk\webdeploy\production\1a27f23c10bc87f7eab1f89e440a46f886b5f544\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    
    pdfkit.from_url('http://127.0.0.1:5000/news', 'out.pdf',configuration=config)
    
    return 

if __name__ == "__main__":
    app.run(debug=True)
    
# Mock Tech Interview (optional):
# 1 HOUR
# Access the NEWS API, an open API.
 
# Create an applicaiton using Flask/Jinja2 Templates to create 
# an application to do the following.

# From the News API, get a set of articles…any set. NEWS API has some guidance and options there. 

# In the BROWSER (not the command line — hint, Jinja template), allow your user to select a random article to read. You can accomplish this in a few different ways. 

# Render the Title, Author, Date, and the contents of the article to the screen. Styling is optional (but a fun challenge). 

# BONUS: Print it to a local file. 
