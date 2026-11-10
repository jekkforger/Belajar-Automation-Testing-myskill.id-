from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False, slow_mo = 2000)
    page = browser.new_page()
    print("mengunjungin halaman MySkill")
    page.goto("https://www.myskill.id/")

    # form register
    page.locator('a[href="/auth/register"]').click()
    page.locator('input[name="email"]').fill("mudzaqimaulana@gmail.com")
    page.locator('input[name="password"]').fill("07Mei2004*")
    page.get_by_label("Tampilkan password").click()
    page.locator('input[name="passwordConfirmation"]').fill("07Mei2004*")
    page.get_by_label("Tampilkan konfirmasi password").click()
    page.locator('button[type="submit"]').click()