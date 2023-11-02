# Common Words Scraper

This is a Python-based web scraper that extracts and counts the occurrences of common words from a given URL. The script supports the use of proxies for scraping. It utilizes the `requests` and `BeautifulSoup` libraries for web scraping and parsing HTML content.

## ⚙️ Installation

You can download this project by either cloning the repository or downloading it as a ZIP file.

### Clone the Repository

git clone https://github.com/your_username/your_repository.git

### Download ZIP

You can also download the ZIP file by clicking on the green "Code" button in the GitHub repository and then selecting "Download ZIP".

After downloading, navigate to the project directory.

cd your_repository

Install the required packages:

pip install -r requirements.txt

## 🚀 Usage

To use the Common Words Scraper, run the script `common_scraper.py` and follow the instructions on the command line. The script allows you to specify a URL and choose the HTML elements to scrape.

python common_scraper.py

### 🔒 Proxies

You can specify proxies by providing the `--proxies` argument, followed by one or more proxies separated by commas.

python common_scraper.py --proxies=http://myproxy.com,https://myproxy.com

## 🛠️ Requirements

The script requires the following Python packages:

- `requests`
- `beautifulsoup4`

You can install the required packages using the following command:

pip install requests beautifulsoup4

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📌 Note

The script is for educational and informational purposes only. Make sure to comply with ethical web scraping practices and respect the terms of service of the websites you are scraping.
