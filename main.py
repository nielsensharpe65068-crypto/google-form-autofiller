import argparse
import time
import sys
import datetime
import json
import random
import string # Đảm bảo có dòng này ở đầu tệp

import requests

import form
def remove_accents(text):
    """Hàm để loại bỏ dấu từ chuỗi tiếng Việt."""
    s = text.lower()
    s = s.replace('á', 'a').replace('à', 'a').replace('ả', 'a').replace('ã', 'a').replace('ạ', 'a')
    s = s.replace('ă', 'a').replace('ắ', 'a').replace('ằ', 'a').replace('ẳ', 'a').replace('ẵ', 'a').replace('ặ', 'a')
    s = s.replace('â', 'a').replace('ấ', 'a').replace('ầ', 'a').replace('ẩ', 'a').replace('ẫ', 'a').replace('ậ', 'a')
    s = s.replace('đ', 'd')
    s = s.replace('é', 'e').replace('è', 'e').replace('ẻ', 'e').replace('ẽ', 'e').replace('ẹ', 'e')
    s = s.replace('ê', 'e').replace('ế', 'e').replace('ề', 'e').replace('ể', 'e').replace('ễ', 'e').replace('ệ', 'e')
    s = s.replace('í', 'i').replace('ì', 'i').replace('ỉ', 'i').replace('ĩ', 'i').replace('ị', 'i')
    s = s.replace('ó', 'o').replace('ò', 'o').replace('ỏ', 'o').replace('õ', 'o').replace('ọ', 'o')
    s = s.replace('ô', 'o').replace('ố', 'o').replace('ồ', 'o').replace('ổ', 'o').replace('ỗ', 'o').replace('ộ', 'o')
    s = s.replace('ơ', 'o').replace('ớ', 'o').replace('ờ', 'o').replace('ở', 'o').replace('ỡ', 'o').replace('ợ', 'o')
    s = s.replace('ú', 'u').replace('ù', 'u').replace('ủ', 'u').replace('ũ', 'u').replace('ụ', 'u')
    s = s.replace('ư', 'u').replace('ứ', 'u').replace('ừ', 'u').replace('ử', 'u').replace('ữ', 'u').replace('ự', 'u')
    s = s.replace('ý', 'y').replace('ỳ', 'y').replace('ỷ', 'y').replace('ỹ', 'y').replace('ỵ', 'y')
    return s

