parking_car = [
    {
        "id": 1,
        "type": "Xe máy",
        "owner": "Phạm Thành Đạt"
    }
]
max_id = len(parking_car)
while True:
    choose = input("""===========================================================
    QUẢN LÝ BÃI XE - SMART PARKING
===========================================================
1. Thêm xe mới vào bãi 
2. Hiển thị danh sách xe trong bãi 
3. Tìm kiếm xe theo mã (id)
4. Xóa xe khỏi bãi (khi xe ra)
5. Thoát chương trình
===========================================================
Lựa chọn chương trình của bạn (1-5): """)
    if choose == "1":
        type_new_car = input("Nhập loại xe mới: ").strip()
        while type_new_car == "":
            print("Loại xe không được để trống, vui lòng nhập lại")
            type_new_car = input("Nhập loại xe mới: ").strip()
        owner_new_car = input("Nhập tên chủ xe mới: ").strip()
        while owner_new_car == "":
            print("Chủ xe không được để trống, vui lòng nhập lại")
            owner_new_car = input("Nhập tên chủ xe mới: ").strip()
        new_car = {
            "id": max_id+1,
            "type": type_new_car,
            "owner": owner_new_car
        }
        parking_car.append(new_car)
        max_id += 1
        print("Thêm xe mới thành công")
        print()
    elif choose == "2":
        if len(parking_car) == 0:
            print("Bãi xe hiện đang trống")
        else: 
            print(f'{"ID": <5} | {"Loại xe": <10} | {"Chủ xe": <20}')
            for car in parking_car:
                print(f'{car.get("id"): <5} | {car.get("type"): <10} | {car.get("owner")}')
        print()
    elif choose == "3":
        search_car = input("Nhập id của xe cần tìm: ")
        valid = True
        for car in parking_car:
            if int(search_car) == car.get("id"):
                print(f"{car}")
                valid = False
                break 
        if valid == True:
            print(f"Không tìm thấy xe có ID {search_car}")
        print()
    elif choose == "4":
        delete_car = input("Nhập id của xe cần xóa: ")
        valid = True
        for index,car in enumerate(parking_car):
            if int(delete_car) == car.get("id"):
                parking_car.pop(index)
                print(f"Đã xóa xe ID {delete_car} thành công")
                valid = False
                break 
        if valid == True:
            print("Không tìm thấy xe để xóa")
        print()
    elif choose == "5":
        print("Chương trình kết thúc")
        break 
    else:
        print("Lựa chọn không hợp lệ")
        print()