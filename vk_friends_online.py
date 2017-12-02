#!/usr/bin/env python
import getpass
import vk


APP_ID = 6280715


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
    list_friends_online = api.users.get(user_ids=friends_online)
    print('\nThere are friends online:')
    for friend in list_friends_online:
        print(' {} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = input('Input login: ')
    password = getpass.getpass('Input password: ')
    try:
        friends_online, api = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        pass
    except vk.exceptions.VkAPIError:
        print('Don\'t forget to input your username and password.')
    else:
        output_friends_to_console(friends_online, api)
