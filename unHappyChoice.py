from playwright.sync_api import sync_playwright
from pageObjects import User
from pageObjects import frontVisit
from pageObjects import locals
from pageObjects import Action

with sync_playwright() as p:

    description = "UnHappyLogin"

    safari = p.webkit.launch(headless=False, slow_mo=500)

    page = safari.new_page()

    page.goto(locals.login)

    frontVisit.login(page, User.Xmail, User.Pass)

    Action.Print(page, description)

with sync_playwright() as p:

    description = "unHappyRegister"

    safari = p.webkit.launch(headless=False, slow_mo=500)

    page = safari.new_page()

    page.goto(locals.register)

    frontVisit.register(page, User.Xame, User.Xmail, User.Pass)

    Action.Print(page, description)