from bot import create_bot


def main():
    bot = create_bot()
    bot.start_polling()


if __name__ == "__main__":
    main()
