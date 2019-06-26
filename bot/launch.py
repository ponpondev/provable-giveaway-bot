# import discord
import traceback
from bot.bot import CustomBot
from django.conf import settings


def launcher():
    prefix = '.' if settings.DEBUG is True else settings.BOT_PREFIX

    bot = CustomBot(command_prefix=prefix, owner_id=209551520008503297)
    # remove the default 'help' command
    bot.remove_command('help')

    # Initialize extension (command) packages
    initial_extensions = (
        'bot.cogs.giveaway',
        'bot.cogs.help',
        'bot.cogs.owner',
        'bot.cogs.pfair',

        'bot.tasks.giveawaytask',

    )
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception:
            traceback.print_exc()

    bot.run(settings.BOT_TOKEN)