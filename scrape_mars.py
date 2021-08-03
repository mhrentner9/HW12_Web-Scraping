#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time


# In[2]:
def init_browser():
 
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

    # In[3]:


    # Show path that we will be using
    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    get_ipython().system('which chromedriver')

#Scrape the Mars News Site and collect the latest News Title and Paragraph Text. 
#Assign the text to variables that you can reference later.
# Visit Nasa news url through splinter module
def scrape():
    browser = init_browser()

    url_news = "https://redplanetscience.com/"
    browser.visit(url_news)


    # In[4]:


    # HTML Object
    html_news = browser.html
    soup = bs(html_news, "html.parser")


    # In[5]:


    # Scrape the latest News Title and Paragraph Text
    news_title = soup.find("div", class_ = "content_title").text
    news_paragraph = soup.find("div", class_ = "article_teaser_body").text

    # Display scrapped news 
    print(news_title)
    print("-----------------------------------------")
    print(news_paragraph)


    # In[6]:


    # Exit Browser.
    browser.quit()


    # In[7]:


    # Setup splinter for image
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[8]:


    # Visit JPL Featured Space Image url through splinter module
    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    # Retrieve all elements that contain book information
    images = soup.find_all('div', class_='floating_text_area')

    for image in images:
        link = image.find("a")
        href = link['href']
        
        featured_image_url = ("https://spaceimages-mars.com/" + href)
        
    featured_image_url


    # In[11]:


    facts_url = 'https://galaxyfacts.com/mars/'
    response = requests.get(facts_url)
    soup = bs(response.text, 'html.parser')


    # In[13]:


    tables = pd.read_html(facts_url)
    tables[0]


    # In[33]:


    # Visit Mars facts url 
    facts_url = 'https://galaxyfacts-mars.com/'

    # Use Panda's `read_html` to parse the url
    mars_facts = pd.read_html(facts_url)

    # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
    mars_df = mars_facts[0]

    # Assign the columns `['Description', 'Value']`
    mars_df.columns = ['Description','Mars','Earth']

    # Set the index to the `Description` column without row indexing
    mars_df.set_index('Description', inplace=True)

    # Save html code to folder Assets
    mars_df.to_html()

    data = mars_df.to_dict(orient='records')  # Here's our added param..

    # Display mars_df
    mars_df


    # In[34]:


    # Visit hemispheres website through splinter module 
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)


    # In[35]:


    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html_hemispheres, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    # Store the main_ul 
    hemispheres_main_url = 'https://marshemispheres.com/'

    # Loop through the items previously stored
    for i in items: 
        # Store title
        title = i.find('h3').text
        
        # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        
        # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + partial_img_url)
        
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
        
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = bs( partial_img_html, 'html.parser')
        
        # Retrieve full image source 
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        
        # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        

    # Display hemisphere_image_urls
    hemisphere_image_urls
    # Close the browser after scraping
    browser.quit()

# In[ ]:





# In[ ]:




