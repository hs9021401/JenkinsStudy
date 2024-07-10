import datetime
import sys
from QuickSort import QuickSort

dt = datetime.datetime.today().strftime('%Y年%m月%d日')

user = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else "User"

print(f'Hello {user}! 現在是{dt}')


arr = [163, 23, 2, 55, 35, 243, 30, 11]
print(f'Before sort: {arr}')

print(f'Quick Sort start...')
QuickSort(arr, 0, len(arr) - 1)

print(f'After sort: {arr}')
