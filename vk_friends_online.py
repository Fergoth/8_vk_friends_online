import vk
import getpass
import sys

APP_ID = 6941791  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


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
    )
    api = vk.API(session, v='5.95')
    friends_info = api.friends.get(fields='online')['items']
    friends_online = [
        (friend['first_name'], friend['last_name'])
        for friend in friends_info
        if friend['online']
    ]
    return friends_online


def output_friends_to_console(friends_online):
    print('Друзья онлайн: ')
    for name, second_name in friends_online:
        print('{:^20}{:^20}'.format(name, second_name))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        sys.exit('Ошибка авторизации')
    output_friends_to_console(friends_online)
