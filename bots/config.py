import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv("Gf9KC0aZoiqu4eBC2YaYr")
    consumer_secret = os.getenv("U4w9dwJ5ta9TK6YZ2AuEgxIAXZzyl1HCROorrq2m")
    access_token = os.getenv("1217447530813890560-XIck0nW7qaRreIs5Ef1NUU")
    access_token_secret = os.getenv("uU3pkdPRuOGj0ENzdbjCUKzY7CaRIRWmrI")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api