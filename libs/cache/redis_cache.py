# -*- coding : utf-8 -*-

import redis

class redisCache :
    def get_drive(self):
        r = redis.StrictRedis(host='r-2zey9h0uvci82hmn9bpd.redis.rds.aliyuncs.com', port=6379, db=1, password='CLOUD7092qaz@!#')
        return r