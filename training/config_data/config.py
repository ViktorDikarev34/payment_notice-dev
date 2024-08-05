from environs import Env
from dataclasses import dataclass

@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    tg_bot: TgBot

def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        )
    )

token_ms = '9c10e0dc4b1b681143e68c18a5f647e9b6480216'