from termcolor import colored
print colored('\n\t\t\t\tPassword is chinku','magenta',attrs=['bold'])

def pas():
    i=True
    while i:
        z = raw_input('Enter password:')

        if z == 'chinku':
            print'Welcome to Instabot'
            break
        elif z != 'chinku':
            print'Invalid Password\n\tTry Again'

pas()


APP_ACCESS_TOKEN = '5697641738.df4661d.9c398ccb8a8445df89c3c9810f38f02b'

BASE_URL = 'https://api.instagram.com/v1/'

import requests


from func import self_info,get_user_id,get_user_info,get_own_post,get_user_post,get_post_id,like_a_post,post_a_comment,get_like_list,get_comment_list
from obj import line_plot,users_interest

def bot_start():
    while True:
        print '\n'
        print colored('-----///Lets_get_instabot_started\\\-----','blue',attrs=['bold'])
        choo = raw_input("a.Self Info\nb.Sandbox Users\nc.Hashtag Analysis of a user\nd.Exit\n *Enter your choice:")
        if choo == "a":
            print "1.Get your own details\n"
            print "2.Get your own recent post\n"
            choice = raw_input("Enter you choice: ")
            if choice == "1":
                self_info()
            elif choice == "2":
                get_own_post()

        elif choo == 'b':
            print "1.Get details of a user by username\n"
            print "2.Get the recent post of a user by username\n"
            print "3.Like the recent post of a user\n"
            print "4.Get a list of people who have liked the recent post of a user\n"
            print "5.Make a comment on the recent post of a user\n"
            print "6.Get a list of comments on the recent post of a user\n"
            choice = raw_input("Enter you menu choice: ")
            if choice == "1":
                insta_username = raw_input("Enter the username of the user: ")
                get_user_info(insta_username)
            elif choice == "2":
                insta_username = raw_input("Enter the username of the user: ")
                get_user_post(insta_username)
            elif choice == "3":
                insta_username = raw_input("Enter the username of the user: ")
                like_a_post(insta_username)
            elif choice == "4":
                insta_username = raw_input("Enter the username of the user: ")
                get_like_list(insta_username)
            elif choice == "5":
                insta_username = raw_input("Enter the username of the user: ")
                post_a_comment(insta_username)
            elif choice == "6":
                insta_username = raw_input("Enter the username of the user: ")
                get_comment_list(insta_username)
        elif choo == 'c':
            print ":::Starting hashtag _ analysis :::"
            insta_username = raw_input("Enter username :")
            users_interest(insta_username)
        elif choo == 'd':
            print "Thank You for using Instabot"
            exit()
bot_start()
