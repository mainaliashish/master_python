# url = http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from csv import writer
# from time import sleep
from random import choice

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        response = requests.get(f"{BASE_URL}{url}")
        print(f"Now Scraping : {BASE_URL}{url}...")
        soup = BeautifulSoup(response.text, "html.parser")  
        quotes = soup.find_all(class_="quote")


        for quote in quotes:
            all_quotes.append({
                "text" : quote.find(class_="text").get_text(),    
                "author" : quote.find(class_="author").get_text(),
                "bio_url" : quote.find("a")["href"] 
            })
        next_btn = soup.find(class_="next")    
        url = next_btn.find("a")["href"] if next_btn else None
        # sleep(2)
    return all_quotes


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a Quote : ")
    print(quote["text"])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this Quote? Guesses remaining : {remaining_guesses} \n ")
        if guess == quote["author"].lower():
            print("You guess was Correct!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio_url']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_location = soup.find(class_="author-born-location").get_text() 
            print(f"Here is a hint : The author was born on {birth_date} in {birth_location}")
        elif remaining_guesses == 2:
            print(f"The author first name starts with : {quote['author'][0] }") 
        elif remaining_guesses == 1:
            last_hint = quote["author"].split(" ")[1][0]
            print(f"The author's last name starts with : {last_hint}") 
        else:
            print("Sorry You ran out of guesses..")
            print(f"The author of the quote is : {quote['author']}")
        

    again = ''    
    while again.lower() not in ('y', "yes", 'n', "no"):
        again = input("Would you like to play again (y/n) ? \n")
        
    if again.lower() in ('y', "yes"):
        return start_game(quote)
    else:
        print("Goodbye! See You soon..")


quotes = scrape_quotes()
start_game(quotes)