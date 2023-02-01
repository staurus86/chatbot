import openai
import telebot

openai.api_key = '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'
bot = telebot.TeleBot("6197915948:AAFKPBzqEAT6enKOK4A4kC8O7XMZ2tyIoPA")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=1024,
        top_p=1.0,
        temperature=0.5,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )

    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

bot.polling()