def fill_random_value(type_id, entry_id, options, required = False, entry_name = ''):
    '''
    Hàm tùy chỉnh để điền giá trị cho từng câu hỏi dựa trên ID.
    Phiên bản này đảm bảo so sánh chính xác ID bằng cách chuyển nó thành chuỗi.
    '''
    # Chuyển đổi entry_id sang kiểu chuỗi để so sánh nhất quán
    entry_id_str = str(entry_id)

    # --- PHẦN TÙY CHỈNH THEO YÊU CẦU CỦA BẠN ---

    # Tên: Tạo ngẫu nhiên theo nhiều kiểu (tên đầy đủ, tên chính, chữ cái ngẫu nhiên)
    if entry_id_str == '687151206':
        # Chọn ngẫu nhiên một trong ba kiểu tạo tên
        kieu_tao_ten = random.choice(['day_du', 'chi_ten', 'ky_tu'])

        if kieu_tao_ten == 'ky_tu':
            # Kiểu 1: Chuỗi ký tự ngẫu nhiên
            return ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))

        # Danh sách tên để sử dụng cho hai kiểu còn lại
        ho = ['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Huỳnh', 'Hoàng', 'Phan', 'Vũ', 'Võ', 'Đặng', 'Bùi', 'Đỗ', 'Hồ', 'Ngô', 'Dương', 'Lý', 'Trịnh', 'Đinh', 'Đoàn', 'Trương', 'Mai', 'Cao', 'Châu', 'Hà', 'Lương', 'Lâm', 'Tạ', 'Tôn', 'Thạch', 'Chu', 'Cù', 'Quách', 'Diệp', 'Vương']
        
        ten_dem_unisex = ['Gia', 'An', 'Minh', 'Nhật', 'Ngọc', 'Lam', 'Thanh', 'Vĩnh', 'Xuân', 'Phương', 'Khánh', 'Hạ', 'Anh']
        ten_dem_nam = ['Văn', 'Hữu', 'Đức', 'Công', 'Quang', 'Đình', 'Duy', 'Tuấn', 'Hoàng', 'Quốc', 'Trọng', 'Mạnh', 'Thành', 'Tấn', 'Xuân', 'Nhật', 'Khắc', 'Bá', 'Thái', 'Khải', 'Đăng'] + ten_dem_unisex
        ten_dem_nu = ['Thị', 'Ngọc', 'Thùy', 'Quỳnh', 'Phương', 'Bảo', 'Diệu', 'Mỹ', 'Thảo', 'Tường', 'Yến', 'Mai', 'Kim', 'Cẩm', 'Như', 'Lan', 'An', 'Tuệ', 'Diệp', 'Ái', 'Châu'] + ten_dem_unisex

        ten_chinh_nam = ['An', 'Anh', 'Bảo', 'Bình', 'Cường', 'Dũng', 'Duy', 'Dương', 'Đức', 'Giang', 'Hải', 'Hiếu', 'Hoàng', 'Huy', 'Hùng', 'Khang', 'Khải', 'Khoa', 'Kiên', 'Long', 'Mạnh', 'Minh', 'Nam', 'Nghĩa', 'Nguyên', 'Nhân', 'Phong', 'Phúc', 'Quân', 'Quang', 'Quốc', 'Sang', 'Sơn', 'Tài', 'Tâm', 'Thái', 'Thành', 'Thịnh', 'Toàn', 'Trọng', 'Trung', 'Tú', 'Tuấn', 'Việt', 'Vinh']
        ten_chinh_nu = ['An', 'Anh', 'Ánh', 'Bích', 'Châu', 'Chi', 'Dung', 'Duyên', 'Giang', 'Hà', 'Hân', 'Hằng', 'Hạnh', 'Hoa', 'Hồng', 'Huệ', 'Huyền', 'Hương', 'Khánh', 'Khuê', 'Lan', 'Linh', 'Ly', 'Mai', 'My', 'Nga', 'Ngân', 'Ngọc', 'Nhi', 'Nhung', 'Oanh', 'Phương', 'Quyên', 'Quỳnh', 'Tâm', 'Thảo', 'Thơ', 'Thu', 'Thủy', 'Thương', 'Trà', 'Trang', 'Trinh', 'Trúc', 'Tú', 'Uyên', 'Vân', 'Vy', 'Yến']
        
        danh_sach_ten_chinh = ten_chinh_nam + ten_chinh_nu

        if kieu_tao_ten == 'chi_ten':
            # Kiểu 2: Chỉ một tên chính
            return random.choice(danh_sach_ten_chinh)
        
        else: # kieu_tao_ten == 'day_du'
            # Kiểu 3: Tên đầy đủ (Họ + Tên đệm + Tên chính)
            if random.choice(['nam', 'nu']) == 'nam':
                ten_dem = random.choice(ten_dem_nam)
                ten_chinh = random.choice(ten_chinh_nam)
            else:
                ten_dem = random.choice(ten_dem_nu)
                ten_chinh = random.choice(ten_chinh_nu)
            return f"{random.choice(ho)} {ten_dem} {ten_chinh}"

    # Tuổi: Random '18-20', '21-22', 'Trên 22'
    if entry_id_str == '1950221337':
        return random.choice(['18 - 20 tuổi', '21 - 22 tuổi', 'Trên 22 tuổi'])

    # Năm học: Random
    if entry_id_str == '247762463':
        return random.choice(['Năm nhất', 'Năm hai', 'Năm ba', 'Năm tư', 'Khác'])

    # Giới tính: Random Nam/Nữ
    if entry_id_str == '236693252':
        return random.choice(['Nam', 'Nữ'])

    # Email: Tạo ngẫu nhiên theo nhiều kiểu tiếng Việt
    if entry_id_str == '866847573':
        # 50% cơ hội tạo email, 50% bỏ trống
        if not random.choice([True, False]):
            return ""

        # Danh sách các từ/tên để tạo email
        ten_nguoi = ['anh', 'trang', 'minh', 'phuong', 'hieu', 'thao', 'quynh', 'hoang', 'bach', 'long']
        tu_tieng_viet = ['muaxuan', 'muaha', 'hoacuc', 'ngoinha', 'dongsong', 'bau troi', 'maytrang', 'nangvang']
        
        # Chọn ngẫu nhiên 1 trong 3 kiểu tạo email
        kieu_tao = random.choice(['ten_namsinh', 'viet_tat', 'tu_viet'])

        local_part = ""
        if kieu_tao == 'ten_namsinh':
            # Kiểu 1: Tên người viết liền + năm sinh (1985-2005)
            ten = random.choice(ten_nguoi)
            nam_sinh = str(random.randint(1985, 2005))
            local_part = ten + nam_sinh
        
        elif kieu_tao == 'viet_tat':
            # Kiểu 2: Tên viết tắt + số ngẫu nhiên
            ten = random.choice(ten_nguoi)
            viet_tat = ten[0] + random.choice('abcdefghijklmnopqrstuvwxyz')
            so_ngau_nhien = str(random.randint(100, 9999))
            local_part = viet_tat + so_ngau_nhien

        else: # kieu_tao == 'tu_viet'
            # Kiểu 3: Từ tiếng Việt viết liền + số ngẫu nhiên
            tu = random.choice(tu_tieng_viet)
            so_ngau_nhien = str(random.randint(10, 999))
            local_part = tu + so_ngau_nhien
            
        return f"{remove_accents(local_part)}@gmail.com"

    # Nhóm 1: Mua sắm, Thu nhập, Chi tiêu (Random)
    if entry_id_str in ['965818835', '1747022867', '953070746']:
        return random.choice(options) if options else ''

    # Nhóm 2, 4, 5: Các câu hỏi thang đo 1-5 (Random)
    if entry_id_str in [
        '52566242', '1051087591', '1562888166', '189305489', '565850207', '365829033',
        '1725216252', '96670760', '605261018', '675996958', '606736157', '1763731881',
        '598873275', '32377337', '1242600396', '2044726087', '679572474', '731634874',
        '267862701', '1691917716', '2145599714', '1929997236', '2115170286',
        '1734298429', '2027053865', '950315784'
    ]:
        return random.choice(options) if options else ''

    # Nhóm 3: Các câu hỏi kiểm tra sự tập trung (Chọn '4')
    if entry_id_str in ['1405784530', '483990084', '1845975606']:
        return '4'

    # Nhóm 6: Các câu hỏi kiến thức tài chính (Chọn đáp án cụ thể)
    if entry_id_str == '1832474600':
        return '2.040.000 VND'
    if entry_id_str == '813865330':
        return 'Ít hàng hóa hơn so với hôm nay'
    if entry_id_str == '625104329':
        return 'Sai'
    if entry_id_str == '242028223':
        return '1.210.000 VND'

    # Nhóm 7: Tần suất sử dụng SPayLater (Random)
    if entry_id_str == '246642087':
        return random.choice(['1-2 lần', 'Trên 5 lần', '3-5 lần'])

    # Xử lý trường hợp đặc biệt 'emailAddress' nếu form yêu cầu thu thập email
    if entry_id_str == 'emailAddress':
        return 'your_email@gmail.com'

    # Nếu không có quy tắc nào khớp, trả về chuỗi rỗng để tránh lỗi
    return ''


