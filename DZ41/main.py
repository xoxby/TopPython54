from bs4 import BeautifulSoup
import requests
import csv


class Parser:
    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name

    def get_html(self, url):
        r = requests.get(url)
        return r.text

    def get_data(self, html):
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

    def write_csv(self, data):
        with open(self.file_name, "a", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\n")

            for quote in data:
                writer.writerow([quote["text"], quote["author"], quote["tags"]])

    def run(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\n")
            writer.writerow(["text", "author", "tags"])

        count = 0

        for page in range(1, 4):
            url = f"{self.url}/page/{page}/"
            data = self.get_data(self.get_html(url))
            self.write_csv(data)
            count += len(data)

        print("Данные записаны в файл", self.file_name)
        print("Количество записей:", count)


def main():
    pars = Parser("https://quotes.toscrape.com", "quotes_pages.csv")
    pars.run()


if __name__ == "__main__":
    main()
