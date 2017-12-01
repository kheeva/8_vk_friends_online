#!/usr/bin/env python
import getpass
import vk


APP_ID = 6280715


def get_user_login(login=input('Input login: ')):
    return login


def get_user_password(password=getpass.getpass('Input password: ')):
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    return api.friends.getOnline(), api


def output_friends_to_console(friends_online, api):
    json_friends_online = api.users.get(user_ids=friends_online)
    for friend in json_friends_online:
        print('\nThere are friends online:')
        print(' {} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online, api = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        pass
    else:
        output_friends_to_console(friends_online, api)
