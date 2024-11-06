import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_valid():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    
    # Kiểm tra kết quả
    assert "http://localhost/opencart/index.php?route=account/login&language=vi-vn" in driver.current_url
    # Đóng trình duyệt
    driver.quit()

def test_login_invalid_without_up():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("")
    time.sleep(3)
    
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(2)
    
    assert "http://localhost/opencart/index.php?route=account/login&language=vi-vn" in driver.current_url
    
    # Đóng trình duyệt
    driver.quit()
    
def test_login_invalid_without_u():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(2)
    
    assert "http://localhost/opencart/index.php?route=account/login&language=vi-vn" in driver.current_url
    
    # Đóng trình duyệt
    driver.quit()
    
def test_login_invalid_without_p():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("")
    time.sleep(3)
    
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(2)
    
    assert "http://localhost/opencart/index.php?route=account/login&language=vi-vn" in driver.current_url
    
    # Đóng trình duyệt
    driver.quit()
    
def test_register_valid():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-firstname").send_keys("nguyen")
    driver.find_element(By.ID, "input-lastname").send_keys("tri")
    driver.find_element(By.ID, "input-email").send_keys("b193@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/form/div/div/input").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/form/div/button").click()
    time.sleep(30)
    
    content = driver.find_element(By.CSS_SELECTOR,"#content > h1").text
    assert "Your Account Has Been Created!" == content 
    
    # Đóng trình duyệt
    driver.quit()
    
def test_register_invalid():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-firstname").send_keys("nguyen")
    driver.find_element(By.ID, "input-lastname").send_keys("tri")
    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/form/div/div/input").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/form/div/button").click()
    time.sleep(20)
    
    assert "http://localhost/opencart/index.php?route=account/register&language=vi-vn" in driver.current_url
    # Đóng trình duyệt
    driver.quit()
    
def test_logout():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(15)
    
    # Kiểm tra kết quả
    assert "http://localhost/opencart/index.php?route=account/logout&language=vi-vn" in driver.current_url
    # Đóng trình duyệt
    driver.quit()
    
def test_navigator():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"#narbar-menu > ul > li:nth-child(1) > a").click()
    time.sleep(10)
    
    driver.find_element(By.CSS_SELECTOR,"#narbar-menu > ul > li:nth-child(1) > div > a").click()
    time.sleep(10)
    
    assert "http://localhost/opencart/index.php?route=product/category&language=vi-vn&path=20" in driver.current_url
    
def test_navigator_cart():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)  
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"#top > div > div.nav.float-end > ul > li:nth-child(4) > a > span").click()
    time.sleep(10)
    
    
    assert "http://localhost/opencart/index.php?route=checkout/cart&language=vi-vn" in driver.current_url
    
def test_navigator_wish_list():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)  
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"#wishlist-total > span").click()
    time.sleep(10)
    
    content = driver.find_element(By.CSS_SELECTOR,"#content > h1").text
    time.sleep(10)
    
    assert "My Wishlist" == content

def test_navigator_contact_us():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)  
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"body > footer > div > div > div:nth-child(2) > ul > li:nth-child(1) > a").click()
    time.sleep(10)
    
    content = driver.find_element(By.CSS_SELECTOR,"#content > h1").text
    time.sleep(10)
    
    assert "Contact Us" == content

def test_navigator_gift_certificate():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)  
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"body > footer > div > div > div:nth-child(3) > ul > li:nth-child(2) > a").click()
    time.sleep(10)
    
    content = driver.find_element(By.CSS_SELECTOR,"#content > h1").text
    time.sleep(10)
    
    assert "Purchase a Gift Certificate" == content 
    
def test_search_available_product():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"#search > input").send_keys("mac")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#search > button").click()
    time.sleep(3)
    
    content = driver.find_element(By.CSS_SELECTOR,"#content > h1").text
    assert "Search - mac" == content

def test_search_unavailable_product():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"#search > input").send_keys("aaa")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#search > button").click()
    time.sleep(3)
    
    content = driver.find_element(By.CSS_SELECTOR,"#content > p").text
    assert "There is no product that matches the search criteria." == content

def test_search_blank_product():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"#search > input").send_keys("")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#search > button").click()
    time.sleep(3)
    
    # content = driver.find_element(By.CSS_SELECTOR,"#content > p").text
    assert "http://localhost/opencart/index.php?route=product/search&language=vi-vn" in driver.current_url

