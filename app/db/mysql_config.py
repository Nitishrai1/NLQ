import os
import mysql.connector
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Connect using environment variables
mysql_connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB")
)

cursor = mysql_connection.cursor(dictionary=True)


def seed_transactions():
    transactions = [
        (101, "RELIANCE", 200000, "2024-06-01"),
        (102, "TATA", 150000, "2024-06-05"),
        (101, "HDFC", 300000, "2024-06-07"),
        (103, "INFY", 100000, "2024-06-09")
    ]
    
    insert_query = """
    INSERT INTO transactions (user_id, stock, amount, transaction_date)
    VALUES (%s, %s, %s, %s)
    """

    cursor.executemany(insert_query, transactions)
    mysql_connection.commit()
    print("✅ Sample transactions inserted.")


if __name__ == "__main__":
    seed_transactions()

