# RAM Price Tracker

A scalable web scraping framework that tracks RAM memory prices across multiple marketplaces and analyzes price trends.

## Features

- **Multi-Market Support**: Extensible architecture for scraping prices from any marketplace
- **Currency Conversion**: Automatic price conversion to USD using CurrencyAPI
- **Smart Filtering**: Outlier detection using percentile-based filtering (35th-95th percentile)
- **Price Analysis**: Statistical analysis with NumPy for accurate average calculations
- **Modular Design**: Easy to add new markets and data sources

## Supported Markets

| Marketplace | Region | Status |
|-------------|--------|--------|
| Amazon | USA | ✅ Active |
| Ebay | USA | ✅ Active |
| Mercado Libre | Mexico | ❌ Inactive |
| *More coming soon...* | | |

## Prerequisites

- Python 3.x
- A [CurrencyAPI](https://currencyapi.com/) API key

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

3. Set up your environment variables:
```bash
cp .env.template .env
```

4. Add your CurrencyAPI key to `.env`:
```
CURRENCY_MX_API_KEY=your_api_key_here
```

## Usage

Run the main script:
```bash
python main.py
```

## Project Structure

```
.
├── main.py                          # Entry point - orchestrates scraping and analysis
├── scrapping.py                     # Web scraping logic using BeautifulSoup
├── outlier_filter.py                # Outlier filtering using percentiles
├── cleaning_scrapping/
│   ├── __init__.py
│   └── mercado_libre_mx.py          # Mercado Libre Mexico market adapter
├── .env                             # Environment variables (gitignored)
├── .env.template                    # Template for environment variables
└── requirements.txt                 # Python dependencies
```

## Adding a New Market

The modular architecture makes it easy to add new marketplaces:

1. Create a new adapter file in `cleaning_scrapping/` (e.g., `amazon_us.py`)
2. Define the market-specific config and price cleaning logic
3. Register the new market in the main scraper

## How It Works

1. **Scraping**: Fetches product listings from configured marketplaces and extracts price elements
2. **Cleaning**: Normalizes price formats and converts local currencies to USD
3. **Filtering**: Removes outlier prices below the 35th percentile and above the 95th percentile
4. **Analysis**: Calculates average prices from the filtered data across all active markets

## TODO

- [ ] Add support for more marketplaces (Amazon, Newegg, etc.)
- [ ] Save results to database
- [ ] Add price history tracking
- [ ] Add error handling and retries
- [ ] Add logging
