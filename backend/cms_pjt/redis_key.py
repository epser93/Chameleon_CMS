from django.core.cache import cache

class RedisKey():
    departemt = 'department'
    template = 'template'
    category = 'category*'
    category_customer = 'category:customer:'
    category_admin = 'category:admin:'
    item = 'item*'
    item_customer = 'item:customer:'
    item_admin = 'item:admin:'
    temp = 'temp*'
    temp_item = 'temp:item:'
    event = 'event*'
    event_admin = 'event:admin:'
    event_customer = 'event:customer:'
    notice = 'notice*'
    notice_admin = 'notice:admin:'
    notice_customer = 'notice:customer:'
    main = 'main*'
    main_admin = 'main:admin:'
    main_customer = 'main:customer:'
    carousel = 'carousel*'
    carousel_admin = 'carousel:admin:'
    carousel_customer = 'carousel:customer:'
    search = 'search*'
    search_customer = 'search:customer:'
    search_admin = 'search:admin:'
    user = 'user*'
    user_admin = 'user:'
    user_search = 'user:search:'
    remove_list = [category, item, temp, event, notice, main, carousel, search]

    @classmethod
    def remove_data(cls):
        print(1)
        for _type in cls.remove_list:
            cls.remove_keys(cache.keys(_type))

    @classmethod
    def remove_temp(cls):
        cls.remove_keys(cache.keys(cls.temp))


    @classmethod
    def remove_user(cls):
        cls.remove_keys(cache.keys(cls.user))


    @classmethod
    def remove_keys(cls, keys):
        for key in keys:
            cache.delete(key)