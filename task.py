from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver

driver = webdriver.Chrome()
driver.maximize_window()



try:
        # 1. Navigate to the FitPeo Homepage
        driver.get('https://fitpeo.com')

        # 2. Navigate to the Revenue Calculator Page
        wait = WebDriverWait(driver, 10)
        revenue_calculator_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Revenue Calculator')))
        revenue_calculator_link.click()

        # 3. Scroll Down to the Slider Section
        wait = WebDriverWait(driver, 10)
        slider_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiSlider-thumb.MuiSlider-thumbSizeMedium.MuiSlider-thumbColorPrimary.MuiSlider-thumb.MuiSlider-thumbSizeMedium.MuiSlider-thumbColorPrimary.css-sy3s50")))
        actions = ActionChains(driver)
        actions.move_to_element(slider_section).perform()

        # 4. Adjust the Slider
        slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.MuiSlider-root.MuiSlider-colorPrimary.MuiSlider-sizeMedium.css-duk49p')))
        slider_value = slider.get_attribute('value')
        print(f"Initial Slider Value: {slider_value}")
        slider.send_keys(Keys.ARROW_RIGHT * (820 - int(slider_value)))

        # 5. Update the Text Field
        text_field = driver.find_element(By.XPATH, "//input[@id=':r0:']")
        text_field.click()
        text_field.clear()
        text_field.send_keys("560")

        # 6. Validate Slider Value
        updated_slider_value = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".MuiSlider-thumb.MuiSlider-thumbSizeMedium.MuiSlider-thumbColorPrimary.MuiSlider-thumb.MuiSlider-thumbSizeMedium.MuiSlider-thumbColorPrimary.css-sy3s50"))).get_attribute('value')
        assert updated_slider_value == '560', f"Slider value not updated correctly. Current value: {updated_slider_value}"


        # 7. Select CPT Codes
        driver.execute_script("window.scrollBy(0, 500);")
        cpt_99091 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
        cpt_99453 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
        cpt_99454 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[3]")
        cpt_99474 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[8]")
        cpt_99091.click()
        cpt_99453.click()
        cpt_99454.click()
        cpt_99474.click()

        # 8. Validate Total Recurring Reimbursement
        total_reimbursement_header = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 inter css-hocx5c'][normalize-space()='$74115']")))
        total_reimbursement_value = total_reimbursement_header.text
        assert total_reimbursement_value == '$110700', f"Total Reimbursement value is incorrect. Current value: {total_reimbursement_value}"
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
        driver.quit()



