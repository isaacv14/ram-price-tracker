# RAM Price Tracker

A scalable web scraping framework that tracks RAM memory prices across multiple marketplaces, analyzes price trends, and stores results in a TiDB database.

## Features

- **Multi-Market Support**: Extensible architecture for scraping prices from Amazon, eBay, Best Buy, and Mercado Libre
- **Three Scraping Engines**: Requests + BeautifulSoup, Playwright (dynamic content), and Crawlbase (anti-scraping bypass)
- **Currency Conversion**: Automatic MXN to USD conversion using CurrencyAPI
- **Smart Filtering**: Outlier detection using percentile-based filtering (35th–95th percentile)
- **Price Analysis**: Statistical analysis with NumPy for accurate average calculations
- **Database Storage**: Daily price averages persisted to TiDB (MySQL-compatible) cloud database
- **Automated Pipeline**: Daily execution via GitHub Actions scheduled workflow
- **Modular Design**: Easy to add new markets and data sources

## Supported Markets

| Marketplace  | Region | Status     |
|--------------|--------|------------|
| Amazon       | USA    | ✅ Active  |
| eBay         | USA    | ✅ Active  |
| Best Buy     | USA    | ✅ Active  |
| Mercado Libre| Mexico | ✅ Active  |

## Prerequisites

- Python 3.x
- A [Crawlbase](https://crawlbase.com/) API key
- A [CurrencyAPI](https://currencyapi.com/) API key (for MXN → USD conversion)
- A [TiDB Cloud](https://tidbcloud.com/) database (for storing results)

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd ram-price-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browser binaries:
   ```bash
   playwright install chromium
   ```

4. Set up your environment variables:
   ```bash
   cp .env.template .env
   ```

5. Add your API keys and TiDB credentials to `.env`:
   ```
   CURRENCY_MX_API_KEY = your_currency_mx_api_key_here
   TIDB_USER="your_user_prefix.root"
   TIDB_PASSWORD="your_password_here"
   TIDB_HOST="your_tidb_host_address"
   TIDB_PORT=4000
   TIDB_DATABASE="your_database_name"
   CRAWLBASE_API_KEY="your_crawlbase_api_key_here"
   ```

6. Create the database table:
   ```bash
   mysql -h your_tidb_host -P 4000 -u your_user -p < schema.sql
   ```

## Usage

Run the full pipeline:
```bash
python main.py
```

The script will:
1. Scrape RAM prices from all configured marketplaces
2. Filter outliers per site (35th–95th percentile)
3. Calculate the overall average price
4. Insert the daily average into the database

For debugging a specific URL (inspect raw HTML and parsed prices):
```bash
python pytest.py
```

## Project Structure

```
.
├── main.py                          # Entry point — orchestrates scraping, filtering, and DB insert
├── scraping.py                      # Scraping engines (requests, Playwright, Crawlbase)
├── outlier_filter.py                # Outlier filtering using percentiles
├── database.py                      # TiDB connection and daily price insert
├── schema.sql                       # Database table schema
├── pytest.py                        # Debug script for testing scrapers
├── sites/                           # Marketplace adapters
│   ├── __init__.py
│   ├── amazon_us.py                 # Amazon US adapter
│   ├── ebay_us.py                   # eBay US adapter
│   ├── bestbuy_us.py                # Best Buy US adapter
│   └── mercado_libre_mx.py          # Mercado Libre Mexico adapter (with MXN→USD conversion)
├── .github/workflows/
│   └── python-app.yml               # GitHub Actions scheduled workflow
├── .env                             # Environment variables (gitignored)
├── .env.template                    # Template for environment variables
├── .gitignore                       # Git ignore rules
└── requirements.txt                 # Python dependencies
```

## Adding a New Market

The modular architecture makes it easy to add new marketplaces:

1. Create a new adapter file in `sites/` (e.g., `newegg_us.py`)
2. Define `url`, `html_element`, `html_class`, and a `cleaning_function`
3. Import the adapter and add it to the `sites` list in `main.py`

## Scraping Methods

- **`Scraping`** — Basic requests + BeautifulSoup for simple pages
- **`PlayWrightScraping`** — Headless Chromium for JavaScript-rendered content
- **`CrawlbaseScrape`** — Crawlbase API for sites with aggressive anti-scraping measures

## How It Works

1. **Scraping**: Fetches product listings from configured marketplaces using Crawlbase (or Playwright/requests as fallback) and extracts price elements
2. **Cleaning**: Normalizes price formats and converts MXN to USD via CurrencyAPI
3. **Filtering**: Removes outlier prices below the 35th percentile and above the 95th percentile per site
4. **Analysis**: Calculates the mean price from the filtered data across all active markets
5. **Storage**: Inserts the daily average price into TiDB for historical tracking

## TODO

- [ ] Add more marketplaces (Newegg, Micro Center, B&H, etc.)
- [ ] Add price history charting / visualization
- [ ] Add error handling and retries with backoff
- [ ] Add logging
- [ ] Add data visualization / dashboard
- [ ] Add price alerts / notifications
