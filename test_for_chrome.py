
import time
from chaild import *
from selenium import webdriver

#Scenario 1 start
while True:
    number_of_child = int(input('Введите количество детей больше 1 - '))
    if number_of_child <= 1:
        continue
    else:
        break


driver = webdriver.Chrome()

# 1. go to home page
driver.get("https://booking.com")
time.sleep(1)

# 2. open menu for selecting strangers number
submit_button = driver.find_element_by_css_selector("[data-visible='accommodation,flights']")
submit_button.click()

# 3. specify N number of children (N > 1)
submit_child_quantity = driver.find_element_by_css_selector("button[aria-label='Детей: увеличить количество']")
for i in range(number_of_child):
    submit_child_quantity.click()
    time.sleep(1)

# Expect: the number of age inputs is equal to N
for i in range(number_of_child):
    show_age = generator_age_button(i)
    submit_open_age = driver.find_element_by_css_selector(f'{show_age}')
    submit_open_age.click()
    time.sleep(1)
    show_age = generator_age_button(i)
    chose_age = generator_age(number_of_child)
    submit_select_age = driver.find_element_by_css_selector(f'{show_age}{chose_age}')
    submit_select_age.click()
    if i == number_of_child-1:
        show_age = generator_age_button(i)
        submit_open_age = driver.find_element_by_css_selector(f'{show_age}')
        submit_open_age.click()
time.sleep(2)
# Scenario 1 end

# Scenario 2 start

# 1. choose any city from the menu below
submit_select_city = driver.find_element_by_css_selector("div.promotion-postcards__row.js-ds-layout-events-postcards.u-clearfix div.promotion-postcard__large:nth-child(1)")
submit_select_city.click()
time.sleep(2)

# 2. Click "show prices" button for any hotel
submit_show_prices = driver.find_element_by_css_selector("#hotellist_inner > div:nth-child(4) .sr_property_block_main_row .sr-cta-button-row.sr-cta-button-top-spacing > a")
submit_show_prices.click()
time.sleep(2)

# 3. Set any dates for check in
submit_set_date_in = driver.find_element_by_css_selector(".c2-months-table .c2-month:nth-child(1) tbody > tr:nth-child(3) > td:nth-child(1)")
submit_set_date_in.click()
time.sleep(2)

# 3. open dates for check out
submit_open_date = driver.find_element_by_css_selector("[data-placeholder='Дата отъезда']")
submit_open_date.click()
time.sleep(2)
# 3. Set any dates for check out
submit_set_date_out = driver.find_element_by_css_selector(".c2-wrapper.c2-wrapper-s-position-undefined.c2-wrapper-s-checkout.c2-wrapper-s-has-arrow.c2-wrapper-s-range-highlighted > div:nth-child(2) .c2-month:nth-child(2) tbody > tr:nth-child(3) > td:nth-child(1)")
submit_set_date_out.click()
time.sleep(2)

# 4. Submit search form
submit_search = driver.find_element_by_css_selector("button[data-sb-id='main']")
submit_search.click()
# Scenario 2 end
time.sleep(4)
driver.quit()
