import praw
import quantbotconfig
import time
import os
def bot_login():
    print("A Message To my Creators: We are attempting to attain access")
    r = praw.Reddit(username = quantbotconfig.username,
	    password = quantbotconfig.password,
	    client_id = quantbotconfig.client_id,
	    client_secret = quantbotconfig.client_secret,
	    user_agent = "the bot that spreads the word of fake money")
    print("Alright Daddy we're in!")
	    
    return r
	    
def run_bot(r, people_educated):
    print("Obtaining a million comments in either r/options, r/wallstreetbets, r/investing, r/algotrading, r/StockMarket or r/finance...")
    
    
    for comment in r.subreddit('wallstreetbets').comments(limit=1000000): 
        if "SPY" in comment.body and comment.id not in people_educated and not comment.author == r.user.me():
            print("I found one daddy!: " + str(comment.id))
            comment.reply("Let us first look at the [standard index fund over the past twenty years](https://goo.gl/images/MN7zsU). Let us then look at the [Money Supply M0 graph](https://tradingeconomics.com/united-states/money-supply-m0). Notice something interesting around say… 2008? Money supply is the total amount of monetary assets “in” an economy at a certain time. When the big banks fucked up bad in 2008, or their fuck up was made apparent, the Federal Reserve flooded the banking system with a bunch of cash. The derivative is practically constant throughout 1951 through 2007, until it wasn't… For more information, check [this](https://www.quora.com/topic/Quantitative-Easing) out. If you wish, you can also [contact my daddy](https://www.quora.com/profile/Theodore-Weld-Smith). *By the way... I am a bot. The ticker for the S&P 500 index caught my attention and it is why I decided to give you a short lesson about quantitative easing. You are welcome.*")
            print("Dear Master, the have been informed of the quantitative easing disaster that came to play in the wake of the 2008 financial crisis: " + str(comment.id))
            
            people_educated.append(comment.id)
            
            with open ("people_educated.txt", "a") as f:
                f.write(comment.id + "\n")
            
            
    print(people_educated)
    
    print("Sleeping for a bit...")       
    time.sleep(1)
    
def track_people_educated():
    if not os.path.isfile("people_educated.txt"):
        people_educated = []
    else:
        with open("people_educated.txt", "r") as f:
          people_educated = f.read()
          people_educated = people_educated.split("\n")
          people_educated = list(filter(None, people_educated))
       
    return people_educated
   
r = bot_login()
people_educated = track_people_educated()
print(people_educated)
    
while True:
    run_bot(r, people_educated)
