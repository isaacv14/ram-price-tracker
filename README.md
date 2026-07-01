# RAM Price Tracker

A scalable web scraping framework that tracks RAM memory prices across multiple marketplaces, filters outliers, and stores daily average prices in a TiDB cloud database.

## Features

- **Multi-Market Support**: Extensible architecture for scraping prices from Amazon, eBay, Best Buy, and Mercado Libre
- **Multiple Scraping Strategies**: Direct HTTP requests, headless browser (Playwright), or anti-bot proxy (Crawlbase)
- **Currency Conversion**: Automatic MXN to USD conversion using CurrencyAPI
- **Smart Filtering**: Outlier detection using percentile-based filtering (35th–95th percentile)
- **Price Analysis**: Statistical analysis with NumPy for accurate average calculations
- **Database Storage**: Daily price averages persisted to TiDB (MySQL-compatible) cloud database
- **Automated Pipeline**: Daily execution via GitHub Actions scheduled workflow

## Supported Markets

| Marketplace  | Region | Status     |
|--------------|--------|------------|
| Amazon       | USA    | ✅ Active  |
| eBay         | USA    | ✅ Active  |
| Best Buy     | USA    | ✅ Active  |
| Mercado Libre| Mexico | ❌ Inactive|

## Prerequisites

- Python 3.x
- A [CurrencyAPI](https://currencyapi.com/) API key (for MXN → USD conversion)
- A [Crawlbase](https://crawlbase.com/) API key (for anti-bot scraping)
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

3. Install Playwright Chromium browser:
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

For debugging a specific URL (inspect raw HTML and parsed prices):
```bash
python pytest.py
```

## Project Structure

```
.
├── main.py                          # Entry point — orchestrates scraping, filtering, and DB insertion
├── scraping.py                      # Web scraping logic (requests, Playwright, Crawlbase)
├── outlier_filter.py                # Outlier filtering using percentiles
├── database.py                      # TiDB connection and insert logic
├── schema.sql                       # Database DDL
├── pytest.py                        # Debug scraper for inspecting page structure
├── sites/                           # Marketplace adapter modules
│   ├── __init__.py
│   ├── amazon_us.py                 # Amazon US adapter
│   ├── ebay_us.py                   # eBay US adapter
│   ├── bestbuy_us.py                # Best Buy US adapter
│   └── mercado_libre_mx.py          # Mercado Libre Mexico adapter
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
2. Define the market-specific URL, CSS selector, and price cleaning function
3. Import and register the new market in `main.py`

## How It Works

1. **Scraping**: Fetches product listings from each marketplace using Crawlbase (or Playwright/requests as fallback) and extracts price elements
2. **Cleaning**: Normalizes price formats and converts MXN to USD via CurrencyAPI
3. **Filtering**: Removes outlier prices below the 35th percentile and above the 95th percentile
4. **Analysis**: Calculates the mean price from the filtered data
5. **Storage**: Inserts the daily average price into a TiDB database table with a timestamp

## TODO

- [ ] Add more marketplaces (Newegg, B&H, etc.)
- [ ] Add price history charting / visualization
- [ ] Add error handling and retries
- [ ] Add logging
- [ ] Add price alerts / notifications