def test_search_under_50s():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    
    driver.find_element(By.CSS_SELECTOR,"#search > input").send_keys("iphone")
    time.sleep(3)
    start_time = time.time()
    driver.find_element(By.CSS_SELECTOR,"#search > button").click()
    
    end_time = time.time()
    search_duration = end_time - start_time
    # content = driver.find_element(By.CSS_SELECTOR,"#content > p").text
    assert search_duration < 50

def test_search_SQL_injection():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    
    # Truy cập vào My Account và đăng nhập
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
    time.sleep(15)
    
    # Nhập từ khóa SQL Injection vào ô tìm kiếm
    search_box = driver.find_element(By.CSS_SELECTOR, "#search > input")
    search_box.clear()
    search_box.send_keys("' OR '1'='1")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#search > button").click()
    time.sleep(3)
    
    # Lấy nội dung kết quả tìm kiếm
    content = driver.find_element(By.CSS_SELECTOR, "#content > h1").text
    
    # Kiểm tra tiêu đề kết quả tìm kiếm
    assert content == "Search - ' OR '1'='1", f"Expected search title not found. Got: {content}"
    
    # Kiểm tra không có lỗi SQL Injection trong trang kết quả
    page_source = driver.page_source
    assert "SQL syntax" not in page_source, "Phát hiện lỗi cú pháp SQL trong kết quả!"
    assert "database error" not in page_source, "Phát hiện lỗi cơ sở dữ liệu trong kết quả!"
    assert "warning" not in page_source.lower(), "Cảnh báo liên quan đến SQL Injection trong kết quả!"
    
    # In kết quả để xác nhận kiểm tra thành công
    print("Không phát hiện lỗ hổng SQL Injection với từ khóa kiểm tra.")

    # Đóng trình duyệt
    driver.quit()

def test_dashboard_admin_total_order():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/admin/")
    
    
    driver.find_element(By.CSS_SELECTOR, "#input-username").send_keys("admin")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#form-login > div.text-end > button").click()
    time.sleep(25)
    
    driver.find_element(By.CSS_SELECTOR,"#modal-security > div > div > div.modal-header > button").click()
    time.sleep(3)
    
    # view more total order
    total_order = driver.find_element(By.CSS_SELECTOR,"#content > div.container-fluid > div:nth-child(1) > div:nth-child(1) > div > div.tile-body > h2").text
    
    driver.find_element(By.CSS_SELECTOR,"#content > div.container-fluid > div:nth-child(1) > div:nth-child(1) > div > div.tile-footer > a").click()
    time.sleep(3)
    
    id_lastest = driver.find_element(By.CSS_SELECTOR,"#form-order > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(2)").text
    assert total_order == id_lastest

def test_dashboard_admin_total_sales():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/admin/")
    
    # Đăng nhập vào trang admin
    driver.find_element(By.CSS_SELECTOR, "#input-username").send_keys("admin")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#form-login > div.text-end > button").click()
    time.sleep(25)
    
    # Đóng cảnh báo bảo mật nếu có
    driver.find_element(By.CSS_SELECTOR, "#modal-security > div > div > div.modal-header > button").click()
    time.sleep(3)
    
    # Lấy tổng doanh số từ Dashboard
    total_sales_dashboard = driver.find_element(By.CSS_SELECTOR, "#content > div.container-fluid > div:nth-child(1) > div:nth-child(2) > div > div.tile-body > h2").text
    total_sales_dashboard = float(total_sales_dashboard.replace(",", "").replace("$", ""))  # Chuyển đổi sang số thực
    # Chuyển đến trang quản lý đơn hàng
    driver.find_element(By.CSS_SELECTOR, "#content > div.container-fluid > div:nth-child(1) > div:nth-child(1) > div > div.tile-footer > a").click()
    time.sleep(10)  # Tăng thời gian chờ để đảm bảo bảng đơn hàng được tải đầy đủ
    
    # Lấy tất cả các phần tử chứa giá trị đơn hàng trong cột giá trị
    order_elements = driver.find_elements(By.CSS_SELECTOR, "#form-order > div.table-responsive > table > tbody > tr > td.text-end.d-none.d-lg-table-cell")
    
    # Duyệt qua các phần tử và trích xuất giá trị đơn hàng
    order_values = []
    for order in order_elements:
        try:
            # Chuyển đổi giá trị thành số thực, bỏ qua nếu không phải là số
            order_value = float(order.text.replace(",", "").replace("$", ""))
            order_values.append(order_value)
        except ValueError:
            # Bỏ qua các giá trị không thể chuyển thành số (như 'Pending')
            continue
    
    # Kiểm tra danh sách giá trị đơn hàng để xem các giá trị được thu thập
    print("Order Values:", order_values)
    
    # Tính tổng của tất cả các đơn hàng
    total_order_value = sum(order_values)
    
    # So sánh tổng doanh số từ Dashboard với tổng tính được
    assert total_sales_dashboard == total_order_value, f"Total Sales from Dashboard ({total_sales_dashboard}) does not match calculated total sales ({total_order_value})."
    
    # In kết quả để kiểm tra
    print("Total Sales from Dashboard:", total_sales_dashboard)
    print("Calculated Total Sales:", total_order_value)
    
    # Đóng trình duyệt
    driver.quit()

