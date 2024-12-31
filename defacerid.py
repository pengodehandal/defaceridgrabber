import requests
from bs4 import BeautifulSoup
import re
import time

def get_domains_from_page(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat mengakses {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all('tr')

    url_pattern = r'(?:https?://)?([a-zA-Z0-9.-]+)'

    domains = []

    for row in rows:
        td_elements = row.find_all('td')
        if len(td_elements) > 7:
            website_text = td_elements[7].get_text()
            match = re.search(url_pattern, website_text)
            if match:
                domain = match.group(1)
                domains.append(domain)

    return domains

def scrape_normal_archive():
    all_domains = []
    
    for page_num in range(1, 31):
        url = f"https://defacer.id/archive/{page_num}"
        print(f"\nMengakses halaman {url}...")

        domains = get_domains_from_page(url)

        print(f"Jumlah domain ditemukan di halaman {page_num}: {len(domains)}")

        all_domains.extend(domains)

        if domains:
            with open("DefacerIDGrab.txt", "a") as file:
                for domain in domains:
                    file.write(domain + "\n")

        time.sleep(0.5)

    print(f"Semua domain berhasil disimpan ke dalam DefacerIDGrab.txt")

def scrape_special_archive():
    all_domains = []
    
    for page_num in range(1, 31):
        url = f"https://defacer.id/archive/special/{page_num}"
        print(f"\nMengakses halaman {url}...")

        domains = get_domains_from_page(url)

        print(f"Jumlah domain ditemukan di halaman {page_num}: {len(domains)}")

        all_domains.extend(domains)

        if domains:
            with open("DefacerIDGrabSpecial.txt", "a") as file:
                for domain in domains:
                    file.write(domain + "\n")

        time.sleep(0.5)

    print(f"Semua domain berhasil disimpan ke dalam DefacerIDGrabSpecial.txt")

def scrape_onhold_archive():
    all_domains = []
    
    for page_num in range(1, 31):
        url = f"https://defacer.id/archive/onhold/{page_num}"
        print(f"\nMengakses halaman {url}...")

        domains = get_domains_from_page(url)

        print(f"Jumlah domain ditemukan di halaman {page_num}: {len(domains)}")

        all_domains.extend(domains)

        if domains:
            with open("DefacerIDGrabOnhold.txt", "a") as file:
                for domain in domains:
                    file.write(domain + "\n")

        time.sleep(0.5)

    print(f"Semua domain berhasil disimpan ke dalam DefacerIDGrabOnhold.txt")

def scrape_all_automatically():
    all_domains = []

    for page_num in range(1, 31):
        url_normal = f"https://defacer.id/archive/{page_num}"
        print(f"\nMengakses halaman {url_normal}...")
        domains_normal = get_domains_from_page(url_normal)
        print(f"Jumlah domain ditemukan di halaman {page_num} arsip biasa: {len(domains_normal)}")
        all_domains.extend(domains_normal)

        url_special = f"https://defacer.id/archive/special/{page_num}"
        print(f"Mengakses halaman {url_special}...")
        domains_special = get_domains_from_page(url_special)
        print(f"Jumlah domain ditemukan di halaman {page_num} arsip special: {len(domains_special)}")
        all_domains.extend(domains_special)

        url_onhold = f"https://defacer.id/archive/onhold/{page_num}"
        print(f"Mengakses halaman {url_onhold}...")
        domains_onhold = get_domains_from_page(url_onhold)
        print(f"Jumlah domain ditemukan di halaman {page_num} arsip onhold: {len(domains_onhold)}")
        all_domains.extend(domains_onhold)

        with open("DefacerIDGrabAllAso.txt", "a") as file:
            for domain in domains_normal + domains_special + domains_onhold:
                file.write(domain + "\n")

        time.sleep(0.5)

    print(f"Semua domain berhasil disimpan ke dalam DefacerIDGrabAllAso.txt")

def main():
    while True:
        print("https://github.com/pengodehandal/defaceridgrabber/")
        print("\nPilih opsi:")
        print("1. Grab Biasa")
        print("2. Grab Special")
        print("3. Grab Onhold")
        print("4. Grab dari Arsip Special dan Onhold (Semua Sekaligus)")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5): ")

        if choice == '1':
            print("Sabar...")
            scrape_normal_archive()
        elif choice == '2':
            print("Sabar...")
            scrape_special_archive()
        elif choice == '3':
            print("Sabar...")
            scrape_onhold_archive()
        elif choice == '4':
            print("Sabar...")
            scrape_all_automatically()
        elif choice == '5':
            print("Makasih Cok")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
