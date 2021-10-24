Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def total_factura(cantidad, por_iva=12):
    valor_iva=((float(cantidad)*por_iva)/100)
    return float(cantidad+valor_iva)

print("Valor factura con iva 14: "+ str(total_factura(10,14)))
Valor factura con iva 14: 11.4
print("Valor factura con iva por defecto: "+ str(total_factura(10)))
Valor factura con iva por defecto: 11.2
