manager_task = [
    {"id": "TS001",
     "name_task" : "Thiet ke giao dien App",
     "name_employee" : "Nguyen Van A",
     "expected_date" : 10,
     "finished_date" : 14,
     "difference_index" : 4,
     "status" : "Quá hạn"
     }
]

def display_task(manager_task_list):
    if not manager_task_list:
        print('Danh sách trống!')
        return
    print('===== DANH SÁCH CÔNG VIỆC ======') 
    for item in manager_task_list:
        print(f"Mã: {item.get('id'):<5} | Tên công việc: {item.get('name_task'):<22} | Tên nhân viên: {item.get('name_employee'):<15} |  Số ngày dự kiến hoàn thành: {item.get('expected_date'):<3} | Số ngày thực tế hoàn thành: {item.get('finished_date'):<3} | Chỉ số chênh lệch: {item.get('difference_index'):<2} | Trạng thái: {item.get('status'):<10}")

def classify_auto(difference_index):
    if difference_index < 0:
        return "Hoàn thành sớm"
    elif difference_index == 0:
        return "Bình thường"
    elif 1 <= difference_index <= 3:
        return "Cần tăng tốc"
    elif difference_index > 3:
        return "Quá hạn"
def add_task(manager_task_list):
    while True:
        id = input("Nhập mã công việc: ").strip().upper()
        if id == '':
            print("Mã công việc không được để trống! Vui lòng nhập lại!")
            continue
        for item in manager_task_list:
            if(id == item.get('id')):
                print('Mã công việc đã tồn tại. Vui lòng nhập lại!')
                continue
        else:
            while True:
                name_task = input("Nhập tên công việc: ").strip()
                if name_task == '':
                    print('Tên công việc không được để trống! Vui lòng nhập lại!')
                    continue
                break
            while True:
                name_employee = input("Nhập tên nhân việc: ").strip()
                if name_employee == '':
                    print('Tên nhân viên không được để trống! Vui lòng nhập lại!')
                    continue
                break
            while True:
                try:
                    expected_date = input("Nhập số ngày dự kiến hoàn thành: ").strip()
                    expected_date = int(expected_date)
                    if expected_date <= 0:
                        print("Số ngày dự kiến phải là số nguyên lớn hơn 0! Vui lòng nhập lại!")
                        continue
                    break
                except ValueError:
                    print('Dữ liệu không hợp lệ vui lòng nhập lại!')
                    continue
            while True:
                try:
                    finished_date = input("Nhập số ngày thực tế hoàn thành: ").strip()
                    finished_date = int(finished_date)
                    if finished_date < 0:
                        print("Số ngày dự kiến phải là số nguyên lớn hơn hoặc bằng 0! Vui lòng nhập lại!")
                        continue
                    break
                except ValueError:
                    print('Dữ liệu không hợp lệ vui lòng nhập lại!')
                    continue
            difference_index = finished_date - expected_date
            status = classify_auto(difference_index)
            new_task = {"id": id,
     "name_task" : name_task,
     "name_employee" : name_employee,
     "expected_date" : expected_date,
     "finished_date" : finished_date,
     "difference_index" : difference_index,
     "status" : status
     }
            manager_task_list.append(new_task)
            print('Đã thêm thành công!')
            return
            
