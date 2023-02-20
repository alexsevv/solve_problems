# код страницы 
# network 
# обновляем страницу
# из списка 200ок выбираем первый и правой кнопкой copy - copy as cURL
# идем на сайт https://curlconverter.com/
# сконвертируемое вставляем в файл и пишем спарсенные данные в файл

import requests

cookies = {
    '_device_id': '5d9611f043a9b3805b7bfe82cd187658',
    '_octo': 'GH1.1.1479756642.1665130735',
    'preferred_color_mode': 'light',
    'tz': 'Europe%2FMoscow',
    'user_session': 'LBx0w_maYUzmfWfKCbaO9nHDjKOG4JCdfpJ95--qCSmFUJGL',
    '__Host-user_session_same_site': 'LBx0w_maYUzmfWfKCbaO9nHDjKOG4JCdfpJ95--qCSmFUJGL',
    'tz': 'Europe%2FMoscow',
    'color_mode': '%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
    'logged_in': 'yes',
    'dotcom_user': 'alexsevv',
    'has_recent_activity': '1',
    '_gh_sess': 'QkJ7%2FYamNg7TmPhDYr0eyldToNobT1LT2jYcJCUdBmxc6NdUSg74SM6tyKH%2FG9RuzJK99A629dUUOhxHFfZDsW%2BnbflpK4YLh7Ggn6PDStQuL7yJvKjEAze6lvzHZGbuyLiC7JUELgq2OyM3LuK2k7xK6rpKxuxpIerHkUxWzGpLeRZoOHj4ArntSRfUQhIQWmI6B7gdlk0w7tWhJC2CeutLF0A2C5e6aUD81H%2BWda63k%2BPrWKmPC6eykcF6AbReJmM1ivMazdJXLzClguJm4W1SHBjKroNGREP1nNxs9rmvjDKit%2BoiBnylkAI5UOGUk5PRkxgM27XhqVXxUqpV7%2BdphuZ4tJC2xgU8vBufewZnraN8d1YJM0VCDcYCvA1TC6FKoKLn2KnYk7Fuiro9PpyZYKWHiBQHiGmANaY86ZF0ne%2BSiB1rfAQ06MBsqeFYJ38Kx6XN%2FQ9X%2B0vgjxfhCWPWHadfAeiAedGEEW%2Bos7mK1zkfAGaj6wadKCyYjKmKO5z68BydV8lsxdJ7jvvieVjRiEYg8RRrOdamLITWnYSi3L0H8Zh71TeYqfvF8g45HQ7Bv6bPjrGVIlZDHfDOgrw1wjPwS6BJviuOScPkxl1K8FX7eNwCyr7S9z1dSj9mNfNaSMEfxKEES9AprmoHO3MmetuI%2BXVLmfTxpBfGSei8Mq%2FlKNKwmSxsoIu4kSf2beRwqbn2eWEqwOmaUSLItEaRUNSz%2FhBTfkysDMGqc0pVWEeKv9kL1QTgqQOEas7YV24oQX38N%2BQs06G3qh0Y6SYtBCuiBq9ncE9loImFYoa3JTXuedxaXLbA6GDpgridQbDbYTquNlJtK%2F5KSxHGTI8oDmG%2BPql4U6Rwshgy1b%2Fqb6MUEg%3D%3D--GGurgKTJouuB2rdj--Dfw0Oe%2FrbPbia6iBofmkcQ%3D%3D',
}

headers = {
    'authority': 'github.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_device_id=5d9611f043a9b3805b7bfe82cd187658; _octo=GH1.1.1479756642.1665130735; preferred_color_mode=light; tz=Europe%2FMoscow; user_session=LBx0w_maYUzmfWfKCbaO9nHDjKOG4JCdfpJ95--qCSmFUJGL; __Host-user_session_same_site=LBx0w_maYUzmfWfKCbaO9nHDjKOG4JCdfpJ95--qCSmFUJGL; tz=Europe%2FMoscow; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=alexsevv; has_recent_activity=1; _gh_sess=QkJ7%2FYamNg7TmPhDYr0eyldToNobT1LT2jYcJCUdBmxc6NdUSg74SM6tyKH%2FG9RuzJK99A629dUUOhxHFfZDsW%2BnbflpK4YLh7Ggn6PDStQuL7yJvKjEAze6lvzHZGbuyLiC7JUELgq2OyM3LuK2k7xK6rpKxuxpIerHkUxWzGpLeRZoOHj4ArntSRfUQhIQWmI6B7gdlk0w7tWhJC2CeutLF0A2C5e6aUD81H%2BWda63k%2BPrWKmPC6eykcF6AbReJmM1ivMazdJXLzClguJm4W1SHBjKroNGREP1nNxs9rmvjDKit%2BoiBnylkAI5UOGUk5PRkxgM27XhqVXxUqpV7%2BdphuZ4tJC2xgU8vBufewZnraN8d1YJM0VCDcYCvA1TC6FKoKLn2KnYk7Fuiro9PpyZYKWHiBQHiGmANaY86ZF0ne%2BSiB1rfAQ06MBsqeFYJ38Kx6XN%2FQ9X%2B0vgjxfhCWPWHadfAeiAedGEEW%2Bos7mK1zkfAGaj6wadKCyYjKmKO5z68BydV8lsxdJ7jvvieVjRiEYg8RRrOdamLITWnYSi3L0H8Zh71TeYqfvF8g45HQ7Bv6bPjrGVIlZDHfDOgrw1wjPwS6BJviuOScPkxl1K8FX7eNwCyr7S9z1dSj9mNfNaSMEfxKEES9AprmoHO3MmetuI%2BXVLmfTxpBfGSei8Mq%2FlKNKwmSxsoIu4kSf2beRwqbn2eWEqwOmaUSLItEaRUNSz%2FhBTfkysDMGqc0pVWEeKv9kL1QTgqQOEas7YV24oQX38N%2BQs06G3qh0Y6SYtBCuiBq9ncE9loImFYoa3JTXuedxaXLbA6GDpgridQbDbYTquNlJtK%2F5KSxHGTI8oDmG%2BPql4U6Rwshgy1b%2Fqb6MUEg%3D%3D--GGurgKTJouuB2rdj--Dfw0Oe%2FrbPbia6iBofmkcQ%3D%3D',
    'if-none-match': 'W/"11700d7f4fae26a14b9b5f0a4c1f486c"',
    'referer': 'https://github.com/notifications',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

response = requests.get('https://github.com/', cookies=cookies, headers=headers)

with open('parsing_web_page_result.html', 'w') as file:
    file.write(response.text)
