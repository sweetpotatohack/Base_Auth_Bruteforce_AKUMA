  **AKUMA BASE_AUTH BRUTEFORCER - 悪魔の認証破壊ツール**  

**"In the crimson glow of forbidden login portals, AKUMA whispers the keys to your kingdom..."**  

🚀 **悪魔の概要 (Demon Overview)**  

AKUMA BASE_AUTH BRUTEFORCER (悪魔 - "Demon") is a relentless HTTP Basic Authentication cracking tool forged in Tokyo's underground cyber dojos. Designed for red teams and penetration testers, it combines surgical precision with brute-force efficiency to  atter weak credentials.  

**"When the gates won't open... let the demon knock."**  

   🔥 **悪魔の特徴 (Features of the Demon)**  

   **1. 地獄のコア (Hell Core Engine)**  
- **Multi-threaded chaos**: 10-100x faster than traditional brute-forcers (`-t 50`)  
- **Proxy bloodline**: SOCKS5/HTTP(s) support with Tor anonymity (`-p socks5://127.0.0.1:9050`)  
- **Captcha exorcism**: Automatically solves simple CAPTCHAs (`-c http://target/captcha`)  

    **2. 幽霊の戦術 (Phantom Tactics)**  
- **Randomized delays**: Evades rate-limiting (`-d 1.5`)  
- **User-Agent possession**: Spoofs browsers/mobile devices  
- **SSL/TLS obfuscation**: Bypasses weak certificate validation  

    **3. 血のモジュール (Blood Modules)**  
- **Dictionary onslaught**: Cru es weak passwords (`-Pf rockyou.txt`)  
- **Credential stuffing**: Tests breached credentials (`-Uf darkweb_users.txt`)  
- **Session hijacking**: Steals valid cookies post-auth  

    **4. 鬼の出力 (Oni Output)**  
- **Real-time logging**: `success.log` tracks all victories  
- **Neon terminal UI**: Color-coded results (red = success, blue = failure)  
- **JSON/CSV reports**: For integration with other tools  

   ⚡ **起動コマンド (Activation Sequence)**  

``` 
python3 akuma_bruteforce.py -u https://admin.example.com -Uf users.txt -Pf passwords.txt -t 20 -d 0.3 -p socks5://127.0.0.1:9050
```  

   **常用コマンド (Common Commands)**  

| Command | Description | Example |  
|---------|-------------|---------|  
| `-u` | Target URL | `-u https://target.com` |  
| `-U` | Single username | `-U admin` |  
| `-P` | Single password | `-P password123` |  
| `-Uf` | Username wordlist | `-Uf users.txt` |  
| `-Pf` | Password wordlist | `-Pf rockyou.txt` |  
| `-t` | Threads (speed) | `-t 30` |  
| `-d` | Delay (stealth) | `-d 1.2` |  
| `-p` | Proxy (Tor/VPN) | `-p http://proxy:8080` |  
| `-c` | CAPTCHA URL | `-c http://target/captcha.php` |  

   💀 **システム要件 (System Requirements)**  

   **地獄の依存関係 (Dependencies from Hell)**  
``` 
pip3 install requests tqdm concurrent-log-handler
```  

   **Tor Proxy Setup (Optional)**  
``` 
sudo apt install tor
service tor start
```  
   🌌 **出力例 (Sample Output)**  

``` 
[血月昇る] Bruteforce started...
[!] Target: https://admin.example.com  
[!] Loaded 50 users × 100,000 passwords  
[⚡] Threads: 20 | Delay: 0.3s | Proxy: SOCKS5  

[-] Failed: admin:password123 (403)  
[-] Failed: root:123456 (401)  
[✅] SUCCESS: administrator:admin@123 (200) *SAVED TO success.log*  
[🔥] 1 valid credentials found in 12m 34s.  
```  
   ⚠️ **免責事項 (Disclaimer)**  

**このツールは合法的なセキュリティテスト専用です。**  
*"The demon bites both ways - unauthorized use will summon legal hellhounds."*  

```
          _  _                  _  _            
         / \/ \   _   _   _   / \/ \    _   _  
        / /\_/\ / \ / \ / \ / /\_/\ \ / \ / \ 
        \/      \_/ \_/ \_/ \/      \/ \_/ \_/ 
        悪魔はパスワードを見る...
```  

