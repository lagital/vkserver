__author__ = 'agita'

# Modules
import settings
import sys
import vk
from random import randint
import time

# Classes for quiz types. Do not forget to add a new ones.
from Question import WWW_question

class Manager:

    def __init__(self, login, pwd):
        self.pool = []
        self.pool_posted = []
        self.LIFETIME = settings.LIFETIME
        self.Q_TYPES = settings.Q_TYPES
        self.api = self.connect(login, pwd)
        self.login = login
        self.pwd = pwd

    def connect(self, login, pwd):
        session = vk.AuthSession(app_id=settings, user_login=login, user_password=pwd, scope=settings.SCOPE)
        api = vk.API(session)
        return api

    def post_next(self):
        length = len(self.pool)
        if length > 0:
            pos = randint(0, length)
            if self.pool[pos].type == 1:

                try:
                    self.pool[pos].post_id = self.api.wall.post(owner_id=settings.APP_ID,
                                                        message=self.pool[pos].encode('UTF-8'))
                    self.pool_posted.append(self.pool[pos])
                    self.pool.remove(pos)
                except:
                    self.connect()
                    self.post_next()
            # else for each new quiz type
        elif length == 0:
            self.refill_pool()
            self.post_next()

    def refill_pool(self):
        if len(self.pool) == 0:
            for c in self.Q_TYPES:
                self.pool.append(self.get_class_obj(c))

    def raise_counts(self):
        for q in self.pool_posted:
            if (q.lifetime >= 0) and (q.lifetime < self.LIFETIME):
                q.lifetime = q.lifetime + 1
            elif q.lifetime == self.LIFETIME:
                self.leave_comment(q)
            else:
                self.raise_error('Question counter is invalid.', 0)

    def leave_comment(self, q):
        comment_id = 0
        if q.type == 1:
            try:
                comment_id = self.api.wall.addComment(owner_id=settings.APP_ID, post_id=int(q.post_id[u'post_id']), text='A: ' +
                                        q.answer.encode('UTF-8') + '\n' + 'K: ' + q.comment.encode('UTF-8'))
            except:
                self.connect()
                comment_id = self.leave_comment(q)
        # TODO: add error handling
        return comment_id


        # else for each new quiz type

    def monitoring(self, login, pwd):
        self.refill_pool()
        while (1):
            self.post_next()
            self.raise_counts()
            for q in self.pool_posted:
                if q.lifetime == self.LIFETIME:
                    c = self.leave_comment(q)
                    if c != 0:
                        self.pool_posted.remove(q)
            time.sleep(600)

    def raise_error(self, text, type):
        if type == 0:
            with open("log.txt", "a") as myfile:
                myfile.write("ERROR: " + text)
        elif type == 1:
            with open("log.txt", "a") as myfile:
                myfile.write("WARNING:" + text)

    def get_class_obj(self, c):
        tClass = getattr(sys.modules[__name__], c)
        m = tClass()
        return m

if __name__ == "__main__":
    print ('In test ...')
    M = Manager('t', 'p')
    print (M.Q_TYPES[0])
    M.post_next()
    M.refill_pool()
    print (len(M.pool))