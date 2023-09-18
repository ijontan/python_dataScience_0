import time as t
import datetime as dt

msSinceEpoch = t.time()
date = dt.datetime.fromtimestamp(msSinceEpoch)
print(f'Seconds since January 1, 1970: {msSinceEpoch:,.4f} or {msSinceEpoch:.2e} in scientific notation')
print(date.strftime("%b %d %Y"))