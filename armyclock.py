# 짭 군돌이(armyclock)
# 일단 육군 기준으로 만들고, 다 만들면 육군/해군/공군 선택 구현하기

import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

input = sys.stdin.readline


# 현재 시각
current_time = datetime.now()

# 현재일
today_date = format(current_time, "%Y-%m-%d")

# 입대일
# 백엔드랑 연결하면 input tag에서 입력받아서 값을 이용할 수 있도록 구현
s_year, s_month, s_day = map(int, input().split())
start_date = datetime(s_year, s_month, s_day)
print("\n입대일: {}".format(format(start_date, "%Y-%m-%d")))

# 계급 별 진급시기
grade_1 = start_date
grade_2 = (grade_1 + relativedelta(months = 3)).replace(day = 1) # 매월 1일에 진급하니까!
grade_3 = grade_2 + relativedelta(months = 6)
grade_4 = grade_3 + relativedelta(months = 6)

print("\n일병 진급: {}".format(format(grade_2, "%Y-%m-%d")))
print("상병 진급: {}".format(format(grade_3, "%Y-%m-%d")))
print("병장 진급: {}\n".format(format(grade_4, "%Y-%m-%d")))

# 전역일
end_date = start_date + relativedelta(months = 18) - relativedelta(days = 1)
print("전역일: {}".format(format(end_date, "%Y-%m-%d")))
remain_serve_time = end_date - current_time
print("남은 복무일수는 {}일 {}시간 입니다.\n".format(remain_serve_time.days, remain_serve_time.seconds // 3600))

# 복무 퍼센트(%) 계산
serve_time_til_now = current_time - start_date
serve_time_total = end_date - start_date
print("현재 복무일: {}일".format(serve_time_til_now.days))
print("전체 복무일: {}일".format(serve_time_total.days))
percent = (serve_time_til_now / serve_time_total) * 100
print("\n{:.6f} %".format(percent))
