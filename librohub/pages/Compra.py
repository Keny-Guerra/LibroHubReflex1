from reflex import Component, TextBox, Image, Button, VStack, State, use_params, use_router

class CompraState(State):
    cantidad_compra = 1
    cantidad_disponible = 0

    def set_cantidad_compra(self, value):
        self.cantidad_compra = max(1, min(self.cantidad_disponible, int(value)))

    def handle_comprar(self):
        if self.cantidad_compra <= self.cantidad_disponible:
            self.cantidad_disponible -= self.cantidad_compra
            print(f"Has comprado {self.cantidad_compra} unidad(es).")

class Compra(Component):
    state = CompraState

    def render(self):
        params = use_params()
        libro = next((l for l in data['libros'] if l['nombre'] == params['nombreLibro']), None)

        if not libro:
            return TextBox(value="Libro no encontrado")

        self.state.cantidad_disponible = libro['cantidad']

        return VStack(
            children=[
                TextBox(value=libro['nombre']),
                Image(src=libro['imagen'], width="150px"),
                TextBox(value=f"Autor: {libro['autor']}"),
                TextBox(value=f"Precio: S/.{libro['precio']:.2f}"),
                TextBox(value=f"Cantidad disponible: {self.state.cantidad_disponible}"),
                TextBox(
                    type="number",
                    value=self.state.cantidad_compra,
                    min=1,
                    max=self.state.cantidad_disponible,
                    on_change=self.state.set_cantidad_compra
                ),
                Button(
                    on_click=self.state.handle_comprar,
                    text="Comprar" if self.state.cantidad_disponible > 0 else "Agotado",
                    disabled=self.state.cantidad_disponible == 0
                ),
            ]
        )
