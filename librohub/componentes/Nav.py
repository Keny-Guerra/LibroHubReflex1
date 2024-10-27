from reflex import Component, Box, Button, use_router

class Nav(Component):
    def render(self):
        router = use_router()
        return Box(
            class_name="nav",
            children=[
                Button(text="Inicio", on_click=lambda: router.push("/")),
                Button(text="Admin", on_click=lambda: router.push("/admin"))
            ]
        )
