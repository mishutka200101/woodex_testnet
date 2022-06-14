from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
import secrets
import string
import time


def random_nickname_generator():
    alphabet = string.ascii_letters
    nickname = ''.join(secrets.choice(alphabet) for i in range(8))
    return nickname


def main():
    user_agent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent.random}")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-infobars')
    options.add_argument("--mute-audio")
    options.add_argument('--profile-directory=Default')
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(
        executable_path="chromedriver/chromedriver.exe",
        options=options
    )

    near_wallet_url = 'https://wallet.testnet.near.org/create'
    testnet_url = ''
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(url=near_wallet_url)
        nickname = random_nickname_generator()
        driver.find_element(by=By.XPATH, value='//*[@id="app-container"]/div[3]/form/div[1]/input').send_keys(nickname)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/form/button'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/form/button'))).click()
        time.sleep(2)
        mnemonic1 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[1]/span').text
        mnemonic2 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[2]/span').text
        mnemonic3 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[3]/span').text
        mnemonic4 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[4]/span').text
        mnemonic5 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[5]/span').text
        mnemonic6 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[6]/span').text
        mnemonic7 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[7]/span').text
        mnemonic8 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[8]/span').text
        mnemonic9 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[9]/span').text
        mnemonic10 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[10]/span').text
        mnemonic11 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[11]/span').text
        mnemonic12 = driver.find_element(by=By.XPATH, value='//*[@id="seed-phrase"]/span[12]/span').text
        mnemonic = mnemonic1 + ' ' + mnemonic2 + ' ' + mnemonic3 + ' ' + mnemonic4 + ' ' + mnemonic5 + ' ' + mnemonic6 + \
                   ' ' + mnemonic7 + ' ' + mnemonic8 + ' ' + mnemonic9 + ' ' + mnemonic10 + ' ' + mnemonic11 + ' ' \
                   + mnemonic12
        with open('accounts.txt', 'a') as file:
            file.write(f"Account: {nickname + '.testnet'}, mnemonic: {mnemonic};\n")
        mnemonic_dict = mnemonic.split(' ')
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/div/button[1]'))).click()
        slovo = driver.find_element(by=By.XPATH, value='//*[@id="app-container"]/div[3]/form/div/h4').text
        a = int(slovo.split(' ')[1].slpit('#')[-1])
        driver.find_element(by=By.XPATH, value='//*[@id="app-container"]/div[3]/form/div/input').send_keys(mnemonic_dict[a-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/form/div/button[1]'))).click()
        time.sleep(50)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
