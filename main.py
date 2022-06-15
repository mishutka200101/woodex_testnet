from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pyuseragents import random as fake_useragent
import secrets
import string
import time


def random_nickname_generator():
    alphabet = string.ascii_letters
    nickname = ''.join(secrets.choice(alphabet) for i in range(8))
    return nickname


def main():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={fake_useragent()}")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument('--disable-gpu')
    options.add_argument('--disable-infobars')
    options.add_argument("--mute-audio")
    options.add_argument('--profile-directory=Default')
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(
        executable_path="chromedriver/chromedriver",
        options=options
    )

    near_wallet_url = 'https://wallet.testnet.near.org/create'
    testnet_url = 'https://testnet-dex.woo.org/en/trade'
    wait = WebDriverWait(driver, 20)

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
        a = int(slovo.split(' ')[1].split('#')[-1])
        driver.find_element(by=By.XPATH, value='//*[@id="app-container"]/div[3]/form/div/input').send_keys(mnemonic_dict[a-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/form/div/button[1]'))).click()
        wait.until(EC.url_to_be(url='https://wallet.testnet.near.org/'))
        driver.switch_to.new_window('tab')
        driver.get(url=testnet_url)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/header/div/div[3]/div'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[2]/div[5]/button/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/div/div[4]/button[2]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/div/div[7]/button[2]'))).click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(30)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[2]/div[5]/button/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/header/div/button/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/div[2]/button[2]'))).click()
        wait.until(EC.url_contains(url='https://testnet-dex.woo.org/en/account/wallet?deposit=near&transactionHashes='))
        time.sleep(20)
        driver.get(url=testnet_url)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[5]/div/button[1]/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/button'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[3]/button/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/div[2]/button[2]'))).click()
        wait.until(EC.url_contains(url='https://testnet-dex.woo.org/en/account/wallet?deposit=near&transactionHashes='))
        driver.get('https://testnet-dex.woo.org/en/account/wallet?deposit=near')
        time.sleep(20)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td[5]/div/button[1]/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/input')))
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/input').send_keys(150)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[3]/button/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[3]/div[2]/button[2]'))).click()
        wait.until(EC.url_contains(url='https://testnet-dex.woo.org/en/account/wallet?deposit=near&transactionHashes='))
        driver.get('https://testnet-dex.woo.org/en/account/wallet?deposit=near')
        # wait.until(EC.url_contains(url='https://testnet-dex.woo.org/en/account/wallet?deposit=near&transactionHashes='))
        # driver.get(url=testnet_url)

        time.sleep(500)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
