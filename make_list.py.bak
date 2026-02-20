import os
import json

def generate_playlist():
    base_dir = './music'
    # 결과물을 js 폴더나 플레이어가 읽는 위치에 'songs.js' 같은 이름으로 저장합니다.
    output_file = './playlist_data.js' 
    valid_exts = ('.mp3', '.ogg', '.wav', '.m4a')

    if not os.path.exists(base_dir):
        print(f"❌ 폴더 없음: {base_dir}")
        return

    categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    all_data = {}

    for cat in categories:
        cat_path = os.path.join(base_dir, cat)
        files = [f for f in os.listdir(cat_path) if f.lower().endswith(valid_exts)]
        
        songs = []
        for filename in sorted(files):
            full_name = os.path.splitext(filename)[0]
            # 플레이어 형식에 맞게 title과 url 생성
            songs.append({
                "title": full_name,
                "url": f"music/{cat}/{filename}"
            })
        all_data[cat] = songs

    # 중요: 자바스크립트 변수 형태로 저장합니다.
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"const playlists = {json.dumps(all_data, ensure_ascii=False, indent=4)};")
    
    print(f"✅ 완료! '{output_file}' 파일이 생성되었습니다.")

if __name__ == "__main__":
    generate_playlist()