from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text           # get the info from the site
soup = BeautifulSoup(source, 'lxml')                        # make it a beautiful soup object
print(soup.prettify())                                      # make it look pretty
                                                            # (print HTML in the correct format)

headlines = []
summaries = []
links = []
for article in soup.find_all('article'):                    # find all piece of HTML that have article tag

    headline = article.h2.a.text                            # get the text of the a tag of the h2 tag of the article 
    print(headline)
    headlines.append(headline)
    
    summary = article.find('div', class_='entry-content').p.text    # get text of the div tag with 
    print(summary)                                                  # entry-content class          
    summaries.append(summary)
    
    try:                                                            # if there is a link, get it; if not print None
        vid_src = article.find('iframe', class_='youtube-player')['src']
        
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        
        link = f'https://youtube.com/watch?v={vid_id}'              # embed the link extension in a real link
    except Exception as e:
        link = None
        
    print(link)                                                     # save link & print it
    links.append(link)
    
    print()
    print()
