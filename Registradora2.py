import unittest

class Registradora(object):
    
    n=[]
    
    #armado de lista de compras
    def armado_lista(self,n):
        compras=[]
        for i in n:
            compras.append(i)
        return compras

    #calculo de total de compra
    def precios(self,n):
        articulos={1:25,2:30,3:45,4:20}
        subtotal=0
        for i in n:
            precio= articulos.get(i, 'no se encontro producto')
            subtotal+=precio
        return subtotal

    #calculo de descuento
    def descuento(self,n):
        desc={1:2.5,2:1.5,3:4.5,4:10}
        descuento_total=0
        for i in n:
            desc_unit=desc.get(i, 0)
            descuento_total+=desc_unit
        return descuento_total

    #total con descuento
    def total(self,n):
        articulos={1:25,2:30,3:45,4:20}
        subtotal=0
        desc={1:2.5,2:1.5,3:4.5,4:10}
        descuento_total=0
        for i in n:
            precio= articulos.get(i, 'no se encontro producto')
            subtotal+=precio
            desc_unit=desc.get(i, 0)
            descuento_total+=desc_unit
        total=subtotal-descuento_total
        return total

    #vuelto que se debe dar
    def vuelto(self,n,imp):
        articulos={1:25,2:30,3:45,4:20}
        subtotal=0
        desc={1:2.5,2:1.5,3:4.5,4:10}
        descuento_total=0
        for i in n:
            precio= articulos.get(i, 'no se encontro producto')
            subtotal+=precio
            desc_unit=desc.get(i, 0)
            descuento_total+=desc_unit
        total=subtotal-descuento_total
        vuelto= imp - total
        return vuelto


    

    

class test_regitradora(unittest.TestCase):
    def setUp(self):
        self.lista= Registradora()      

    def test_lista_productos(self):
        lista = self.lista.armado_lista([1,2,3])
        self.assertEqual([1,2,3],lista)

    def test_precios(self):
        precios= self.lista.precios([1,2])
        self.assertEqual(55,precios)

    def test_precios2(self):
        precios= self.lista.precios([1,2,3,4])
        self.assertEqual(120,precios)
    
    def test_descuento(self):
        descuento= self.lista.descuento([1,2,3,4])
        self.assertEqual(18.5,descuento)

    def test_total(self):
        total= self.lista.total([1,2,3,4])
        self.assertEqual(101.5,total)

    def test_vuelto(self):
        vuelto= self.lista.vuelto([1,2,3,4],110)
        self.assertEqual(8.5,vuelto)
    
    

if __name__=='__main__':
    unittest.main()
