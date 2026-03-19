import subprocess
import os
from datetime import datetime

def github_push():
    # 1. ระบุตำแหน่งโฟลเดอร์ Y:\web_app ที่มีไฟล์ .git ของคุณ
    repo_path = r'Y:\web_app'
    
    # ย้ายตำแหน่งการทำงานของ Python ไปที่โฟลเดอร์นั้น
    os.chdir(repo_path)
    
    try:
        # 2. Add เฉพาะไฟล์ JSON (หรือจะใช้ "." เพื่อเอา index.html ไปด้วยก็ได้)
        subprocess.run(["git", "add", "weather_data_locations.json"], check=True)
        
        # 3. Commit พร้อมใส่เวลาที่อัปเดต
        commit_message = f"Auto-update weather data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # 4. Push ขึ้น GitHub
        # เนื่องจากคุณฝัง Token ไว้ใน Remote แล้ว มันจะไม่ถามรหัสผ่านอีก
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print("✅ [GitHub] Data pushed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"❌ [GitHub] Error occurred: {e}")
    except Exception as ex:
        print(f"❌ [GitHub] General Error: {ex}")

if __name__ == "__main__":
    # ตรงนี้คือส่วนที่คุณจะใส่โค้ดที่ใช้ Gen ไฟล์ JSON ของคุณ
    # เช่น: generate_weather_json()
    
    # เมื่อ Gen ไฟล์เสร็จแล้ว ก็เรียกฟังก์ชันส่งขึ้น GitHub
    github_push()