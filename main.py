# internal
import re
import time

# external
import flask
import twython

# local
from env import ENV


#INITS

# flask application
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = ENV['SECRET_KEY']

# twython object
twitter = twython.Twython(
    ENV['API_KEY'],
    ENV['API_SECRET'],
    ENV['ACCESS_TOKEN'],
    ENV['TOKEN_SECRET'],
)


# FUNCTIONS

def force_unfollow_fans(twitter):
    '''
    fans == people that follow you that you dont follow back

    we block and them unblock them to force an unfollow
    '''
    user_name = twitter.verify_credentials()['screen_name']
    followers = twitter.get_followers_ids()['ids']
    following = twitter.get_friends_ids()['ids']
    fans = set(followers) - set(following)

    for fan in fans:
        fan_name = twitter.lookup_user(user_id=fan)[0]['screen_name']
        twitter.create_block(user_id=fan)
        twitter.destroy_block(user_id=fan)
        print('@{} force unfollowed @{}'.format(user_name, fan_name))
        time.sleep(10) # to avoid going too far past the rate limit


# ROUTES

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login')
def login():
    print(flask.request.url_root)
    auth = twitter.get_authentication_tokens(callback_url=flask.request.url_root[:-1]+'/callback')
    flask.session['oauth_token']        = auth['oauth_token']
    flask.session['oauth_token_secret'] = auth['oauth_token_secret']
    return flask.redirect(auth['auth_url'])

@app.route('/callback')
def callback():
    twitter = twython.Twython(
        ENV['API_KEY'],
        ENV['API_SECRET'],
        flask.session['oauth_token'],
        flask.session['oauth_token_secret'],
    )
    auth_creds = twitter.get_authorized_tokens(flask.request.args['oauth_verifier'])
    twitter = twython.Twython(
        ENV['API_KEY'],
        ENV['API_SECRET'],
        auth_creds['oauth_token'],
        auth_creds['oauth_token_secret'],
    )
    force_unfollow_fans(twitter)
    return 'done!'


if __name__ == '__main__':
    app.run(
        debug=False,
        port=int(ENV['PORT']),
        host='0.0.0.0',
    )
