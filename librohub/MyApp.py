from reflex import App, Router, Route
from reflex.components import Box
from components.nav import Nav
from components.footer import Footer
from pages.admin import Admin
from pages.home import Home

class MyApp(App):
    def render(self):
        return Box(
            class_name="App",
            children=[
                Nav(),
                Router(
                    children=[
                        Route(path='/', component=Home),
                        Route(path='/admin', component=Admin),
                    ]
                ),
                Footer()
            ]
        )

if __name__ == "__main__":
    MyApp().run()
