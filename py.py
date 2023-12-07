import math

area = float(input("Informe o tamanho da área metros: "))

llatas = area / 6 * 1.1
latas = math.ceil(llatas / 18)
platas = latas * 80

lgaloes = area / 6 * 1.1
galoes = math.ceil(lgaloes / 3.6)
peloes = galoes * 25

lmist = area / 6 * 1.1
lt = int(lmist // 18)
gestura = math.ceil((lmist % 18) / 3.6)
pestura = lt * 80 + gestura * 25


print("\n1 ")
print("Quantidade de latas: {}".format(latas))
print("Preço total: R$ {:.2f}".format(platas))

print("\n2")
print("Quantidade de galões: {}".format(galoes))
print("Preço total: R$ {:.2f}".format(peloes))

print("\n3")
print("Quantidade de latas: {}".format(lt))
print("Quantidade de galões: {}".format(gestura))
print("Preço total: R$ {:.2f}".format(pestura))