def test_dashboard_admin_total_customers():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/admin/")
    
    # Đăng nhập vào trang admin
    driver.find_element(By.CSS_SELECTOR, "#input-username").send_keys("admin")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#form-login > div.text-end > button").click()
    time.sleep(25)
    
    # Đóng cảnh báo bảo mật nếu có
    driver.find_element(By.CSS_SELECTOR, "#modal-security > div > div > div.modal-header > button").click()
    time.sleep(3)
    
    # Lấy tổng số khách hàng từ Dashboard
    total_customers_dashboard = driver.find_element(By.CSS_SELECTOR, "#content > div.container-fluid > div:nth-child(1) > div:nth-child(3) > div > div.tile-body > h2").text
    total_customers_dashboard = int(total_customers_dashboard.replace(",", ""))  # Chuyển đổi sang số nguyên để đếm
    
    # Chuyển đến trang quản lý khách hàng
    driver.find_element(By.CSS_SELECTOR, "#content > div.container-fluid > div:nth-child(1) > div:nth-child(3) > div > div.tile-footer > a").click()
    time.sleep(10)  # Tăng thời gian chờ để đảm bảo bảng khách hàng được tải đầy đủ
    
    # Đếm số hàng trong bảng khách hàng
    customer_rows = driver.find_elements(By.CSS_SELECTOR, "#form-customer > div.table-responsive > table > tbody > tr")
    total_customers_counted = len(customer_rows)    
    
    # So sánh tổng khách hàng từ Dashboard với tổng số hàng đếm được
    assert total_customers_dashboard == total_customers_counted, f"Total Customers from Dashboard ({total_customers_dashboard}) does not match counted customers ({total_customers_counted})."
    
    # Đóng trình duyệt
    driver.quit()

def test_add_to_cart_one_product():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR,"#logo > a > img").click()
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > form > div > button:nth-child(1)").click()
    time.sleep(3)
    
    
    text = driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > h4 > a").text
    time.sleep(3)
    
    
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > button").click()
    time.sleep(3)
    
    text_in_cart = driver.find_element(By.CSS_SELECTOR,"#header-cart > div > ul > li > table > tbody > tr > td.text-start > a").text
    time.sleep(3)

    assert text == text_in_cart

def test_add_to_cart_one_product_quantity_more():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(30)
    
    # nhấn logo cho quay về trang chính
    driver.find_element(By.CSS_SELECTOR,"#logo > a > img").click()
    time.sleep(10)
    
    # nhấn vào tên sản phẩm
    driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > h4 > a").click()
    time.sleep(30)
    
    
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").clear()
    time.sleep(3)
    input = driver.find_element(By.CSS_SELECTOR,"#input-quantity").send_keys("5")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#button-cart").click()
    time.sleep(15)
    
    driver.find_element(By.CSS_SELECTOR,"#alert > div > button").click()
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > button").click()
    time.sleep(3)
    
    # viewcart
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > ul > li > div > p > a:nth-child(1) > strong").click()
    time.sleep(3)
    
    quantity = driver.find_element(By.CSS_SELECTOR,"#shopping-cart > div > table > tbody > tr > td:nth-child(4) > form > div > input.form-control").get_attribute("value")
    text = driver.find_element(By.CSS_SELECTOR,"#shopping-cart > div > table > tbody > tr > td.text-start.text-wrap > a").text
    assert "MacBook" == text
    assert '5' == quantity
    
def test_add_to_cart_product_quantity_zero():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(30)
    
    # nhấn logo cho quay về trang chính
    driver.find_element(By.CSS_SELECTOR,"#logo > a > img").click()
    time.sleep(10)
    
    # nhấn vào tên sản phẩm
    driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > h4 > a").click()
    time.sleep(30)
    
    
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").clear()
    time.sleep(3)
    input = driver.find_element(By.CSS_SELECTOR,"#input-quantity").send_keys("0")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#button-cart").click()
    time.sleep(15)
    
    
    driver.find_element(By.CSS_SELECTOR,"#alert > div > button").click()
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > button").click()
    time.sleep(3)
    
    content = driver.find_element(By.CSS_SELECTOR,"#header-cart > div > ul > li").text
    time.sleep(3)
    
    assert "Your shopping cart is empty!" == content

