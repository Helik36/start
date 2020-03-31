from .dorctors.surgeons import get_surgeons
# . - из текущего пакета в пакете dorctors вызвать хирургов и взять от туда функ
def get_main():
	print("Мед")
	get_surgeons()  # вызываем