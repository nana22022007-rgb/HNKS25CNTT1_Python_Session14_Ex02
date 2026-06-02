"""
(1) Phân tích lỗi
total_points được khai báo ngoài hàm nên là biến toàn cục (Global Variable).
Python báo lỗi UnboundLocalError vì trong hàm có phép gán:
total_points = total_points + points_earned
nên Python tự hiểu total_points là biến cục bộ. Tuy nhiên biến này chưa được gán giá trị trước khi sử dụng nên phát sinh lỗi.
Nếu chỉ đọc giá trị, ví dụ:
print(total_points)
thì chương trình không bị lỗi vì hàm được phép đọc biến toàn cục.
Cách sửa 1: dùng từ khóa global:
global total_points
để Python biết rằng đang sử dụng biến toàn cục.
Cách sửa 2 (khuyến khích): truyền tổng điểm cũ và điểm mới vào hàm, sau đó dùng:
return
để trả về tổng điểm sau khi cộng.
"""
# Bien toàn cục lưu tổng điểm hiện tại của khách hàng
total_points = 100

# Hàm cộng điểm thưởng
def add_reward_points(points_earned) :
# Co gắng lay tong điểm cu cong them điểm mới
    global total_points
    total_points = total_points + points_earned
    print("Đã cộng thêm", points_earned, "điem.")

# Khách mua hàng được thưởng 50 điểm
add_reward_points(50)

# In ra kết quả
print("Tổng điểm hiện tại của khách hàng:", total_points)
