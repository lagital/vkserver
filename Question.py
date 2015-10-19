__author__ = 'agita'

class Question:

    def __init__(self):
        self.text = ''
        self.answer = ''
        self.comment = ''
        self.ans_list = []
        self.pictures = []
        self.pictures_and = []
        self.lifetime = 0
        self.post_id = 0
        self.type = None

    def load(self):
        return

    def check(self):
        return

class WWW_question (Question):

    def __init__(self):
        Question.__init__(self)
        self.text = ''
        self.answer = ''
        self.comment = ''
        self.ans_list = []
        self.pictures = []
        self.pictures_and = []
        self.lifetime = 0
        self.post_id = 0
        self.type = 0

    def load(self):
        return

if __name__ == "__main__":
    print ('In test ...')
    Q = Question()
    wq = WWW_question()
    wq.check()

