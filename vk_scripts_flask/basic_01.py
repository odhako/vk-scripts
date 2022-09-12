import json
import vk_api
from data import VkData


session = vk_api.VkApi(token=VkData.TOKEN)
vk = session.get_api()

post = vk.wall.get(owner_id=VkData.ROMAODHAKO_ID, count=1, offset=2)
post_id = post['items'][0]['id']
print('### Post id:', post_id)

repost_object = f'wall{VkData.ROMAODHAKO_ID}_{post_id}'

print(vk.wall.repost(object=repost_object, group_id=VkData.API_TEST_ID))
