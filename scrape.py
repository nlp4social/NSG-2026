import urllib.request
import re
import json
import os

urls = [
    "https://scholar.google.com/citations?user=NYYAnbIAAAAJ&hl=en",
    "https://scholar.google.com/citations?user=TrgGMO0AAAAJ&hl=en",
    "https://scholar.google.com/citations?user=gLZgtuMAAAAJ&hl=en",
    "https://scholar.google.com/citations?user=fvQicksAAAAJ&hl=en",
    "https://scholar.google.com/citations?user=t3A39e8AAAAJ&hl=en"
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

advisors = []
organizers = []

if not os.path.exists('assets/organizer_images'):
    os.makedirs('assets/organizer_images')

for url in urls:
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        continue
    
    # Extract name from title
    m = re.search(r'<title>‪(.*?)‬ - ‪Google Scholar‬</title>', html)
    name = m.group(1).strip() if m else "Unknown"
    
    # Clean up name: remove anything that's not alphanumeric/space if google put weird chars
    name = re.sub(r'[^\w\s\.-]', '', name).strip()
    
    # Extract affiliation
    aff_m = re.search(r'<div class="gsc_prf_il">(.*?)</div>', html)
    affiliation = "Unknown Affiliation"
    if aff_m:
        aff_html = aff_m.group(1)
        # remove links
        aff_html = re.sub(r'<[^>]+>', '', aff_html).strip()
        affiliation = aff_html
    
    # Extract homepage or URL
    url_m = re.search(r'<a href="([^"]+)" rel="nofollow" class="gsc_prf_ila">Homepage</a>', html)
    homepage = url_m.group(1) if url_m else url
    
    # Extract image
    img_m = re.search(r'<img[^>]+id="gsc_prf_pup-img"[^>]*>', html)
    image_url = ""
    if img_m:
        img_tag = img_m.group(0)
        src_m = re.search(r'src="([^"]+)"', img_tag)
        if src_m:
            image_url = src_m.group(1).replace("&amp;", "&")
        if image_url.startswith('/'):
            image_url = "https://scholar.google.com" + image_url
            
        img_name = name.lower().replace(' ', '_').replace('.', '') + ".jpg"
        img_path = f"assets/organizer_images/{img_name}"
        
        # Download image
        try:
            img_req = urllib.request.Request(image_url, headers=headers)
            with open(img_path, 'wb') as f:
                f.write(urllib.request.urlopen(img_req).read())
        except Exception as e:
            print(f"Failed to download image: {e}")
            img_path = ""
    else:
        img_path = ""
        
    person = {
        "name": name,
        "image": img_path,
        "url": homepage,
        "role": "Advisor",
        "affiliation": affiliation
    }
    
    if "Iryna" in name:
        person["role"] = "Organizer"
        organizers.append(person)
    else:
        advisors.append(person)

out = {
    "advisors": advisors,
    "organizers": organizers
}
print(json.dumps(out, indent=2))
