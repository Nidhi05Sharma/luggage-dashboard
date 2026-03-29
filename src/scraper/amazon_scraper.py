import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0"
}


# ----------------------------
# SCRAPE SINGLE PRODUCT
# ----------------------------
def scrape_product(url):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # TITLE
        title_tag = soup.find("span", id="productTitle")
        title = title_tag.get_text(strip=True) if title_tag else None

        # PRICE
        price_tag = soup.find("span", class_="a-price-whole")
        price = price_tag.get_text(strip=True) if price_tag else None

        # RATING
        rating_tag = soup.find("span", class_="a-icon-alt")
        rating = rating_tag.get_text(strip=True) if rating_tag else None

        # REVIEW COUNT
        review_tag = soup.find("span", id="acrCustomerReviewText")
        review_count = review_tag.get_text(strip=True) if review_tag else None

        return {
            "title": title,
            "price": price,
            "rating": rating,
            "review_count": review_count
        }

    except Exception as e:
        print("Error:", e)
        return None


# ----------------------------
# 🔥 MULTI-BRAND INPUT
# ----------------------------
brand_urls = {
    "Safari": [
        "https://www.amazon.in/Safari-Polycarbonate-Wheeling-Suitcase-Champagne/dp/B0F9FMQZWN/ref=sr_1_1_sspa?crid=1BYQ844PJWV20&dib=eyJ2IjoiMSJ9.uzZyjmnvROwVEwzzZL3wWFM1Wg07qWi8VuTwkjXPbJT3ufTms2gB2Vw0knh7lpP2JyhBsyLV9e_MuyWi6IayYuGjXv04NO8SYQRq-d4gbFx1r9_LRhBeWqQXkLXpn7UpWkOVbea55h-9xzYn3tQ0emLDR3TNWNfFIkC6Ze_C9FMvPcHCIfa9YdcwumOHFW2t-k4MLYUFW5nkRtmtWKnaU2E2HGVdRXw-OIr3sQCU9gUYcW7mbOrlX8esHuLUGVklWGuToYR7r9yAChngKZ5A7lyfKzVq637qU81W0govAtU.KjT4SFQFJdTrl5ZeLaCHrLlUhYqPvNhEEatX8fJHEAE&dib_tag=se&keywords=SAFARI%2Bluggage&qid=1774795679&sprefix=safari%2Blugga%2Caps%2C498&sr=8-1-spons&aref=vkYv9kYlV4&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "https://www.amazon.in/Safari-Pentagon-Polypropylene-Wheeling-Suitcase/dp/B097BG27MD/ref=sr_1_3_sspa?crid=1BYQ844PJWV20&dib=eyJ2IjoiMSJ9.uzZyjmnvROwVEwzzZL3wWFM1Wg07qWi8VuTwkjXPbJT3ufTms2gB2Vw0knh7lpP2JyhBsyLV9e_MuyWi6IayYuGjXv04NO8SYQRq-d4gbFx1r9_LRhBeWqQXkLXpn7UpWkOVbea55h-9xzYn3tQ0emLDR3TNWNfFIkC6Ze_C9FMvPcHCIfa9YdcwumOHFW2t-k4MLYUFW5nkRtmtWKnaU2E2HGVdRXw-OIr3sQCU9gUYcW7mbOrlX8esHuLUGVklWGuToYR7r9yAChngKZ5A7lyfKzVq637qU81W0govAtU.KjT4SFQFJdTrl5ZeLaCHrLlUhYqPvNhEEatX8fJHEAE&dib_tag=se&keywords=SAFARI%2Bluggage&qid=1774795679&sprefix=safari%2Blugga%2Caps%2C498&sr=8-3-spons&aref=ftyl9PtuKX&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "https://www.amazon.in/Safari-Trolley-Polypropylene-Wheeling-Suitcase/dp/B0FLYG5Y79/ref=sr_1_8?crid=1BYQ844PJWV20&dib=eyJ2IjoiMSJ9.uzZyjmnvROwVEwzzZL3wWFM1Wg07qWi8VuTwkjXPbJT3ufTms2gB2Vw0knh7lpP2JyhBsyLV9e_MuyWi6IayYuGjXv04NO8SYQRq-d4gbFx1r9_LRhBeWqQXkLXpn7UpWkOVbea55h-9xzYn3tQ0emLDR3TNWNfFIkC6Ze_C9FMvPcHCIfa9YdcwumOHFW2t-k4MLYUFW5nkRtmtWKnaU2E2HGVdRXw-OIr3sQCU9gUYcW7mbOrlX8esHuLUGVklWGuToYR7r9yAChngKZ5A7lyfKzVq637qU81W0govAtU.KjT4SFQFJdTrl5ZeLaCHrLlUhYqPvNhEEatX8fJHEAE&dib_tag=se&keywords=SAFARI%2Bluggage&qid=1774795679&sprefix=safari%2Blugga%2Caps%2C498&sr=8-8&th=1",
        "https://www.amazon.in/Safari-Polycarbonate-Wheeling-Speed_Wheel-Suitcase/dp/B097JMXLT9/ref=sr_1_10?crid=1BYQ844PJWV20&dib=eyJ2IjoiMSJ9.uzZyjmnvROwVEwzzZL3wWFM1Wg07qWi8VuTwkjXPbJT3ufTms2gB2Vw0knh7lpP2JyhBsyLV9e_MuyWi6IayYuGjXv04NO8SYQRq-d4gbFx1r9_LRhBeWqQXkLXpn7UpWkOVbea55h-9xzYn3tQ0emLDR3TNWNfFIkC6Ze_C9FMvPcHCIfa9YdcwumOHFW2t-k4MLYUFW5nkRtmtWKnaU2E2HGVdRXw-OIr3sQCU9gUYcW7mbOrlX8esHuLUGVklWGuToYR7r9yAChngKZ5A7lyfKzVq637qU81W0govAtU.KjT4SFQFJdTrl5ZeLaCHrLlUhYqPvNhEEatX8fJHEAE&dib_tag=se&keywords=SAFARI%2Bluggage&qid=1774795679&sprefix=safari%2Blugga%2Caps%2C498&sr=8-10&th=1",
        "https://www.amazon.in/Safari-Trolley-Polycarbonate-Wheeling-Suitcase/dp/B0FNDBNFDB/ref=sr_1_14?crid=1BYQ844PJWV20&dib=eyJ2IjoiMSJ9.uzZyjmnvROwVEwzzZL3wWFM1Wg07qWi8VuTwkjXPbJT3ufTms2gB2Vw0knh7lpP2JyhBsyLV9e_MuyWi6IayYuGjXv04NO8SYQRq-d4gbFx1r9_LRhBeWqQXkLXpn7UpWkOVbea55h-9xzYn3tQ0emLDR3TNWNfFIkC6Ze_C9FMvPcHCIfa9YdcwumOHFW2t-k4MLYUFW5nkRtmtWKnaU2E2HGVdRXw-OIr3sQCU9gUYcW7mbOrlX8esHuLUGVklWGuToYR7r9yAChngKZ5A7lyfKzVq637qU81W0govAtU.KjT4SFQFJdTrl5ZeLaCHrLlUhYqPvNhEEatX8fJHEAE&dib_tag=se&keywords=SAFARI%2Bluggage&qid=1774795679&sprefix=safari%2Blugga%2Caps%2C498&sr=8-14&th=1",
        "https://www.amazon.in/Safari-Polycarbonate-Wheeling-Suitcase-Multicolour/dp/B0FGJKJCR5/ref=sr_1_19?crid=1BYQ844PJWV20&dib=eyJ2IjoiMSJ9.uzZyjmnvROwVEwzzZL3wWFM1Wg07qWi8VuTwkjXPbJT3ufTms2gB2Vw0knh7lpP2JyhBsyLV9e_MuyWi6IayYuGjXv04NO8SYQRq-d4gbFx1r9_LRhBeWqQXkLXpn7UpWkOVbea55h-9xzYn3tQ0emLDR3TNWNfFIkC6Ze_C9FMvPcHCIfa9YdcwumOHFW2t-k4MLYUFW5nkRtmtWKnaU2E2HGVdRXw-OIr3sQCU9gUYcW7mbOrlX8esHuLUGVklWGuToYR7r9yAChngKZ5A7lyfKzVq637qU81W0govAtU.KjT4SFQFJdTrl5ZeLaCHrLlUhYqPvNhEEatX8fJHEAE&dib_tag=se&keywords=SAFARI%2Bluggage&qid=1774795679&sprefix=safari%2Blugga%2Caps%2C498&sr=8-19&th=1"        
    ],
    "American Tourister": [
        "https://www.amazon.in/American-Tourister-27O-70-001/dp/B073XL1C3W/ref=sr_1_14?crid=3QC018783KVQQ&dib=eyJ2IjoiMSJ9.0Hbgw669abpNXpyakBDRaHtciLUyYeiAv4dcQKNKFxxUHMZvxCH80N3U2u3rMQrZPcW8Gyr5kA2YCUb5ymCLEjkpPOTOiZMaRMXNSsLuaclq8Gm41_Kbf-UMGxHS-s9x3Kro3yhvd6SFogzCgJhyen_aPEmYBtnwhIwAv_9gJae00tU9GE3R7VPkSdOyPLqdg2muwFa1OeirsYr1CvjQ7xw_vBQ8ITUZD5yNPzFc71JzoBB4HsfmlHFN92ncL2NP0LzfIHWyoMWwdahwu1X-m4GCBD-cnWAkeXEXv7e-ImA.YN-JMMwIrWP2neqhgEgj4PADcxyvKkr5ihD3eyhGS8M&dib_tag=se&keywords=american%2Btourister%2Bluggage&qid=1774804251&sprefix=american%2Btouristeluggage%2Caps%2C376&sr=8-14&th=1",
        "https://www.amazon.in/American-Tourister-Splash-Luggage-Complete/dp/B0CHRL351K/ref=sr_1_11?crid=3QC018783KVQQ&dib=eyJ2IjoiMSJ9.0Hbgw669abpNXpyakBDRaHtciLUyYeiAv4dcQKNKFxxUHMZvxCH80N3U2u3rMQrZPcW8Gyr5kA2YCUb5ymCLEjkpPOTOiZMaRMXNSsLuaclq8Gm41_Kbf-UMGxHS-s9x3Kro3yhvd6SFogzCgJhyen_aPEmYBtnwhIwAv_9gJae00tU9GE3R7VPkSdOyPLqdg2muwFa1OeirsYr1CvjQ7xw_vBQ8ITUZD5yNPzFc71JzoBB4HsfmlHFN92ncL2NP0LzfIHWyoMWwdahwu1X-m4GCBD-cnWAkeXEXv7e-ImA.YN-JMMwIrWP2neqhgEgj4PADcxyvKkr5ihD3eyhGS8M&dib_tag=se&keywords=american%2Btourister%2Bluggage&qid=1774804251&sprefix=american%2Btouristeluggage%2Caps%2C376&sr=8-11&th=1",
        "https://www.amazon.in/American-Tourister-Liftoff-Suitcase-Trolley/dp/B0F5HGLC5Q/ref=sr_1_8?crid=3QC018783KVQQ&dib=eyJ2IjoiMSJ9.0Hbgw669abpNXpyakBDRaHtciLUyYeiAv4dcQKNKFxxUHMZvxCH80N3U2u3rMQrZPcW8Gyr5kA2YCUb5ymCLEjkpPOTOiZMaRMXNSsLuaclq8Gm41_Kbf-UMGxHS-s9x3Kro3yhvd6SFogzCgJhyen_aPEmYBtnwhIwAv_9gJae00tU9GE3R7VPkSdOyPLqdg2muwFa1OeirsYr1CvjQ7xw_vBQ8ITUZD5yNPzFc71JzoBB4HsfmlHFN92ncL2NP0LzfIHWyoMWwdahwu1X-m4GCBD-cnWAkeXEXv7e-ImA.YN-JMMwIrWP2neqhgEgj4PADcxyvKkr5ihD3eyhGS8M&dib_tag=se&keywords=american%2Btourister%2Bluggage&qid=1774804251&sprefix=american%2Btouristeluggage%2Caps%2C376&sr=8-8&th=1",
        "https://www.amazon.in/American-Tourister-Suitcase-Trolley-Combination/dp/B0F5HQQ361/ref=sr_1_7?crid=3QC018783KVQQ&dib=eyJ2IjoiMSJ9.0Hbgw669abpNXpyakBDRaHtciLUyYeiAv4dcQKNKFxxUHMZvxCH80N3U2u3rMQrZPcW8Gyr5kA2YCUb5ymCLEjkpPOTOiZMaRMXNSsLuaclq8Gm41_Kbf-UMGxHS-s9x3Kro3yhvd6SFogzCgJhyen_aPEmYBtnwhIwAv_9gJae00tU9GE3R7VPkSdOyPLqdg2muwFa1OeirsYr1CvjQ7xw_vBQ8ITUZD5yNPzFc71JzoBB4HsfmlHFN92ncL2NP0LzfIHWyoMWwdahwu1X-m4GCBD-cnWAkeXEXv7e-ImA.YN-JMMwIrWP2neqhgEgj4PADcxyvKkr5ihD3eyhGS8M&dib_tag=se&keywords=american%2Btourister%2Bluggage&qid=1774804251&sprefix=american%2Btouristeluggage%2Caps%2C376&sr=8-7&th=1",
        "https://www.amazon.in/American-Tourister-Expandable-Polyester-Combination/dp/B0CW9X3TB3/ref=sr_1_6?crid=3QC018783KVQQ&dib=eyJ2IjoiMSJ9.0Hbgw669abpNXpyakBDRaHtciLUyYeiAv4dcQKNKFxxUHMZvxCH80N3U2u3rMQrZPcW8Gyr5kA2YCUb5ymCLEjkpPOTOiZMaRMXNSsLuaclq8Gm41_Kbf-UMGxHS-s9x3Kro3yhvd6SFogzCgJhyen_aPEmYBtnwhIwAv_9gJae00tU9GE3R7VPkSdOyPLqdg2muwFa1OeirsYr1CvjQ7xw_vBQ8ITUZD5yNPzFc71JzoBB4HsfmlHFN92ncL2NP0LzfIHWyoMWwdahwu1X-m4GCBD-cnWAkeXEXv7e-ImA.YN-JMMwIrWP2neqhgEgj4PADcxyvKkr5ihD3eyhGS8M&dib_tag=se&keywords=american%2Btourister%2Bluggage&qid=1774804251&sprefix=american%2Btouristeluggage%2Caps%2C376&sr=8-6&th=1",
        "https://www.amazon.in/AMERICAN-TOURISTER-AMT-68cm-Polypropylene/dp/B09RPLYFXJ/ref=sr_1_5?crid=3QC018783KVQQ&dib=eyJ2IjoiMSJ9.0Hbgw669abpNXpyakBDRaHtciLUyYeiAv4dcQKNKFxxUHMZvxCH80N3U2u3rMQrZPcW8Gyr5kA2YCUb5ymCLEjkpPOTOiZMaRMXNSsLuaclq8Gm41_Kbf-UMGxHS-s9x3Kro3yhvd6SFogzCgJhyen_aPEmYBtnwhIwAv_9gJae00tU9GE3R7VPkSdOyPLqdg2muwFa1OeirsYr1CvjQ7xw_vBQ8ITUZD5yNPzFc71JzoBB4HsfmlHFN92ncL2NP0LzfIHWyoMWwdahwu1X-m4GCBD-cnWAkeXEXv7e-ImA.YN-JMMwIrWP2neqhgEgj4PADcxyvKkr5ihD3eyhGS8M&dib_tag=se&keywords=american%2Btourister%2Bluggage&qid=1774804251&sprefix=american%2Btouristeluggage%2Caps%2C376&sr=8-5&th=1"
    ],
    "VIP": [
        "https://www.amazon.in/VIP-Voyager-Polypropylene-Check-Suitcase/dp/B0BH4J7QJP/ref=sr_1_10?crid=3BL6QKFY7ZYYL&dib=eyJ2IjoiMSJ9.Mtp812deczl4PTXOEiOiV6u1BGrmtKtNdViaBwGD8HPf4Ro3wvzHAfenYjywYvibTUIlPBeJ0LbQpj-Rwy3LZfkc6z-9eolmVnvKP7FWSY4Bq5I4rNm6I4DAIO7OYfcDqdIVvpdYWEfzKHbLUeMuw9Jy5jNGcoT4VhSr__btIFRzGnocYeL6cErLOh-5vp6y61k4ATNEvUNHa6keQvRkBgZdnsmQNKFoXhNx2mdAez-41LzDoh-qXLeL33fD9PyfCuS_TQ5uOg7CuY-uyFf5QDpqJVmHF2D54HN9AsdBW4Y.SIeOAofR17wvSVOdDP7f5WnpbitO6RJeIsii5ZWVmHQ&dib_tag=se&keywords=VIP+luggage&qid=1774804479&sprefix=vip+luggage%2Caps%2C472&sr=8-10",
        "https://www.amazon.in/VIP-Polypropylene-Hardshell-Lightweight-Combination/dp/B0D4RD23TM/ref=sr_1_12?crid=3BL6QKFY7ZYYL&dib=eyJ2IjoiMSJ9.Mtp812deczl4PTXOEiOiV6u1BGrmtKtNdViaBwGD8HPf4Ro3wvzHAfenYjywYvibTUIlPBeJ0LbQpj-Rwy3LZfkc6z-9eolmVnvKP7FWSY4Bq5I4rNm6I4DAIO7OYfcDqdIVvpdYWEfzKHbLUeMuw9Jy5jNGcoT4VhSr__btIFRzGnocYeL6cErLOh-5vp6y61k4ATNEvUNHa6keQvRkBgZdnsmQNKFoXhNx2mdAez-41LzDoh-qXLeL33fD9PyfCuS_TQ5uOg7CuY-uyFf5QDpqJVmHF2D54HN9AsdBW4Y.SIeOAofR17wvSVOdDP7f5WnpbitO6RJeIsii5ZWVmHQ&dib_tag=se&keywords=VIP%2Bluggage&qid=1774804479&sprefix=vip%2Bluggage%2Caps%2C472&sr=8-12&th=1",
        "https://www.amazon.in/VIP-Unicorn-Polyester-Spinner-Trolleys/dp/B0GQF3J624/ref=sr_1_11?crid=3BL6QKFY7ZYYL&dib=eyJ2IjoiMSJ9.Mtp812deczl4PTXOEiOiV6u1BGrmtKtNdViaBwGD8HPf4Ro3wvzHAfenYjywYvibTUIlPBeJ0LbQpj-Rwy3LZfkc6z-9eolmVnvKP7FWSY4Bq5I4rNm6I4DAIO7OYfcDqdIVvpdYWEfzKHbLUeMuw9Jy5jNGcoT4VhSr__btIFRzGnocYeL6cErLOh-5vp6y61k4ATNEvUNHa6keQvRkBgZdnsmQNKFoXhNx2mdAez-41LzDoh-qXLeL33fD9PyfCuS_TQ5uOg7CuY-uyFf5QDpqJVmHF2D54HN9AsdBW4Y.SIeOAofR17wvSVOdDP7f5WnpbitO6RJeIsii5ZWVmHQ&dib_tag=se&keywords=VIP%2Bluggage&qid=1774804479&sprefix=vip%2Bluggage%2Caps%2C472&sr=8-11&th=1",
        "https://www.amazon.in/VIP-Trolley-Lightweight-Combination-Suitcase/dp/B0DD3W11L4/ref=sr_1_9?crid=3BL6QKFY7ZYYL&dib=eyJ2IjoiMSJ9.Mtp812deczl4PTXOEiOiV6u1BGrmtKtNdViaBwGD8HPf4Ro3wvzHAfenYjywYvibTUIlPBeJ0LbQpj-Rwy3LZfkc6z-9eolmVnvKP7FWSY4Bq5I4rNm6I4DAIO7OYfcDqdIVvpdYWEfzKHbLUeMuw9Jy5jNGcoT4VhSr__btIFRzGnocYeL6cErLOh-5vp6y61k4ATNEvUNHa6keQvRkBgZdnsmQNKFoXhNx2mdAez-41LzDoh-qXLeL33fD9PyfCuS_TQ5uOg7CuY-uyFf5QDpqJVmHF2D54HN9AsdBW4Y.SIeOAofR17wvSVOdDP7f5WnpbitO6RJeIsii5ZWVmHQ&dib_tag=se&keywords=VIP%2Bluggage&qid=1774804479&sprefix=vip%2Bluggage%2Caps%2C472&sr=8-9&th=1",
        "https://www.amazon.in/VIP-Unicorn-Polyester-Spinner-Trolleys/dp/B0CBTZP3CL/ref=sr_1_5?crid=3BL6QKFY7ZYYL&dib=eyJ2IjoiMSJ9.Mtp812deczl4PTXOEiOiV6u1BGrmtKtNdViaBwGD8HPf4Ro3wvzHAfenYjywYvibTUIlPBeJ0LbQpj-Rwy3LZfkc6z-9eolmVnvKP7FWSY4Bq5I4rNm6I4DAIO7OYfcDqdIVvpdYWEfzKHbLUeMuw9Jy5jNGcoT4VhSr__btIFRzGnocYeL6cErLOh-5vp6y61k4ATNEvUNHa6keQvRkBgZdnsmQNKFoXhNx2mdAez-41LzDoh-qXLeL33fD9PyfCuS_TQ5uOg7CuY-uyFf5QDpqJVmHF2D54HN9AsdBW4Y.SIeOAofR17wvSVOdDP7f5WnpbitO6RJeIsii5ZWVmHQ&dib_tag=se&keywords=VIP%2Bluggage&qid=1774804479&sprefix=vip%2Bluggage%2Caps%2C472&sr=8-5&th=1",
        "https://www.amazon.in/VIP-Lexus-Hardside-Spinner-Anti-Theft/dp/B0F4K9VLQ8/ref=sr_1_1_sspa?crid=3BL6QKFY7ZYYL&dib=eyJ2IjoiMSJ9.Mtp812deczl4PTXOEiOiV6u1BGrmtKtNdViaBwGD8HPf4Ro3wvzHAfenYjywYvibTUIlPBeJ0LbQpj-Rwy3LZfkc6z-9eolmVnvKP7FWSY4Bq5I4rNm6I4DAIO7OYfcDqdIVvpdYWEfzKHbLUeMuw9Jy5jNGcoT4VhSr__btIFRzGnocYeL6cErLOh-5vp6y61k4ATNEvUNHa6keQvRkBgZdnsmQNKFoXhNx2mdAez-41LzDoh-qXLeL33fD9PyfCuS_TQ5uOg7CuY-uyFf5QDpqJVmHF2D54HN9AsdBW4Y.SIeOAofR17wvSVOdDP7f5WnpbitO6RJeIsii5ZWVmHQ&dib_tag=se&keywords=VIP%2Bluggage&qid=1774804479&sprefix=vip%2Bluggage%2Caps%2C472&sr=8-1-spons&aref=yOSDXSJNoH&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
    ],
    "Aristocrat": [
        "https://www.amazon.in/Aristocrat-Liberty-Combination-International-Warranty/dp/B0FMF3SLPK/ref=sr_1_7?crid=18WGB0DXV805I&dib=eyJ2IjoiMSJ9.LJy59rl1JvS10mHIIxBWT5TP6M88Hjc8YmJoI1KTjdi1lqF5VaKJM1yqh8hVeVOTb2O0IWPF3c7aGP15xsQsKIc8vXK22xfuXddNj4cSJa2T6bziZ_WeefX4SbWesmZDAy7kC1CIs9sW6H2QkZNjWflLzk1sDbZtKTN7NwJEA8MQWwoR3f312rsJuGaCFCmWPcGm7cEOUaTdf-1E4rT2v082B3gMUHhlOhpUHfvcI5VD86v3oQy9tRr5wACBL8rsmKtZ2x2nF_2pMlTUr5EcDYNgW-YHRxv8zC6ccoDDhqA.OIJE_7j4GyorUMvZKR2HmK1y_ufMcnQfTeEYnLLj9aw&dib_tag=se&keywords=aristocrat%2Bluggage&qid=1774804673&sprefix=aristoc%2Bluggage%2Caps%2C405&sr=8-7&th=1",
        "https://www.amazon.in/Aristocrat-Spacious-Polyester-Combination-Dazzling/dp/B0C8YVFRMQ/ref=sr_1_4_sspa?crid=18WGB0DXV805I&dib=eyJ2IjoiMSJ9.LJy59rl1JvS10mHIIxBWT5TP6M88Hjc8YmJoI1KTjdi1lqF5VaKJM1yqh8hVeVOTb2O0IWPF3c7aGP15xsQsKIc8vXK22xfuXddNj4cSJa2T6bziZ_WeefX4SbWesmZDAy7kC1CIs9sW6H2QkZNjWflLzk1sDbZtKTN7NwJEA8MQWwoR3f312rsJuGaCFCmWPcGm7cEOUaTdf-1E4rT2v082B3gMUHhlOhpUHfvcI5VD86v3oQy9tRr5wACBL8rsmKtZ2x2nF_2pMlTUr5EcDYNgW-YHRxv8zC6ccoDDhqA.OIJE_7j4GyorUMvZKR2HmK1y_ufMcnQfTeEYnLLj9aw&dib_tag=se&keywords=aristocrat%2Bluggage&qid=1774804673&sprefix=aristoc%2Bluggage%2Caps%2C405&sr=8-4-spons&aref=fQTYaHrTsa&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "https://www.amazon.in/Aristocrat-Expander-Suitcase-Combination-Construction/dp/B0FPCJX1TR/ref=sr_1_3_sspa?crid=18WGB0DXV805I&dib=eyJ2IjoiMSJ9.LJy59rl1JvS10mHIIxBWT5TP6M88Hjc8YmJoI1KTjdi1lqF5VaKJM1yqh8hVeVOTb2O0IWPF3c7aGP15xsQsKIc8vXK22xfuXddNj4cSJa2T6bziZ_WeefX4SbWesmZDAy7kC1CIs9sW6H2QkZNjWflLzk1sDbZtKTN7NwJEA8MQWwoR3f312rsJuGaCFCmWPcGm7cEOUaTdf-1E4rT2v082B3gMUHhlOhpUHfvcI5VD86v3oQy9tRr5wACBL8rsmKtZ2x2nF_2pMlTUr5EcDYNgW-YHRxv8zC6ccoDDhqA.OIJE_7j4GyorUMvZKR2HmK1y_ufMcnQfTeEYnLLj9aw&dib_tag=se&keywords=aristocrat%2Bluggage&qid=1774804673&sprefix=aristoc%2Bluggage%2Caps%2C405&sr=8-3-spons&aref=t0Uo1rd8iW&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "https://www.amazon.in/Aristocrat-Spinners-Trolley-Lightweight-Anti-Theft/dp/B0DG2CJQCW/ref=sr_1_2_sspa?crid=18WGB0DXV805I&dib=eyJ2IjoiMSJ9.LJy59rl1JvS10mHIIxBWT5TP6M88Hjc8YmJoI1KTjdi1lqF5VaKJM1yqh8hVeVOTb2O0IWPF3c7aGP15xsQsKIc8vXK22xfuXddNj4cSJa2T6bziZ_WeefX4SbWesmZDAy7kC1CIs9sW6H2QkZNjWflLzk1sDbZtKTN7NwJEA8MQWwoR3f312rsJuGaCFCmWPcGm7cEOUaTdf-1E4rT2v082B3gMUHhlOhpUHfvcI5VD86v3oQy9tRr5wACBL8rsmKtZ2x2nF_2pMlTUr5EcDYNgW-YHRxv8zC6ccoDDhqA.OIJE_7j4GyorUMvZKR2HmK1y_ufMcnQfTeEYnLLj9aw&dib_tag=se&keywords=aristocrat%2Bluggage&qid=1774804673&sprefix=aristoc%2Bluggage%2Caps%2C405&sr=8-2-spons&aref=KhygkDZipO&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "https://www.amazon.in/Aristocrat-Suitcase-Combination-Convipack-Warranty/dp/B0FPXK5JRQ/ref=sr_1_9?crid=18WGB0DXV805I&dib=eyJ2IjoiMSJ9.LJy59rl1JvS10mHIIxBWT5TP6M88Hjc8YmJoI1KTjdi1lqF5VaKJM1yqh8hVeVOTb2O0IWPF3c7aGP15xsQsKIc8vXK22xfuXddNj4cSJa2T6bziZ_WeefX4SbWesmZDAy7kC1CIs9sW6H2QkZNjWflLzk1sDbZtKTN7NwJEA8MQWwoR3f312rsJuGaCFCmWPcGm7cEOUaTdf-1E4rT2v082B3gMUHhlOhpUHfvcI5VD86v3oQy9tRr5wACBL8rsmKtZ2x2nF_2pMlTUr5EcDYNgW-YHRxv8zC6ccoDDhqA.OIJE_7j4GyorUMvZKR2HmK1y_ufMcnQfTeEYnLLj9aw&dib_tag=se&keywords=aristocrat%2Bluggage&qid=1774804673&sprefix=aristoc%2Bluggage%2Caps%2C405&sr=8-9&th=1",
        "https://www.amazon.in/Aristocrat-Spacious-Polyester-Combination-Dazzling/dp/B0C8YWY72M/ref=sr_1_1_sspa?crid=38H0BS230YPML&dib=eyJ2IjoiMSJ9.LJy59rl1JvS10mHIIxBWT5TP6M88Hjc8YmJoI1KTjdi1lqF5VaKJM1yqh8hVeVOTb2O0IWPF3c7aGP15xsQsKIc8vXK22xfuXddNj4cSJa2T6bziZ_WeefX4SbWesmZDAy7kC1CIs9sW6H2QkZNjWflLzk1sDbZtKTN7NwJEA8MQWwoR3f312rsJuGaCFCmWPcGm7cEOUaTdf-1E4rT2v082B3gMUHhlOhpUHfvcI5VD86v3oQy9tRr5wACBL8rsmKtZ2x2nF_2pMlTUr5EcDYNgW-YHRxv8zC6ccoDDhqA.OIJE_7j4GyorUMvZKR2HmK1y_ufMcnQfTeEYnLLj9aw&dib_tag=se&keywords=aristocrat%2Bluggage&qid=1774804651&sprefix=aristoc%2Bluggage%2Caps%2C411&sr=8-1-spons&aref=mhoZuROs4C&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
    ]
}


# ----------------------------
# MAIN LOOP
# ----------------------------
all_products = []

for brand, urls in brand_urls.items():
    print(f"\nScraping {brand}...")

    for url in urls:
        product = scrape_product(url)

        if product:
            product["brand"] = brand   # 🔥 IMPORTANT
            all_products.append(product)


# ----------------------------
# SAVE DATA
# ----------------------------
df = pd.DataFrame(all_products)

print("\nFINAL DATA:")
print(df)

df.to_csv("data/luggage_dataset_final_clean.csv", index=False)

print("\nDONE → MULTI-BRAND DATASET CREATED")