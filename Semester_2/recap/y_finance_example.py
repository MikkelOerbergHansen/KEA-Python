
import yfinance as yf



msft = yf.Ticker("SIM.CO")

print(msft.info)

hist=msft.history(period="max")

print(msft.actions)

print(msft.dividends)

print(msft.splits)

print(msft.shares)

#print(msft.income_stmt)

#print(msft.quarterly_income_stmt)

print(msft.balance_sheet)

#print(msft.quarterly_balance_stmt)


print(msft.cashflow)

print(msft.quarterly_cashflow)

print(msft.major_holders)




































