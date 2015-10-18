import time
import vk
import re
import json

session = vk.AuthSession(app_id='test', user_login='test', user_password='test', scope='friends,messages,wall')

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

#api.messages.send(user_id=test, message='Python server: Test, sir!')
api.wall.post(owner_id=test, message='Python server: Test, sir!')