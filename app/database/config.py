#datos para la coneccion a la base de datos

dataBaseName = "gestorDb"
userName = "root"
userPassword = None
conetionPort = 3306
server = "localhost"

#creando la coneccion a la base de datos
dataBaseConector = f"mysql+mysqlconector://{userName}:{userPassword}:@{server}:{conetionPort}/{dataBaseName}"
print (dataBaseConector)