def generate_request_body(url: str, only_required = False):
    ''' Generate random request body data '''
    data = form.get_form_submit_request(
        url,
        only_required = only_required,
        fill_algorithm = fill_random_value,
        output = "return",
        with_comment = False
    )
    if data is None:
        return None
    data = json.loads(data)
    # you can also override some values here
    return data

def submit(url: str, data: any):
    ''' Submit form to url with data '''
    response_url = form.get_form_response_url(url)
    print("Submitting to", response_url)
    print("Data:", data, flush = True)

    res = requests.post(response_url, data=data, timeout=5)
    if res.status_code != 200:
        print(f"Error! Can't submit form. Status code: {res.status_code}")
        print("Response content:", res.text)


def main(url, count, delay, random_delay, only_required):
    """Hàm chính để điều khiển việc gửi form lặp lại."""

    def countdown(seconds):
        """Hàm hiển thị đồng hồ đếm ngược."""
        for i in range(seconds, 0, -1):
            # Ghi đè lên cùng một dòng trên terminal
            sys.stdout.write(f"\rWaiting for {i} seconds before next submission... ")
            sys.stdout.flush()
            time.sleep(1)
        # In một dòng mới sau khi đếm ngược xong
        print() 

    for i in range(count):
        print(f"--- Starting submission {i + 1} of {count} ---")
        try:
            payload = generate_request_body(url, only_required=only_required)
            if payload:
                submit(url, payload)
            else:
                print("Failed to generate payload. Cannot submit.")

            # Logic chờ giữa các lần gửi
            if i < count - 1:
                sleep_time = 0
                if random_delay:
                    try:
                        min_delay, max_delay = map(int, random_delay.split('-'))
                        sleep_time = random.randint(min_delay, max_delay)
                    except ValueError:
                        print("Invalid random_delay format. Use 'min-max'.")
                        break
                elif delay > 0:
                    sleep_time = delay
                
                if sleep_time > 0:
                    # Gọi hàm đếm ngược thay vì time.sleep
                    countdown(sleep_time)

        except Exception as e:
            print(f"An unexpected error occurred during submission {i + 1}: {e}")
            print("Waiting for 60 seconds before retrying...")
            time.sleep(60)
    
    print("--- All submissions completed! ---")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tự động gửi Google Form nhiều lần.')
    parser.add_argument('url', help='URL của Google Form')
    parser.add_argument('-n', '--count', type=int, default=1, help='Số lần gửi form (mặc định: 1)')
    parser.add_argument('-d', '--delay', type=int, default=0, help='Thời gian chờ cố định (giây) giữa các lần gửi.')
    parser.add_argument('--random-delay', type=str, help="Khoảng thời gian chờ ngẫu nhiên (giây), ví dụ: '1500-1800'")
    parser.add_argument('-r', '--required', action='store_true', help='Chỉ điền các trường bắt buộc')
    args = parser.parse_args()

    # Truyền các tham số mới vào hàm main
    main(args.url, args.count, args.delay, args.random_delay, args.required)