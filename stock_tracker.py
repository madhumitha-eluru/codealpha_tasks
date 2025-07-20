import yfinance as yf

# Ask user to enter a stock symbol (like AAPL, TSLA, INFY)
symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ")

# Get data using yfinance
stock = yf.Ticker(symbol)

# Fetch latest market info
info = stock.info

# Print useful details
print("\n--- Stock Information ---")
print("Company Name:", info.get("longName", "N/A"))
print("Current Price:", info.get("currentPrice", "N/A"))
print("Market Cap:", info.get("marketCap", "N/A"))
print("52 Week High:", info.get("fiftyTwoWeekHigh", "N/A"))
print("52 Week Low:", info.get("fiftyTwoWeekLow", "N/A"))
