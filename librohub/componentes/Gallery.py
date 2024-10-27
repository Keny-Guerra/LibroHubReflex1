from reflex import Component, Box, Image, Text, Button, VStack, use_state
import json

# Cargar datos desde el archivo JSON
with open('pages/data.json', 'r') as f:
    data = json.load(f)

class Gallery(Component):
    cantidad: int

    def render(self):
        selected_book, set_selected_book = use_state(None)

        libros = data['libros'][:self.cantidad]

        if selected_book:
            return VStack(
                class_name="book-details",
                children=[
                    Text(value=selected_book['nombre'], class_name="book-title"),
                    Text(value=f"Autor: {selected_book['autor']}"),
                    Text(value=f"Precio: S/.{selected_book['precio']:.2f}"),
                    Text(value=f"Cantidad: {selected_book['cantidad']}"),
                    Image(src=selected_book['imagen'], width="200px"),
                    Button(
                        text="Volver",
                        on_click=lambda: set_selected_book(None)
                    )
                ]
            )
        else:
            return Box(
                class_name="gallery",
                children=[
                    Box(
                        class_name="image-grid",
                        children=[
                            Box(
                                key=index,
                                class_name="image-container",
                                children=[
                                    Image(
                                        src=libro['imagen'],
                                        alt=libro['nombre'],
                                        on_click=lambda l=libro: set_selected_book(l)
                                    )
                                ]
                            ) for index, libro in enumerate(libros)
                        ]
                    )
                ]
            )