def test_add_to_cart_products():
    # Khởi tạo trình duyệt
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    
    try:
        # Đăng nhập vào tài khoản
        driver.find_element(By.LINK_TEXT, "My Account").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)

        # Nhập thông tin tài khoản và đăng nhập
        driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
        driver.find_element(By.ID, "input-password").send_keys("123456")
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)

        # Quay về trang chính
        driver.find_element(By.CSS_SELECTOR, "#logo > a").click()
        time.sleep(2)

        # Danh sách tên sản phẩm muốn thêm vào giỏ hàng
        product_names = ["MacBook", "iPhone"]

        for product_name in product_names:
            # Tìm sản phẩm bằng tên
            try:
                product = driver.find_element(By.LINK_TEXT, product_name)
                product.click()
                time.sleep(2)

                # Thêm sản phẩm vào giỏ hàng với số lượng nhất định
                driver.find_element(By.CSS_SELECTOR, "#input-quantity").clear()
                driver.find_element(By.CSS_SELECTOR, "#input-quantity").send_keys("3")
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, "#button-cart").click()
                time.sleep(3)
                print(f"Đã thêm sản phẩm {product_name} vào giỏ hàng.")
            except Exception as e:
                print(f"Lỗi khi thêm sản phẩm {product_name} vào giỏ hàng: {str(e)}")

            # Quay lại trang chính để chọn sản phẩm tiếp theo
            driver.find_element(By.CSS_SELECTOR, "#logo > a").click()
            time.sleep(2)

        # Mở giỏ hàng
        driver.find_element(By.CSS_SELECTOR, "#header-cart > div > button").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "View Cart").click()
        time.sleep(5)  # Tăng thời gian chờ

        # Kiểm tra sự hiện diện của các sản phẩm trong giỏ hàng
        cart_items = driver.find_elements(By.CSS_SELECTOR, "#shopping-cart > div > table > tbody > tr > td.text-start.text-wrap > a")
        cart_product_names = [item.text for item in cart_items]
        print("Các sản phẩm trong giỏ hàng:", cart_product_names)

        for expected_name in product_names:
            assert expected_name in cart_product_names, f"Lỗi: Sản phẩm {expected_name} không có trong giỏ hàng."

        print("Tất cả sản phẩm đã được thêm vào giỏ hàng thành công.")
    
    finally:
        driver.quit()

def test_add_to_cart_one_product():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR,"#logo > a > img").click()
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > form > div > button:nth-child(1)").click()
    time.sleep(3)
    
    
    text = driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > h4 > a").text
    time.sleep(3)
    
    
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > button").click()
    time.sleep(3)
    
    text_in_cart = driver.find_element(By.CSS_SELECTOR,"#header-cart > div > ul > li > table > tbody > tr > td.text-start > a").text
    time.sleep(3)

    assert text == text_in_cart

def test_add_to_cart_one_product_quantity_invalid():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(30)
    
    # nhấn logo cho quay về trang chính
    driver.find_element(By.CSS_SELECTOR,"#logo > a > img").click()
    time.sleep(10)
    
    # nhấn vào tên sản phẩm
    driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > h4 > a").click()
    time.sleep(30)
    
    
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").clear()
    time.sleep(3)
    input = driver.find_element(By.CSS_SELECTOR,"#input-quantity").send_keys("aaa")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#button-cart").click()
    time.sleep(15)
    
    
    driver.find_element(By.CSS_SELECTOR,"#alert > div > button").click()
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > button").click()
    time.sleep(3)
    
    content = driver.find_element(By.CSS_SELECTOR,"#header-cart > div > ul > li").text
    time.sleep(3)
    
    assert "Your shopping cart is empty!" == content

