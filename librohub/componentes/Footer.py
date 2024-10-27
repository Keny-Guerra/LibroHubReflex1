from reflex import Component, Box, Text

class Footer(Component):
    def render(self):
        return Box(
            class_name="footer",
            children=[
                Text(value="LibroHub"),
                Text(
                    value="Copyright © 2024 LibroHub, Todos los derechos reservados.",
                    class_name="transparente"
                ),
            ]
        )
