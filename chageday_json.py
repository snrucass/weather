import json
from datetime import datetime, timedelta

def shift_json_datetime(data, days_shift=-5):
    """
    ฟังก์ชันสำหรับวนลูปอัปเดตค่า datetime ในโครงสร้าง JSON
    โดยเลื่อนวันที่เพิ่มขึ้นตามจำนวนวันที่กำหนด (ค่าเริ่มต้นคือ 5 วัน)
    """
    for district in data.get("districts", []):
        for village in district.get("villages", []):
            for item in village.get("weather_data", []):
                if "datetime" in item:
                    dt = datetime.strptime(item["datetime"], "%Y-%m-%d %H:%M:%S")
                    new_dt = dt + timedelta(days=days_shift)
                    item["datetime"] = new_dt.strftime("%Y-%m-%d %H:%M:%S")
    return data

def process_weather_file(input_filename, output_filename, days_shift=-5):
    """
    อ่านไฟล์ JSON ต้นทาง แปลงวันที่ และบันทึกลงไฟล์ใหม่
    """
    with open(input_filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated_data = shift_json_datetime(data, days_shift)

    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(updated_data, f, ensure_ascii=False, indent=4)

    print(f"บันทึกไฟล์เรียบร้อยแล้ว: {output_filename}")

if __name__ == "__main__":
    # ระบุชื่อไฟล์ต้นทางและไฟล์ปลายทางที่ต้องการ
    input_file = "weather_data_locations.json"
    output_file = "weather_data_locations.json"
    
    process_weather_file(input_file, output_file, days_shift=-5)
