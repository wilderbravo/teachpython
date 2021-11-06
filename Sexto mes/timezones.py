# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

from datetime import datetime
import pytz 

quito_timezone = pytz.timezone('America/Guayaquil')
quito_date = datetime.now(quito_timezone)

print("Quito: ", quito_date.strftime("%d/%m/%Y, %H:%M:S"))
