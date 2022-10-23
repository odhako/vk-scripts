import vk_api
from vk_scripts.reposter.modules.data import VkData


def print_console():
    print('Ten seconds passed.')


def get_screen_name_id(url):
    session = vk_api.VkApi(token=VkData.TOKEN)
    vk = session.get_api()

    screen_name = url.split("/")[-1]
    print(screen_name)

    output = vk.utils.resolveScreenName(screen_name=screen_name)
    print(output)


def repost_test():
    session = vk_api.VkApi(token=VkData.TOKEN)
    vk = session.get_api()

    post = vk.wall.get(owner_id=VkData.ROMAODHAKO_ID, count=1, offset=2)
    post_id = post['items'][0]['id']
    print('### Post id:', post_id)

    repost_object = f'wall{VkData.ROMAODHAKO_ID}_{post_id}'

    print(vk.wall.repost(object=repost_object, group_id=VkData.API_TEST_ID))


def repost_random():
    session = vk_api.VkApi(token=VkData.TOKEN)
    vk = session.get_api()




# if __name__ == '__main__':
#     get_screen_name_id('https://vk.com/id2977889')
