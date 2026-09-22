# import datetime

# now = datetime.datetime.now()
# print(now)

# print(("{:05d}".format(123)))



import datetime
now = datetime.datetime.now()

print(now.month)

print("{:02d}월".format(now.month))
print("{:02d}분".format(now.minute))
print("{:02d}초".format(now.second))


# strftime
f_date = now.strftime("%Y-%m-%d")
print(f_date)


f_date = now.strftime("%m월 %d일")
print(f_date)





