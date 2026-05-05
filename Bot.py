import feedparser
import requests
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1501317101657522298/aVcFueGRvNyt7Rm1FWV-xnye5iYcFckAgwmCkevy-o15GjKYyLMoiIqx4_ArxA7QaVUh"

RSS_URL = "https://news.google.com/rss/search?q=fortnite&hl=es&gl=ES&ceid=ES:es"

enviados = set()

print("Bot iniciado...")

while True:
    feed = feedparser.parse(RSS_URL)

    for noticia in feed.entries[:5]:
        if noticia.link not in enviados:
            enviados.add(noticia.link)

            data = {
                "embeds": [
                    {
                        "title": noticia.title,
                        "url": noticia.link,
                        "description": "🟣 Fortnite News Update",
                        "color": 7506394
                    }
                ]
            }

            try:
                requests.post(WEBHOOK_URL, json=data)
                print("Enviado:", noticia.title)
            except Exception as e:
                print("Error:", e)

    time.sleep(45)
