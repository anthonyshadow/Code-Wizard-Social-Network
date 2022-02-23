import web

urls = (
    '/', 'Home',
    '/register', 'Register',
)

render =web.template.render("Views/Templates", base="mainLayout")
app = web.application(urls, globals())

# Classes/Routes

class Home:
    def GET(self):
        return render.Home()

class Register:
    def GET(self):
        return render.Register()

if __name__ == "__main__":
    app.run()