from reflex import Component, State, TextBox, Button, Image, Box, VStack, HStack, List, ListItem, use_effect
from reflex.router import use_router
import requests
import json

# Cargar datos iniciales desde `data.json`
with open('data.json', 'r') as f:
    data = json.load(f)['libros']

class AdminState(State):
    libros = data
    nombre = ""
    autor = ""
    precio = ""
    cantidad = ""
    imagen = None
    edit_index = None

    def handle_add_or_edit(self):
        form_data = {
            "nombre": self.nombre,
            "autor": self.autor,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "imagen": self.imagen,
            "editIndex": self.edit_index,
        }
        response = requests.post("http://localhost:5000/addBook", files=form_data)
        self.libros = response.json()['libros']
        self.reset_fields()

    def reset_fields(self):
        self.nombre = self.autor = self.precio = self.cantidad = ""
        self.imagen = None
        self.edit_index = None

    def handle_edit(self, index):
        libro = self.libros[index]
        self.nombre, self.autor, self.precio, self.cantidad = libro['nombre'], libro['autor'], str(libro['precio']), str(libro['cantidad'])
        self.imagen = libro.get('imagen', None)
        self.edit_index = index

    def handle_delete(self, index):
        self.libros.pop(index)

class Admin(Component):
    state = AdminState

    def render(self):
        return VStack(
            class_name="crudContainer",
            children=[
                VStack(
                    class_name="agregarLibrosInput",
                    children=[
                        TextBox(placeholder="Nombre", value=self.state.nombre, on_change=self.state.set_nombre),
                        TextBox(placeholder="Autor", value=self.state.autor, on_change=self.state.set_autor),
                        TextBox(type="number", placeholder="Precio", value=self.state.precio, on_change=self.state.set_precio),
                        TextBox(type="number", placeholder="Cantidad", value=self.state.cantidad, on_change=self.state.set_cantidad),
                        TextBox(type="file", accept="image/*", on_change=self.state.set_imagen),
                        Button(
                            on_click=self.state.handle_add_or_edit,
                            text="Modificar" if self.state.edit_index is not None else "Agregar"
                        ),
                    ],
                ),
                List(
                    class_name="listaLibros",
                    children=[
                        ListItem(
                            key=index,
                            children=[
                                Image(src=libro['imagen'], width="50px"),
                                *[TextBox(value=f"{key.capitalize()}: {value}") for key, value in libro.items() if key != 'imagen'],
                                Button(text="Editar", class_name="editar", on_click=lambda idx=index: self.state.handle_edit(idx)),
                                Button(text="Eliminar", class_name="eliminar", on_click=lambda idx=index: self.state.handle_delete(idx)),
                            ],
                        ) for index, libro in enumerate(self.state.libros)
                    ]
                )
            ],
        )
