#Ex1
from datetime import datetime, timedelta
five_days_ago = datetime.now() - timedelta(days=5)
print("Бес күн бұрын:", five_days_ago.strftime("%Y-%m-%d"))


#Ex2
from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))


#Ex3
from datetime import datetime
current_time = datetime.now().replace(microsecond=0)
print("Микросекундтарсыз уақыт:", current_time)


#Ex4
from datetime import datetime

date1 = datetime(2023, 1, 1, 12, 0, 0)
date2 = datetime(2023, 1, 2, 12, 0, 0)
difference = (date2 - date1).total_seconds()
print("Айырмашылық (секунд):", difference)




