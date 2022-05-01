from environs import Env

env = Env()
env.read_env()


class Config(object):
    BOT_TOKEN = env.str("BOT_TOKEN")
    ADMINS = env.list("ADMINS")
