import requests
from bs4 import BeautifulSoup
from helpers.selectors import OVERVIEW_QUEUE_BUTTON, OVERVIEW_STATS, OVERVIEW_TABLE
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def topchampions_command(sum_name, queue, num):
    topChampions = []
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(
        "D:\chromedriver_win32 (3)\chromedriver.exe", chrome_options=options
    )
    driver.get(f"https://na.op.gg/summoner/userName={sum_name}")

    driver.find_element(By.CSS_SELECTOR, OVERVIEW_QUEUE_BUTTON[queue]).click()

    table = driver.find_element_by_css_selector(OVERVIEW_TABLE[queue])
    rows = table.find_elements(By.CLASS_NAME, "ChampionBox")

    index = 1
    for r in rows:
        topChampions.append(
            {
                index: r.find_element(
                    By.CSS_SELECTOR, OVERVIEW_STATS["name"]
                ).text.strip(),
                "winrate": r.find_element(
                    By.CSS_SELECTOR, OVERVIEW_STATS["winrate"]
                ).text.strip(),
                "played": r.find_element(
                    By.CSS_SELECTOR, OVERVIEW_STATS["played"]
                ).text.strip(),
            }
        )
        index += 1

    driver.quit()
    return format(topChampions, num)


def format(topChampions, num):
    retval = ""
    for x in range(0, int(num)):
        retval += f"{x+1}. {topChampions[x][x+1]} winrate {topChampions[x]['winrate']} played {topChampions[x]['winrate']}\n"
    return retval
