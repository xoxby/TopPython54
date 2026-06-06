from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    quotes = soup.find_all("div", class_="quote")
    data = []

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = quote.find("div", class_="tags").find_all("a")
        tag_list = []

        for tag in tags:
            tag_list.append(tag.text)

        data.append({
            "text": text,
            "author": author,
            "tags": ", ".join(tag_list),
        })

    return data


def write_csv(data):
    with open("quotes.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerow(["text", "author", "tags"])

        for quote in data:
            writer.writerow([quote["text"], quote["author"], quote["tags"]])


def main():
    url = "https://quotes.toscrape.com/"
    data = get_data(get_html(url))
    write_csv(data)
    print("Данные записаны в файл quotes.csv")
    print("Количество записей:", len(data))


if __name__ == "__main__":
    main()
