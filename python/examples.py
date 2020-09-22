# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *
import smbus2
import bme280

mylcd = RPi_I2C_driver.lcd()

porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)

calibracao_paramentros = bme280.load_calibration_params(bus, endereco)



contador = 0

while True:

	dado = bme280.sample(bus, endereco, calibracao_paramentros)

	# mylcd.lcd_display_string("Temperatura: ", 1)
	# mylcd.lcd_display_string(str(dado.temperature), 2)

	temperatura = "Temp. " + "{:.2f} ".format(dado.temperature)
	umidade = "Umid. " + "{:.2f}% ".format(dado.humidity)
	pressao = "Pressao. "+ "{:.2f} ".format(dado.pressure)

	print(temperatura+pressao+umidade)
	#print(umidade)
	#print(pressao)
	mylcd.lcd_display_string(temperatura+pressao, 1)
	mylcd.lcd_display_string(umidade, 2)


	sleep(1)
