def top_10_retweets():
    """
    Find the 10 most retweeted tweets.
    """
    pass

def top_10_users_by_tweets():
    """
    Find the 10 most active users.
    """
    pass

def top_10_days_by_tweets():
    """
    Find the 10 most active days.
    """
    pass

def top_10_hashtags():
    """
    Find the 10 most used hashtags.
    """
    pass

if __name__ == "__main__":
    the_input = 5
    while the_input != 0:
        print("Select a function to run:")
        print("1. Top 10 Retweets")
        print("2. Top 10 Users by Tweets")
        print("3. Top 10 Days by Tweets")
        print("4. Top 10 Hashtags")
        print("0. Exit")
        the_input = int(input("Enter a number: "))
        if the_input == 1:
            top_10_retweets()
        elif the_input == 2:
            top_10_users_by_tweets()
        elif the_input == 3:
            top_10_days_by_tweets()
        elif the_input == 4:
            top_10_hashtags()
        elif the_input == 0:
            print("Exiting...")
            break
        else:
            print("Invalid input")
            continue