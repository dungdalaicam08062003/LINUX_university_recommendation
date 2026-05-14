import requests
import json

API_KEY = "AIzaSyBDPC_TRCa3Su_U9E5VflzLhQnQDvkP_kE"  # điền API Key của bạn
SEARCH_ENGINE_ID = "93a85ee06b74c49fb"  # điền Search Engine ID (cx)

def search_google(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    
    # Kiểm tra status code
    if response.status_code != 200:
        print("HTTP Error:", response.status_code)
        print(response.text)
        return
    
    results = response.json()
    
    # Nếu có lỗi từ Google API
    if "error" in results:
        print("API Error:", results["error"])
        return
    
    # In toàn bộ JSON để debug (tuỳ chọn)
    print(json.dumps(results, indent=2, ensure_ascii=False))
    
    # In kết quả tìm kiếm
    items = results.get("items", [])
    if not items:
        print("Không có kết quả nào.")
    else:
        for item in items:
            print(item["title"])
            print(item["link"])
            print("-" * 50)

if __name__ == "__main__":
    search_google("tin tức công nghệ mới nhất")