def test_add_to_cart_one_product_update_quantity():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(30)
    
    # nhấn logo cho quay về trang chính
    driver.find_element(By.CSS_SELECTOR,"#logo > a > img").click()
    time.sleep(10)
    
    # nhấn vào tên sản phẩm
    driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > h4 > a").click()
    time.sleep(30)
    
    
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").clear()
    time.sleep(3)
    input = driver.find_element(By.CSS_SELECTOR,"#input-quantity").send_keys("3")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#button-cart").click()
    time.sleep(15)
    
    
    driver.find_element(By.CSS_SELECTOR,"#alert > div > button").click()
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > button").click()
    time.sleep(3)
    
   #view cart 
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > ul > li > div > p > a:nth-child(1) > strong").click()
    time.sleep(3)
    
    # update quantity
    driver.find_element(By.CSS_SELECTOR,"#shopping-cart > div > table > tbody > tr > td:nth-child(4) > form > div > input.form-control").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#shopping-cart > div > table > tbody > tr > td:nth-child(4) > form > div > input.form-control").clear()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#shopping-cart > div > table > tbody > tr > td:nth-child(4) > form > div > input.form-control").send_keys("5")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#shopping-cart > div > table > tbody > tr > td:nth-child(4) > form > div > button.btn.btn-primary").click()
    time.sleep(3)
    quantity = driver.find_element(By.CSS_SELECTOR,"#shopping-cart > div > table > tbody > tr > td:nth-child(4) > form > div > input.form-control").get_attribute('value')
    time.sleep(3)
    assert "5" == quantity

def test_checkout_without_payment_method():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")

    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.ID, "input-email").send_keys("minhtringuyen061103@gmail.com")
    time.sleep(3)
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(30)

    # Nhấn logo để quay về trang chính
    driver.find_element(By.CSS_SELECTOR, "#logo > a > img").click()
    time.sleep(10)

    # Nhấn vào tên sản phẩm
    driver.find_element(By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > h4 > a").click()
    time.sleep(30)

    # Thêm sản phẩm vào giỏ
    driver.find_element(By.CSS_SELECTOR, "#input-quantity").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#input-quantity").clear()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#input-quantity").send_keys("5")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#button-cart").click()
    time.sleep(15)

    driver.find_element(By.CSS_SELECTOR, "#alert > div > button").click()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, "#header-cart > div > button").click()
    time.sleep(3)

    # Checkout
    driver.find_element(By.CSS_SELECTOR, "#header-cart > div > ul > li > div > p > a:nth-child(2) > strong").click()
    time.sleep(20)

    # Chọn phương thức thanh toán
    driver.find_element(By.CSS_SELECTOR, "#button-payment-methods").click()
    time.sleep(20)

    # Lấy thông báo lỗi
    content = driver.find_element(By.CSS_SELECTOR, "#error-payment-method").text
    print("Thông báo lỗi:", content)  # In ra thông báo lỗi để kiểm tra

    # Kiểm tra thông báo lỗi chính xác
    assert "Customer required!" == content, f"Thông báo lỗi không đúng. Đã nhận được: {content}"

def test_checkout():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    driver.find_element(By.CSS_SELECTOR, "#logo > a > img").click()
    time.sleep(10)

    driver.find_element(By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > h4 > a").click()
    time.sleep(30)
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#input-quantity").clear()
    time.sleep(3)
    input = driver.find_element(By.CSS_SELECTOR,"#input-quantity").send_keys("3")
    time.sleep(3)
    # button add to cart
    driver.find_element(By.CSS_SELECTOR,"#button-cart").click()
    time.sleep(15)
    
    # delete notice
    driver.find_element(By.CSS_SELECTOR,"#alert > div > button").click()
    time.sleep(3)
    #item cart
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > button").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#header-cart > div > ul > li > div > p > a:nth-child(2) > strong").click()
    time.sleep(3)
    
    # input information
    
    driver.find_element(By.CSS_SELECTOR,"#input-guest").click()
    driver.find_element(By.CSS_SELECTOR,"#input-firstname").send_keys("nguyen")
    driver.find_element(By.CSS_SELECTOR,"#input-lastname").send_keys("tri")
    driver.find_element(By.CSS_SELECTOR,"#input-email").send_keys("minhtringuyen061103@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"#input-shipping-address-1").send_keys("888/67/5c Lạc Long Quân")
    driver.find_element(By.CSS_SELECTOR,"#input-shipping-city").send_keys("Quận Tân Bình")
    driver.find_element(By.CSS_SELECTOR,"#input-shipping-country").send_keys("VietNam")
    driver.find_element(By.CSS_SELECTOR,"#input-shipping-zone").send_keys("Ho Chi Minh City")
    driver.find_element(By.CSS_SELECTOR,"#input-password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR,"#input-register-agree").click()
    driver.find_element(By.CSS_SELECTOR,"#input-newsletter").click()
    driver.find_element(By.CSS_SELECTOR,"#button-register").click()
    

    
    
    
    
    
    
    
    
    
    
    



