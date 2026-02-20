import os
import json

def generate_playlist():
    # 폴더 설정
    base_dir = './music'  # 음악이 들어있는 폴더
    output_dir = './data' # 결과(json)가 저장될 폴더
    valid_exts = ('.mp3', '.ogg', '.wav', '.m4a')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(base_dir):
        print(f"❌ 폴더를 찾을 수 없습니다: {base_dir}")
        return

    # 하위 폴더(old, enka, jazz 등) 탐색
    categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    if not categories:
        print("💡 music 폴더 안에 하위 폴더(예: old)가 없습니다. 폴더 구조를 확인하세요.")
        return

    for cat in categories:
        cat_path = os.path.join(base_dir, cat)
        files = [f for f in os.listdir(cat_path) if f.lower().endswith(valid_exts)]
        
        playlist = []
        for index, filename in enumerate(sorted(files)):
            full_name = os.path.splitext(filename)[0]
            
            # 파일명에 ' - '가 있으면 가수/제목 분리, 없으면 전체를 제목으로
            if " - " in full_name:
                artist, title = full_name.split(" - ", 1)
            else:
                artist, title = "Artist", full_name

            song_info = {
                "id": index + 1,
                "title": title.strip(),
                "artist": artist.strip(),
                "url": f"/music/{cat}/{filename}",
                "cover": "img/default.jpg"
            }
            playlist.append(song_info)

        # json 파일 저장
        output_file = os.path.join(output_dir, f"{cat}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(playlist, f, ensure_ascii=False, indent=4)
        
        print(f"✅ {cat} 장르 완료: {len(playlist)}곡 등록됨")

if __name__ == "__main__":
    generate_playlist()