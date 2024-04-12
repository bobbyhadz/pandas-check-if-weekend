# Pandas: Check if a Date is during the Weekend or Weekday

import pandas as pd

# Saturday, August 5th, 2023
a_date = pd.Timestamp('2023-08-05')

if a_date.weekday() > 4:
    # 👇️ this runs
    print('The date is during the weekend')
else:
    print('The date is a weekday')
