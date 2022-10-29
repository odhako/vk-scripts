import vk_api
from .data import VkData
from ..models import Group
from random import choice, randint


def get_id_and_type(url):
    session = vk_api.VkApi(token=VkData.TOKEN)
    vk = session.get_api()

    screen_name = url.split("/")[-1]
    print(screen_name)

    output = vk.utils.resolveScreenName(screen_name=screen_name)
    print(output)
    return output['object_id']


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

    groups = Group.objects.filter(active=True)
    if not groups:
        return
    random_group = choice(groups)
    url = random_group.url
    print(url)
    screen_name = url.split("/")[-1]
    print(screen_name)
    post = vk.wall.get(domain=screen_name, count=1)
    post_count = post['count']
    print('Post count: ', post_count)

    random_post = vk.wall.get(domain=screen_name,
                              count=1,
                              offset=randint(1, post_count))

    post_id = random_post['items'][0]['id']
    print('### Post id:', post_id)

    group_id = get_id_and_type(url)
    repost_object = f'wall-{group_id}_{post_id}'

    print('NEW')
    print(vk.wall.repost(object=repost_object, group_id=VkData.API_TEST_ID))


def get_random_post():
    session = vk_api.VkApi(token=VkData.TOKEN)
    vk = session.get_api()

    groups = Group.objects.filter(active=True)
    if not groups:
        return '/'
    random_group = choice(groups)
    url = random_group.url
    print(url)
    screen_name = url.split("/")[-1]
    print(screen_name)
    post = vk.wall.get(domain=screen_name, count=1)
    post_count = post['count']
    print('Post count: ', post_count)

    random_post = vk.wall.get(domain=screen_name,
                              count=1,
                              offset=randint(1, post_count))

    post_id = random_post['items'][0]['id']
    print('### Post id:', post_id)

    group_id = get_id_and_type(url)
    post = 'https://vk.com/' + f'wall-{group_id}_{post_id}'
    return post
