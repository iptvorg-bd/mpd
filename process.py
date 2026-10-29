import requests

SOURCE_URL = "https://m3u-tvb.pages.dev/dmngo.m3u"
OUTPUT_FILE = "output.m3u"

def update_playlist():
    print("ডাউনলোড শুরু হচ্ছে...")
    response = requests.get(SOURCE_URL, timeout=30)
    
    if response.status_code != 200:
        print(f"ডাউনলোড ব্যর্থ হয়েছে, স্ট্যাটাস কোড: {response.status_code}")
        return

    content = response.text
    
    # এখানে ফাইলের কন্টেন্ট সেভ করা হচ্ছে
    # যদি সোর্স ফাইলটিতে সরাসরি ক্লিয়ার-কি বা কোডি ট্যাগ না থাকে, তবে প্রয়োজনীয় পার্সিং লজিক এখানে যুক্ত করতে পারেন
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"সফলভাবে {OUTPUT_FILE} তৈরি হয়েছে।")

if __name__ == "__main__":
    update_playlist()
