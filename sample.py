import time
import vk
import re
import json

session = vk.AuthSession(app_id='5108900', user_login='borisenkop@mail.ru', user_password='i23love56vk', scope='friends,messages,wall')

api = vk.API(session)

f = api.friends.getOnline()

#for i in range(len(f)):
#       s = api.users.get(user_ids=f[i])
#       last_name = re.search("(?<=last_name\': u\')(.*)(?=\'\,)", str(s))
#       last_name = last_name.group()
#       print last_name.decode('unicode-escape')
#       if last_name.decode('unicode-escape') == 'Nova':
#               print (str(s))
#       time.sleep(2)

#api.messages.send(user_id=25549196, message='Python server: Test, sir!')
api.wall.post(owner_id=-104885261, message='Python server: Test, sir!')