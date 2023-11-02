# Common Scraper

This is a Python-based web scraper that extracts and counts the occurrences of common words from a given URL. The script supports the use of proxies for scraping. It utilizes the `requests` and `BeautifulSoup` libraries for web scraping and parsing HTML content.

## ⚙️ Installation

You can download this project by either cloning the repository or downloading it as a ZIP file.

### Install the required packages:
```
pip install requests beautifulsoup4
```

### Clone the Repository
```
git clone https://github.com/gamemaster123356/CommonScraper.git
```

After downloading, you can navigate to the project directory.
```
cd CommonScraper
```

OR

### Download ZIP

You can also download the ZIP file by clicking on the green "Code" button in the GitHub repository and then selecting "Download ZIP".

After downloading and extracting, you can navigate to the project directory.
```
cd CommonScraper-main
```

## 🚀 Usage

To use the Common Words Scraper, run the script `common_scraper.py` and follow the instructions on the command line. The script allows you to specify a URL and choose the HTML elements to scrape.
```
python commonscraper.py
```

### 🔒 Proxies

You can specify proxies by providing the `--proxies` argument, followed by one or more proxies separated by commas.
```
python commonscraper.py --proxies=http://myproxy.com,https://myproxy.com
```

## 🖼️ Screenshots
![Screenshot 1](https://github.com/gamemaster123356/CommonScraper/blob/github-assets/screenshot1.png)

![Screenshot 2](https://github.com/gamemaster123356/CommonScraper/blob/github-assets/screenshot2.png)

![Screenshot 3](https://github.com/gamemaster123356/CommonScraper/blob/github-assets/screenshot3.png)

## 🛠️ Requirements

The script requires the following Python packages:

- `requests`
- `beautifulsoup4`

You can install the required packages using the following command:
```
pip install requests beautifulsoup4
```

## 📝 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 📌 Note

The script is for educational and informational purposes only. Make sure to comply with ethical web scraping practices and respect the terms of service of the websites you are scraping.
