import datetime
import sys

dt = datetime.datetime.today().strftime('%Y年%m月%d日')

user = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else "User"

print(f'Hello {user}! 現在是{dt}')
