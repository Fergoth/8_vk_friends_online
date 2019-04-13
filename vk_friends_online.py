import vk
import getpass
import sys

APP_ID = -1  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    username = input('Введите имя пользователя вк\n')
    return username


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope=2,
    )
    api = vk.API(session, v='5.95')
    friends_online_ids = api.friends.getOnline()
    friends_online  = api.users.get(user_ids=friends_online_ids)
    return friends_online


def output_friends_to_console(friends_online):
    print('Друзья онлайн: ')
    for friend in friends_online:
        print('{:^20}{:^20}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    #ogin = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        sys.exit('Ошибка авторизации')
    output_friends_to_console(friends_online)
