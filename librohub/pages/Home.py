from reflex import Component, Image, VStack, TextBox

class Home(Component):
    def render(self):
        return VStack(
            class_name="home",
            children=[
                TextBox(value="What recent sold?", class_name="home-title"),
                Gallery(cantidad=7),
                TextBox(value="What do you search?", class_name="home-title"),
                Gallery(cantidad=4),
                VStack(
                    class_name="contenedor",
                    children=[
                        TextBox(value="Lorem Ipsum is simply dummy text of the printing and typesetting industry...")
                    ]
                ),
                VStack(
                    class_name="alianzas-ucsm",
                    children=[TextBox(value="Universidad Católica Santa María")]
                ),
                VStack(
                    class_name="alianzas-pucp",
                    children=[TextBox(value="Pontificia Universidad Católica del Perú")]
                ),
            ],
        )
