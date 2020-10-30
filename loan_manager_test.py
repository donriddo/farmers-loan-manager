import unittest
import loan_manager

class LoanManager(unittest.TestCase):
  def setUp(self):
    self.test_loan_1 = loan_manager.Loan(1000, 3)
    self.test_loan_2 = loan_manager.Loan(500, 10)
    self.test_loan_3 = loan_manager.Loan(1500, 7)

  def test_loan_is_correctly_created(self):
    self.assertEqual(self.test_loan_1.rate, 1000)
    self.assertEqual(self.test_loan_1.start_day, 3)
  
  def test_amount_payable_for_day_1_is_correct(self):
    self.assertEqual(
      loan_manager.get_amount_payable(
        1, # Day 1
        [self.test_loan_1, self.test_loan_2, self.test_loan_3]
      ),
      0
    )

  def test_amount_payable_for_day_2_is_correct(self):
    self.assertEqual(
      loan_manager.get_amount_payable(
        2, # Day 2
        [self.test_loan_1, self.test_loan_2, self.test_loan_3]
      ),
      0
    )

  def test_amount_payable_for_day_3_is_correct(self):
    self.assertEqual(
      loan_manager.get_amount_payable(
        3, # Day 3
        [self.test_loan_1, self.test_loan_2, self.test_loan_3]
      ),
      1000
    )

  def test_amount_payable_for_day_4_is_correct(self):
    self.assertEqual(
      loan_manager.get_amount_payable(
        4, # Day 4
        [self.test_loan_1, self.test_loan_2, self.test_loan_3]
      ),
      1000
    )

  def test_amount_payable_for_day_7_is_correct(self):
    self.assertEqual(
      loan_manager.get_amount_payable(
        7, # Day 7
        [self.test_loan_1, self.test_loan_2, self.test_loan_3]
      ),
      2500
    )

  def test_amount_payable_for_day_9_is_correct(self):
    self.assertEqual(
      loan_manager.get_amount_payable(
        9, # Day 9
        [self.test_loan_1, self.test_loan_2, self.test_loan_3]
      ),
      2500
    )

  def test_amount_payable_for_day_10_is_correct(self):
    self.assertEqual(
      loan_manager.get_amount_payable(
        10, # Day 10
        [self.test_loan_1, self.test_loan_2, self.test_loan_3]
      ),
      3000
    )

  def test_get_loan_days_of_power(self):
    days_of_power, balance = loan_manager.get_loan_days_of_power(
      21000, # Amount paid
      [self.test_loan_1, self.test_loan_2, self.test_loan_3]
    )

    self.assertEqual(days_of_power, 10)
    self.assertEqual(balance, 500)

  def test_get_days_of_power_1(self):
    days_of_power, balance = loan_manager.get_days_of_power(
      R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000
    )

    self.assertEqual(days_of_power, 10)
    self.assertEqual(balance, 500)

  def test_get_days_of_power_2(self):
    days_of_power, balance = loan_manager.get_days_of_power(
      R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000
    )

    self.assertEqual(days_of_power, 141)
    self.assertEqual(balance, 4500)

  def test_get_days_of_power_3(self):
    days_of_power, balance = loan_manager.get_days_of_power(
      R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700500
    )

    self.assertEqual(days_of_power, 142)
    self.assertEqual(balance, 0)

  def test_get_days_of_power_4(self):
    days_of_power, balance = loan_manager.get_days_of_power(
      R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000
    )

    self.assertEqual(days_of_power, 17)
    self.assertEqual(balance, 1000)

  def test_get_days_of_power_5(self):
    days_of_power, balance = loan_manager.get_days_of_power(
      R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000
    )

    self.assertEqual(days_of_power, 5)
    self.assertEqual(balance, 1000)

  def test_get_days_of_power_6(self):
    days_of_power, balance = loan_manager.get_days_of_power(
      R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000
    )

    self.assertEqual(days_of_power, 1)
    self.assertEqual(balance, 1000)


if __name__ == '__main__':
  unittest.main()
