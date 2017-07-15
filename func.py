#necessary functions

APP_ACCESS_TOKEN = '5697641738.df4661d.9c398ccb8a8445df89c3c9810f38f02b'

BASE_URL = 'https://api.instagram.com/v1/'

import requests, urllib

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'user_id: %s' % (user_info['data']['id'])
            print 'Username: %s' % (user_info['data']['username'])
            print 'Full name: %s' % (user_info['data']['full_name'])
            print 'Profile picture: %s' % (user_info['data']['profile_picture'])
            print 'Bio: %s' % (user_info['data']['bio'])
            print 'Total followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'Total users you are following: %s' % (user_info['data']['counts']['follows'])
            print 'Total posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'Invalid User'
    else:
        print 'Status code invalid'

#Function declaration to get the ID of a user by username
def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code invalid'
        exit()



#Function declaration to get the info of a user by username



def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'user_id: %s' % (user_info['data']['id'])
            print 'Username: %s' % (user_info['data']['username'])
            print 'Full name: %s' % (user_info['data']['full_name'])
            print 'Profile picture: %s' % (user_info['data']['profile_picture'])
            print 'Bio: %s' % (user_info['data']['bio'])
            print 'Total followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'Total users you are following: %s' % (user_info['data']['counts']['follows'])
            print 'Total posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'Users data is empty!'
    else:
        print 'Status code invalid'



#Function declaration to get your recent post



def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            for temp in own_media['data']:
                image_name = temp['id'] + '.jpeg'
                image_url = temp['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print 'Image downloaded'
        else:
            print 'Null post'
    else:
        print 'Status code invalid'



#Function declaration to get the recent post of a user by username



def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            for temp in user_media['data']:
                image_name = temp['id'] + '.jpeg'
                image_url = temp['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print 'Your image has been downloaded!'

        else:
            print 'No post available'
    else:
        print 'Status code invalid'


#Function declaration to get the ID of the recent post of a user by username


def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User not available'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    post = []
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            for temp in user_media['data']:
                post.append(temp['id'])
                return temp['id']
        else:
            print 'No recent post of the user'
            exit()
    else:
        print 'Status code invalid'
        exit()




#Function declaration to like the recent post of a user



def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Liked the post!'
    else:
        print 'Liked failed. Try again!'



#function declaration to get like list



def get_like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes/?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    r = requests.get(request_url).json()
    if r['meta']['code']==200:
        if len(r['data']):
            for temp in r['data']:
                print temp['username']
        else:
            print "Post does not exist"
    else:
        print "Error "



#Function declaration to make a comment on the recent post of the user



def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "New comment have been posted"
    else:
        print "Comment unsucessful"



#Function declaration to get a comment list



def get_comment_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    r = requests.get(request_url).json()
    if r['meta']['code'] == 200:
        if len(r['data']):
            for temp in r['data']:
                print "comment by %s : %s" % (temp['from']['username'],temp['text'])

        else:
            print "Post does not exist"
    else:
        print "Error "



#Function for user's interest based on hashtags analysis


'''
def user's_hastags(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print ('User doesn't exist in your sandbox','red')
    request_url = Base_url + 'users/' + user_id + '/media/recent/?access_token=' + APP_ACCESS_TOKEN
        print  ('GET request url:', request_url)
    item = 1
    flag = False
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
           for post in user_media['data']:
               if len(post['tags']):
                   flag = True
                   #caption = post['caption']
                   hash_tag['media_id'].append(post['id'])
                   hash_tag['words'].append(post['tags'])
        if (not flag):
           print ('No hashtags found')

'''