**Github:** [https://github.com/sweetpotatohack/Base_Auth_Bruteforce_AKUMA](https://github.com/sweetpotatohack/Base_Auth_Bruteforce_AKUMA)  
**License:** BSD 3-Clause "New" or "Revised" License (血の誓約)  

--- 

**"Exploit with honor. Cra  with glory."** 🔪

  **AKUMA BASE_AUTH BRUTEFORCER - Демонический взломщик базовой аутентификации**  

**"В кровавом свете запретных точек входа, AKUMA шепчет вам ключи от королевства..."**  
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 **Обзор демона**  

AKUMA BASE_AUTH BRUTEFORCER (яп. 悪魔 - "Демон") - это беспощадный инструмент для взлома HTTP Basic Authentication, созданный в кибердодзё токийского андеграунда. Разработан для red team и пентестеров, сочетает хирургическую точность с грубой силой для взлома слабых учетных данных.  

**"Когда ворота не открываются... позволь демону постучаться."**  

   🔥 **Особенности демона**  

   **1. Адское ядро**  
- **Многопоточный хаос**: в 10-100 раз быстрее обычных брутфорсеров (`-t 50`)  
- **Прокси-кровь**: поддержка SOCKS5/HTTP(s) с анонимностью Tor (`-p socks5://127.0.0.1:9050`)  
- **Изгнание капчи**: автоматическое решение простых капч (`-c http://target/captcha`)  

    **2. Тактика призрака**  
- **Случайные задержки**: обход ограничений скорости (`-d 1.5`)  
- **Смена User-Agent**: маскировка под браузеры/мобильные устройства  
- **Обфускация SSL/TLS**: обход слабой проверки сертификатов  

    **3. Кровавые модули**  
- **Атака словаря**: уничтожение слабых паролей (`-Pf rockyou.txt`)  
- **Credential stuffing**: проверка слитых учетных данных (`-Uf darkweb_users.txt`)  
- **Угоны сессий**: кража валидных куков после аутентификации  

    **4. Демонический вывод**  
- **Логирование в реальном времени**: `success.log` сохраняет все успехи  
- **Неоновый интерфейс**: цветные результаты (красный = успех, синий = провал)  
- **Отчеты JSON/CSV**: для интеграции с другими инструментами  

   ⚡ **Команды запуска**  

``` 
python3 akuma_bruteforce.py -u https://admin.example.com -Uf users.txt -Pf passwords.txt -t 20 -d 0.3 -p socks5://127.0.0.1:9050
```  

   **Частые команды**  

| Команда | Описание | Пример |  
|---------|-------------|---------|  
| `-u` | Целевой URL | `-u https://target.com` |  
| `-U` | Один логин | `-U admin` |  
| `-P` | Один пароль | `-P password123` |  
| `-Uf` | Словарь логинов | `-Uf users.txt` |  
| `-Pf` | Словарь паролей | `-Pf rockyou.txt` |  
| `-t` | Потоки (скорость) | `-t 30` |  
| `-d` | Задержка (скрытность) | `-d 1.2` |  
| `-p` | Прокси (Tor/VPN) | `-p http://proxy:8080` |  
| `-c` | URL капчи | `-c http://target/captcha.php` |  

   💀 **Системные требования**  

   **Адские зависимости**  
``` 
pip3 install requests tqdm concurrent-log-handler
```  
   **Настройка Tor (опционально)**  
``` 
sudo apt install tor
service tor start
```  
   🌌 **Пример вывода**  

``` 
[Кровавая луна] Bruteforce запущен...
[!] Цель: https://admin.example.com  
[!] Загружено 50 логинов × 100,000 паролей  
[⚡] Потоки: 20 | Задержка: 0.3s | Прокси: SOCKS5  

[-] Неудача: admin:password123 (403)  
[-] Неудача: root:123456 (401)  
[✅] УСПЕХ: administrator:admin@123 (200) *СОХРАНЕНО В success.log*  
[🔥] Найдено 1 валидных учетных данных за 12m 34s.  
```  
   ⚠️ **Дисклеймер**  

**Этот инструмент предназначен только для легального тестирования безопасности.**  
*"Демон кусает обе стороны - несанкционированное использование вызовет юридических адских гончих."*  

```
          _  _                  _  _            
         / \/ \   _   _   _   / \/ \    _   _  
        / /\_/\ / \ / \ / \ / /\_/\ \ / \ / \ 
        \/      \_/ \_/ \_/ \/      \/ \_/ \_/ 
        Демон видит пароли...
```  

**Github:** [https://github.com/sweetpotatohack/Base_Auth_Bruteforce_AKUMA](https://github.com/sweetpotatohack/Base_Auth_Bruteforce_AKUMA)  
**Лицензия:** BSD 3-Clause "New" or "Revised" License (Кровавая клятва)  

--- 

**"Взламывай с честью. Падай с славой."** 🔪
