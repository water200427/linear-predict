import matplotlib.pyplot as plt

day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_month_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
average_of_month_temperature = [2, 3, 7, 12, 17, 20, 22, 22, 18, 13, 7, 3]

initial_temperature = 5

def linear_prediction():
    temperature_of_month_and_day = []
    current_temp = initial_temperature  # 第一個月的起始溫度
    
    for i in range(len(day_of_month)):
        temperature_of_day = []
        current_avg = average_of_month_temperature[i]
        mid_point = day_of_month[i] // 2
        
        # 計算本月需要達到的斜率，使得月中時達到平均溫度
        slope = (current_avg - current_temp) / mid_point
        
        # 計算整個月的溫度變化
        for j in range(day_of_month[i]):
            if j < mid_point:
                # 月初到月中
                temp = current_temp + slope * j
            else:
                # 月中到月底，保持相同斜率
                temp = current_avg + slope * (j - mid_point)
            temperature_of_day.append(temp)
        
        temperature_of_month_and_day.append(temperature_of_day)
        # 用這個月最後一天的溫度作為下個月的起始溫度
        current_temp = temperature_of_day[-1]
    
    return temperature_of_month_and_day

if __name__ == "__main__":
    temperature_of_month_and_day = linear_prediction()
    flat_temperature_of_month_and_day = [temperature for month in temperature_of_month_and_day for temperature in month]
    adjusted_average_temperature = []
    for i in range(len(day_of_month)):
        adjusted_average_temperature.extend([average_of_month_temperature[i]] * day_of_month[i])
    
    # 建立月份刻度
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_positions = []
    current_pos = 0
    
    # 計算每個月份的位置
    for days in day_of_month:
        month_positions.append(current_pos)  # 在每月初標示月份
        current_pos += days

    plt.figure(figsize=(12, 6))
    plt.plot(adjusted_average_temperature, label='Average Monthly Temperature')
    plt.plot(flat_temperature_of_month_and_day, label='Predicted Daily Temperature')
    
    # 設置月份刻度
    plt.xticks(month_positions, month_names)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xlabel("Month")
    plt.ylabel("Temperature (°C)")
    plt.title("Daily Temperature Prediction")
    plt.savefig('prediction_result.png', dpi=300, bbox_inches='tight')
    plt.show()
