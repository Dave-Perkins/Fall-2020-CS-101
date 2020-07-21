"""
CS101 Webscraping Project Example
Gwen Urbanczyk
"""
from bs4 import BeautifulSoup
import requests

def get_actors(movie_num):
    """
    Function goes through the first movie_num movies on the IMDb top 1000 movies page.
    (movie_num must be a multiple of 50 and 0 < x <= 1000) and scrapes thier titles
    and cast member list.
    Returns a tuple of a list of titles and a list of actor lists.
    """
    if movie_num % 50 != 0:
        raise ValueError("movie_num must be a multiple of 50")
    if movie_num < 0 or movie_num > 1000:
        raise ValueError("movie_num must be between 0 and 1000")
    
    list_base_url = 'https://www.imdb.com/search/title/?groups=top_1000&'
    titles = []
    actor_lists = []
    
    for page in range(1, movie_num, 50):
        # Building the URL...
        url = list_base_url
        if page != 1:
            url += "start={}".format(page)
            
        # Scraping the source code
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        url_base = 'https://www.imdb.com'


        soup = soup.find('div', class_ = "lister-list")
        
        # For each movie on the page...
        for entry in soup.find_all('div', class_="lister-item mode-advanced"):
            # Get the link to the movie's page
            content = entry.find('div', class_="lister-item-content")
            title = content.h3.a.text
            url_extension = content.h3.a['href']
            
            # Get the source code off the movie's page
            new_url = url_base + url_extension
            source2 = requests.get(new_url).text
            soup2 = BeautifulSoup(source2, 'html.parser')
            cast_list = []
            
            soup2 = soup2.find('div', id = 'pagecontent').find('div', id = 'main_bottom')
            soup2 = soup2.find('div', id="titleCast").find('table', class_="cast_list")
            
            # For each cast member in the grid...
            for cast_member in soup2.find_all('tr'):
                name = cast_member.find('td', class_="")
                # Needed because sometimes there are empty entries
                if name:
                    name = name.a.text
                    name = name.strip()       
                    cast_list.append(name)
                    
            # Append to result a tuple of the title and the cast_list
            titles.append(title)
            actor_lists.append(cast_list)
            

    return (titles, actor_lists)


def main():
    """
    Program scrapes the IMDb top 1000 movies page for the movie's titles and
    list of cast members, then prompts the user to enter a movie title, then an actor
    from that movie, and outputs all the movies that include that actor. Users can continue
    to enter movies and actors until they choose to exit the prompt loop.
    
    Warning! Program is very slow, even with low number of movies (50-100)
    """
    
    print("Hello! Below, please enter the number of movies you want to scrape off of IMDb's " + \
          "top 1000 movies list. Please note that this number should be a multiple of 50, as " + \
          "the list is organized into pages of 50 movies each. Also note the larger the number, " + \
          "the longer the program will take.")
    print()
    movies_to_scrape = int(input("Please enter the number of movies you want to scrape: "))


    # Scrape the data off the IMDb site
    titles, actors = get_actors(movies_to_scrape)
    
    done = False

    # Menu Loop for find movies with a given actor in them
    while not done:
        user_in = input("Enter \'t\' to see list of titles, " + \
                        "enter title name to get actor list, enter nothing to exit: ")
        
        # exit
        if user_in == "":
            done = True
        # print list of titles
        elif user_in == "t":
            print(titles)
        # Enter sub-menu for actor selection
        elif user_in in titles:
            # Print the list of actors
            print(actors[titles.index(user_in)])
            actor = input("Enter a actor to find other movies with them in it: ")
            print()
            
            result = ""
            # Find all the other movies with that actor in them
            for actor_list in actors:
                current_title = titles[actors.index(actor_list)]
                if current_title != user_in:
                    if actor in actor_list:
                        result += current_title + '\n'
        
            result = result.rstrip('\n')
            
            # Output result
            if result != "":
                print("Here are some other movies with {} in them that you might like!".format(actor))
                print(result)
            else:
                print(("Sorry! I couldn't find any other movies with {} in them, try " + \
                      "increasing the number of movies to scrape!").format(actor))
                
        else:
            print("Oops! Sorry! Command or Movie not recognized!")
                
                
                
if __name__ == "__main__":
    main()