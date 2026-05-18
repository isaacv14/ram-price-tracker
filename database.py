import os
import mysql.connector
import certifi
from dotenv import load_dotenv


# Load the variables from the local .env file into the script's memory environment
load_dotenv()

# Safely read the environment variables
config = {
    'user': os.getenv('TIDB_USER'),
    'password': os.getenv('TIDB_PASSWORD'),
    'host': os.getenv('TIDB_HOST'),
    'port': int(os.getenv('TIDB_PORT', 4000)), # Fallback default port is 4000
    'database': os.getenv('TIDB_DATABASE'),
    'ssl_verify_cert': True, # Required for secure TiDB Cloud connections
    
    # Point directly to certifi's certificatle bundle
    'ssl_ca': certifi.where(),
    'ssl_verify_cert' : True
}

# Establish connection as usual
def get_db_connection(price):
  try:
    conn = mysql.connector.connect(**config)
    print("Successfully connected securely using environment variables!")
    
    cur = conn.cursor(dictionary=True)
    cur.execute(f"""
      INSERT INTO market (market_date, price)
      VALUES (curdate(), {price});            
    """)
    version = cur.fetchone()
    
  except mysql.connector.Error as err:
    print(f"Connection failed: {err}")
  finally:
    if 'conn' in locals() and conn.is_connected():
      conn.close()