def update_task(manager_task_list):
    if not manager_task_list:
        print('Danh sách trống!')
        return
    while True:
        id = input("Nhập mã công việc: ").strip().upper()
        if id == '':
            print("Mã công việc không được để trống! Vui lòng nhập lại!")
            continue
        for item in manager_task_list:
            if(id == item.get('id')):
                while True:
                    name_employee = input("Nhập tên nhân việc: ").strip()
                    if name_employee == '':
                        print('Tên nhân viên không được để trống! Vui lòng nhập lại!')
                        continue
                    break
                while True:
                    try:
                        expected_date = input("Nhập số ngày dự kiến hoàn thành: ").strip()
                        expected_date = int(expected_date)
                        if expected_date <= 0:
                            print("Số ngày dự kiến phải là số nguyên lớn hơn 0! Vui lòng nhập lại!")
                            continue
                        break
                    except ValueError:
                        print('Dữ liệu không hợp lệ vui lòng nhập lại!')
                        continue
                while True:
                    try:
                        finished_date = input("Nhập số ngày thực tế hoàn thành: ").strip()
                        finished_date = int(finished_date)
                        if finished_date < 0:
                            print("Số ngày dự kiến phải là số nguyên lớn hơn hoặc bằng 0! Vui lòng nhập lại!")
                            continue
                        break
                    except ValueError:
                        print('Dữ liệu không hợp lệ vui lòng nhập lại!')
                        continue
                difference_index = finished_date - expected_date
                status = classify_auto(difference_index)
                item["name_employee"] = name_employee
                item["expected_date"] = expected_date
                item["finished_date"] = finished_date
                item["difference_index"] = difference_index
                item["status"] = status
                print('Đã cập nhật xong!')
                return
        else:
            print("Không tìm thấy mã công việc!")
            return
        
def remove_task(manager_task_list):
    if not manager_task_list:
        print('Danh sách trống!')
        return
    while True:
        id = input("Nhập mã công việc: ").strip().upper()
        if id == '':
            print("Mã công việc không được để trống! Vui lòng nhập lại!")
            continue
        for item in manager_task_list:
            if(id == item.get('id')):
                choice_remove = input("Bạn có chắc muốn xóa công việc này khỏi dự án không(Y/N)?").upper
                if choice_remove == "Y":
                    manager_task_list.remove(item)
                    print('Đã xóa thành công!')
                    return
                elif choice_remove == "N":
                    print("Không xóa nữa!")
                    return
        else:
            print('Không tìm thấy mã công việc')
            return

def look_for_task(manager_task_list):
    if not manager_task_list:
        print('Danh sách trống!')
        return
    while True:
        look_for = input("Nhập mã công việc hoặc tên công việc: ").strip().upper()
        if look_for == '':
            print("Mã công việc không được để trống! Vui lòng nhập lại!")
            continue
        new_list = []
        for item in manager_task_list:
            if look_for == item.get('id') or look_for in item.get('name') :
                new_list.append(item)
        
        if not new_list:
            print("Không tìm thấy")
            return
        else:
            display_task(new_list)
            return

def statistics(manager_task_list):
    count_complete_early = 0
    count_complete = 0
    count_complete_late = 0
    count_complete_very_late = 0

    for item in manager_task_list:
        if item.get('status') == "Hoàn thành sớm":
            count_complete_early += 1
        if item.get('status') == "Bình thường":
            count_complete += 1
        if item.get('status') == "Cần tăng tốc":
            count_complete_early += 1
        if item.get('status') == "Quá hạn":
            count_complete_very_early += 1

    print(f"Trạng thái nộp sớm {count_complete_early}")
    print(f"Trạng thái nộp bình thường {count_complete}")
    print(f"Trạng thái cần tăng tốc {count_complete_early}")
    print(f"Trạng thái nộp trễ {count_complete_very_early}")
        




                
while True:
    choice = input("""
===== QUẢN LÝ DANH SÁCH CÔNG VIỆC =====
1. Hiển thị danh sách công việc
2. Thêm mới công việc
3. Cập nhật tiến độ thực tế
4. Xóa công việc khỏi dự án
5. Tìm kiếm công việc
6. Thống kê trạng thái tiến độ
7. Thoát chương trình
=======================================
Nhập lựa chọn của bạn: """)
    match choice:
        case '1':
            display_task(manager_task)
        case '2':
            add_task(manager_task)
        case '3':
            update_task(manager_task)
        case '4':
            remove_task(manager_task)
        case '5':
            look_for_task(manager_task)
        case '6':
            statistics(manager_task)
        case '7':
            print('Thoát chương trình!...')
            break
        case _:
            print("Vui lòng nhập lại!")