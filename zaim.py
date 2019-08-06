from requests_oauthlib import OAuth1Session
import datetime
import clipboard
import webbrowser
import keys

if __name__ == "__main__":

    callback_url = 'https://www.zaim.net'
    base_hostname = 'https://api.zaim.net'

    url = base_hostname + '/v2/home/user/verify'
    url_genre = base_hostname + '/v2/home/genre'
    url_category = base_hostname + '/v2/home/category'
    url_payment = base_hostname + '/v2/home/money/payment'

    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    access_token = keys.access_token
    access_token_secret = keys.access_token_secret
    oauth_verifier = keys.oauth_verifier


    status ='<Response [200]>'

    zaim_api = OAuth1Session(client_key=consumer_key,
                             client_secret=consumer_secret,
                             resource_owner_key=access_token,
                             resource_owner_secret=access_token_secret,
                             callback_uri=callback_url,
                             verifier=oauth_verifier
                             )

    now = datetime.datetime.now()
    date = '{0:%Y}-{0:%m}-{0:%d}'.format(now)

    price = clipboard.get()
    price = int(price)

    data = {
        'mapping': 1,
        'category_id': 43632945,
        'genre_id': 24135932,
        'amount': price,
        'date': date
    }

    res = zaim_api.post(url_payment, data=data)
    print(res)
    clipboard.set(str(res))
    webbrowser.open('workflow://')
