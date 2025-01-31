class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto):
        if producto.codigo not in self.carrito.keys():
            self.carrito[producto.codigo]={
                "nombre":producto.nombre,
                "producto_id":producto.codigo,
                "disponibilidad":producto.disponibilidad,
                "precio": str (producto.precio),
                "cantidad": 1,
                "total": producto.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key == producto.codigo:
                    value["cantidad"] = value ["cantidad"]+1
                    value["precio"] = producto.precio
                    value["total"] = value["total"] + producto.precio
                    break
            self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = producto.codigo_sku
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self, producto):
        for key, value in self.carrito.items():
            if key == producto.codigo_sku:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- producto.precio
                if value["cantidad"] < 1:   
                    self.eliminar(producto)
                break
        self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified=True 