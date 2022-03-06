from env import email, password, xmail, name, xame

class User:

    #construtor
    def __init__(self, Email= email, Xmail= xmail, Pass= password, Name= name, Xname= xame):
        self.email = Email
        self.xmail = Xmail
        self.password = Pass
        self.Name = Name
        self.Xname = Xname
    


class Navigation:

    urlLogin = "http://localhost/phpCrud/login.php"

    urlRegister = "http://localhost/phpCrud/register.php"

    def login(page, email, password):
        
        page.fill("#email", email)

        page.fill("#password", password)

        page.click("#login")
    
    def register(page, name, email, password):
    
        page.fill("#name", name)

        page.fill("#email", email)

        page.fill("#pass", password)

        page.click("#login")

class Tools:

    def Print(page, description):

        page.screenshot(path = "{}.png".format(description))
    
class Consult:

    icms = "icms"

    irrf = "IRRF"

    iss = "iss"

    icmsSimple = [
    {
        "price" : "3046",
        "mva" : "60",
        "internal" : "18",
        "external" : "20",
        "description" : "icmsSimples"
    },
    {
        "price" : "500",
        "mva" : "60",
        "internal" : "18",
        "external" : "12",
        "description" : "icmsSimples2"
    }
    ]   

    icmsComplex = [
    {
        "price" : "3046",
        "descount" : "200",
        "shipping" : "20",
        "mva" : "60",
        "internal" : "18",
        "external" : "20",
        "ipi" : "5",
        "description" : "icmsComplex"
    },
    {
        "price" : "500",
        "descount" : "200",
        "shipping" : "20",
        "mva" : "60",
        "internal" : "18",
        "external" : "12",
        "ipi" : "10",
        "description" : "icmsComplex2"
    }
    ]     

    indexSimple = len(icmsSimple)

    indexComplex = len(icmsComplex)

    def option(page, tax):

        page.select_option('select#options', tax)

        page.click("#displayText")
    
    def icmsConsultSimple(page, price, mva, internal, external):

        page.click("#options")

        page.fill("#price", price)

        page.fill("#MVA", mva)

        page.fill("#internal", internal)

        page.fill("#external", external)

        page.click("#icmsSubmit")
    
    def icmsConsultComplex(page, price, descount, shipping, mva, internal, external, ipi):

        page.click("#options")

        page.fill("#price", price)

        page.fill("#discount", descount)

        page.fill("#shipping", shipping)

        page.fill("#MVA", mva)

        page.fill("#internal", internal)

        page.fill("#external", external)

        page.fill("#IPI", ipi)

        page.click("#icmsSubmit")
    
    def issConcult(page, salary, percentage):

        page.click("#options")

        page.fill("#issPrice", salary)

        page.fill("#pratAliqt", percentage)

        page.click("#issSubmit")



