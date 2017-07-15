# Determine user's interest
# Based on hash_tag analysis of recent post
# Plot the data using matplotlib
from matplotlib import pyplot as p
import requests
app_access_token = '5697641738.df4661d.9c398ccb8a8445df89c3c9810f38f02b'
base_url = 'https://api.instagram.com/v1/'

def line_plot(filt_word):
    x = range(len(filt_word))

    y = [filt_word.count(w) for w in filt_word] # Storing the frequency of occurence

    p.xlabel("Hash_tags")
    p.ylabel("Occurence of hash_tags")
    p.title("User's interest based on hash_tag analysis")
    p.plot(x,y,'or')
    p.plot(x,y,'b')
    p.show()

def users_interest(username):
    req = (base_url + 'users/search/?q=%s&access_token=%s') % (username,app_access_token)
    raw = requests.get(req).json() # Requesting
    if raw['meta']['code']==200:
        if len(raw['data']):
            user_id = raw['data'][0]['id']  # Fetching user_id
        else:
            print "No user"
    else:
        print "Error"
    req1 = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id,app_access_token)
    raw1 = requests.get(req1).json() # Requesting
    hash_tags = []
    data = []
    post = int(raw_input("Enter no of post to analyse :"))
    if raw1['meta']['code']==200:
        if len(raw1['data']):
            for temp in raw1['data']:
                if post==0:
                    break
                hash_tags.append(temp['tags']) # Appending hash_tag in list
                post = post-1
                for tags in temp['tags']:
                    data.append(tags)   # Ordered hash_tag appended in list
                    print tags
        else:
            print "No Post"
    else:
        print "Error"

    # Analysing hash_tags for 
    def analyse_data(data):
       
        # Splitting the ordered data on the basis of upper_case letters 
        u_pos = []
        words = []
        for tmp in data:
            for i, char in enumerate(tmp):
                if char.isupper():   # If the character of the tag is upper_case
                    u_pos.append(i)  # Fetching position_id of the upper case letters
            for count in range(len(u_pos)):
                print count
                # Using Error handling for the last item during the below list comprehension 
                try:
                    words.append(tmp[u_pos[count]:u_pos[count + 1]]) # Appending splitted words(Starting with uppercase letter)using list comprehension
                except IndexError:
                    words.append(tmp[u_pos[count]:])  # Appending split during the last                              
                                                      #  position of the list(List comprehension)


    # Filtering the data(splitted words) by checking for words present in dictionary 
    def checkword(data):

        import enchant    # Enchant lib for checking words present in dictionary
        dict_word = enchant.Dict("en-US")   # Dictionary instance created
        word = []
        dis = ''
        for temp in data:

            for c in temp:
                dis = dis + c    # Appending every letter in dis untill the conditions is true
                if len(dis)>3:   # Ignoring words less than or equal to 3 letters
                    if dict_word.check(dis):    # Checking for words present in dictionary
                        word.append(dis)        # Appending the present words in a list

            dis=''  # Reinitiating dis for next english word 
        print word  # Printing filtered list words (those present in dictionary)
        
        # Stopwords a py file which are the list of words that have no major meaning or which doesnot describe the main type        
        import stopwords
        filt_word = []
        for w in word:
            if w not in stopwords.stopwords:   # Checking for filtered words in the stopword's list
                filt_word.append(w)            # If not, appending to a new list
        print filt_word                        # New filtered data
        
        # Checking for similiar words (like rain,raining,rainy,etc)
        for i,temp in enumerate(filt_word):
            try:
                if filt_word[i] in filt_word[i+1]: # Checking if the initial word is present in the next word 
                    del filt_word[i]               # If present,delete the initial one
            except IndexError:
                break
        print filt_word  # filtered_data_next stage
        
        
        # Checking for the frequency of occurence of every words in filt_word list
        frequency = []   
        for temp in filt_word:
            freq = {temp:filt_word.count(temp)}     # Creating dictionary and storing the newly filtered words with their frequency of occurence
            frequency.append(freq)                  # Appending dictionary in the new list     
            print "Hash_tag :%s [freq :%d]" % (temp,freq[temp])     # Printing the hash tags and the frequency of it

        line_plot(filt_word)   # Function to display the graph based on the hashtag and their frequency
    checkword(data)


users_interest("neogchiranjeev")
