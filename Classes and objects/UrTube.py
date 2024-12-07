from User import *
from time import sleep


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.adult_age = 18

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Вы вошли как {user.nickname}')
                return
        print('Вы ошиблись при вводе логина или пароля либо вы не зарегистрированы в UrTube. Попробуйте еще раз.')

    def register(self, nickname, password, age):
        # в условии задачи сказано, что при регистрации проводится проверка на наличие записи с таким же логином И паролем
        # но проверять надо только логин. Потому что будет странно, если в системе будет два одинаковых логина но с разными паролями.
        # обычно логины пользователей все-таки уникальные.

        if any(user.nickname == nickname for user in self.users):
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f'Вы зарегистрированы в UrTube и вошли как {self.current_user}')

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, searchString):
        listOfVideos = []
        for video in self.videos:
            if searchString in video:
                listOfVideos.append(video)
        return listOfVideos

    def watch_video(self, title):
        for video in self.videos:
            if title == video.title:
                if not self.current_user:
                    print('Войдите в аккаунт или зарегистрируйтесь, чтобы смотреть видео')
                elif self.current_user.age < self.adult_age:
                    print('Вам нет 18 лет, покиньте пожалуйста страницу')
                else:
                    print('Начинаю проигрывание видео..')
                    for i in range(1, video.duration + 1):
                        video.time_now = i
                        print(f'{video.time_now} ', end='')
                        sleep(1)
                    print("Конец видео")
                    video.time_now = 0
