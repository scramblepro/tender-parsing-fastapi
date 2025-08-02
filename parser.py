from bs4 import BeautifulSoup
import requests
from database import insert_tender

def get_tenders():
    for page in range(1, 6):  
        url = f"https://rostender.info/extsearch?page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"[!] Ошибка запроса: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", class_="tender-row row")

        for article in articles:
            try:
                # Номер тендера
                number_tag = article.find("span", class_="tender__number")
                number = number_tag.text.strip().replace("Тендер", "").replace("№", "").strip() if number_tag else ""

                # Заголовок и ссылка
                title_tag = article.find("a", class_="tender-info__description")
                title = title_tag.text.strip() if title_tag else ""
                link = "https://rostender.info" + title_tag["href"] if title_tag else ""

                # Начальная цена
                price_tag = article.find("div", class_="starting-price--price")
                price = price_tag.text.strip().replace("\xa0", " ") if price_tag else None

                # Регион
                region_tag = article.find("div", class_="tender-address")
                region = region_tag.text.strip() if region_tag else ""

                # Заказчик
                customer_tag = article.find("div", class_="tender-costomer-branch")
                customer = customer_tag.text.strip() if customer_tag else ""

                # Дата окончания
                deadline_tag = article.find("span", class_="tender__countdown-text")
                deadline_date = ""
                if deadline_tag:
                    deadline_parts = deadline_tag.text.split(" ")
                    for part in deadline_parts:
                        if "." in part and len(part.strip()) == 10:
                            deadline_date = part.strip()
                            break

                # Дата начала
                start_tag = article.find("span", class_="tender__date-start")
                start_date = start_tag.text.replace("от", "").strip() if start_tag else ""

                data = {
                    "number": number,
                    "title": title,
                    "link": link,
                    "price": price,
                    "region": region,
                    "customer": customer,
                    "deadline_date": deadline_date,
                    "start_date": start_date
                }

                insert_tender(data)
            except Exception as e:
                print(f"[!] Ошибка при обработке тендера: {e}")
