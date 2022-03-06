from playwright.sync_api import sync_playwright
from pageObjects import User, Tools, Navigation, Consult

#instanciando um usuario
Usuario = User()

novoUsuario = User("novo@email.com", "", "123123123")

with sync_playwright() as p:

    description = "RealizarLogin"

    safari = p.chromium.launch(headless=False, slow_mo=500)

    page = safari.new_page()

    page.goto(Navigation.urlLogin)

    Navigation.login(page, Usuario.email, Usuario.password)

    Tools.Print(page, description)

with sync_playwright() as p:

    description = "RealizarRegistro"
    
    safari = p.chromium.launch(headless=False, slow_mo=500)

    page = safari.new_page()

    page.goto(Navigation.urlRegister)

    Navigation.register(page, novoUsuario.Name, novoUsuario.email, novoUsuario.password)

    Tools.Print(page, description)

with sync_playwright() as p:

    description = "icmsConsult"

    safari = p.chromium.launch(headless=False, slow_mo=500)

    page = safari.new_page()

    page.goto(Navigation.urlLogin)

    Navigation.login(page, Usuario.email, Usuario.password)

    Consult.option(page, Consult.icms)

    Consult.icmsConsultSimple(page, "3046", "60", "12", "18")

    Tools.Print(page, description)

with sync_playwright() as p:
    
    description = "icmsConsultComplex"

    safari = p.chromium.launch(headless=False, slow_mo=500)

    page = safari.new_page()

    page.goto(Navigation.urlLogin)

    Navigation.login(page, Usuario.email, Usuario.password)

    Consult.option(page, Consult.icms)

    for k in range(Consult.indexComplex):

        price = str(Consult.icmsComplex[k]["price"])

        descount = str(Consult.icmsComplex[k]["descount"])

        shipping = str(Consult.icmsComplex[k]["shipping"])

        mva = str(Consult.icmsComplex[k]["mva"])

        internal = str(Consult.icmsComplex[k]["internal"])

        external = str(Consult.icmsComplex[k]["external"])

        desc = str(Consult.icmsComplex[k]["description"])

        ipi = str(Consult.icmsComplex[k]["ipi"])

        Consult.icmsConsultComplex(page, price, descount, shipping, mva, internal, external, ipi)

        Tools.Print(page, desc)

with sync_playwright() as p:
    
    safari = p.chromium.launch(headless=False, slow_mo=500)

    page = safari.new_page()

    page.goto(Navigation.urlLogin)

    Navigation.login(page, Usuario.email, Usuario.password)

    Consult.option(page, Consult.icms)

    for k in range(Consult.indexSimple):

        price = str(Consult.icmsSimple[k]["price"])

        mva = str(Consult.icmsSimple[k]["mva"])

        internal = str(Consult.icmsSimple[k]["internal"])

        external = str(Consult.icmsSimple[k]["external"])

        desc = str(Consult.icmsSimple[k]["description"])

        Consult.icmsConsultSimple(page, price, mva, internal, external)

        Tools.Print(page, desc)

with sync_playwright() as p:

    description = "issConsult"

    safari = p.chromium.launch(headless=False, slow_mo=500)

    page = safari.new_page()

    page.goto(Navigation.urlLogin)

    Navigation.login(page, Usuario.email, Usuario.password)

    Consult.option(page, Consult.iss)

    Consult.issConcult(page, "2000", "5")

    Tools.Print(page, description)