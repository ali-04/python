import datetime
q = ('-'.join(input().split('/')))

x = datetime.date.fromisoformat(q)
y = datetime.date.today()

e = y-x

print  (int(e.days)//365)












