import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/scraper", methods=["GET"])
def scrape_falabella():
    url = "https://www.falabella.com/falabella-cl/search?Ntt=descuento"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "No se pudo obtener los datos"}), 500

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    for product in soup.select(".pod-details"):
        name = product.select_one(".pod-title").text.strip()
        price = product.select_one(".pod-prices span").text.strip()
        link = "https://www.falabella.com" + product.select_one("a")["href"]

        products.append({"name": name, "price": price, "url": link})

    return jsonify(products)

if __name__ == "__main__":
    app.run()
