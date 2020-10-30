class Loan(object):
  def __init__(self, loan_rate, loan_start_day):
    self.rate = loan_rate
    self.start_day = loan_start_day


def get_amount_payable(current_day, loans):
  """
  loop through loans and check if loan has started.
  if yes, add it to the total amount payable for current day
  """
  amount_payable = 0
  for loan in loans:
    loan_rate = loan.rate
    loan_start_day = loan.start_day
    if current_day >= loan_start_day:
      amount_payable += loan_rate
  
  return amount_payable

def get_loan_days_of_power(amount_paid, loans):
  """
  general function to get days of power for any number of loans obtained by farmer
  for each successive day:
    give farmer a day of power as long he has enough balance to cover amount payable
    for the day
  """
  balance = amount_paid
  amount_payable = 0
  days_of_power = 0
  current_day = 0
  rates = [loan.rate for loan in loans]

  while balance >= amount_payable:
    current_day += 1
    amount_payable = get_amount_payable(current_day, loans)
    if (amount_payable >= min(rates) and amount_payable <= balance):
      days_of_power += 1
      balance -= amount_payable

  return (days_of_power, balance)

def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
  loan1 = Loan(R1, D1)
  loan2 = Loan(R2, D2)
  loan3 = Loan(R3, D3)
  
  return get_loan_days_of_power(K, [loan1, loan2, loan3])



if __name__ == '__main__':
    print("Days of power = %d | balance = %d" % get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000))

    print("Days of power = %d | balance = %d" % get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000))
    print("Days of power = %d | balance = %d" % get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000))
    print("Days of power = %d | balance = %d" % get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000))
    print("Days of power = %d | balance = %d" % get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000))
