import sqlite3
from sqlite3.dbapi2 import Cursor


class DataBase():
    def __init__(self, name = "system.db") -> None:
        self.name = name
    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS users(

                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                    
                );
            
            """)
        except AttributeError:
            print("faça a conexão")

    def insert_user(self, name, user, password, access):

        cursor = self.connection.cursor()
        cursor.execute("""

            INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)
        
        """,(name,user, password, access))
        self.connection.commit()
   
    def check_user(self, user, password):

        try: 
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM users;
            
            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Administrador":
                    return "Administrador"
 
                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Usuário":        
                    return "user"

                else:
                    continue
            return "sem acesso"
        except:
            pass

    def insert_data(self, full_dataset):

        cursor = self.connection.cursor()

        campos_tabela = (
            'NFe','serie','data_emissao','chave','cnpj_emitente','nome_emitente',
             'valorNfe','itemNota','cod','qntd','descricao','unidade_medida','valorProd',
             'data_importacao','usuario','data_saida' )  
        qntd = ','.join(map(str, '?'*16))
        query = f"""INSERT INTO Notas {campos_tabela} VALUES ({qntd})"""

        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
                self.connection.commit()
        except sqlite3.IntegrityError:
            print('Nota já existe no banco')

    def create_table_nfe(self):

        cursor = self.connection.cursor()

        cursor.execute(f"""

            CREATE TABLE IF NOT EXISTS Notas(

            NFe TEXT,
            serie TEXT,
            data_emissao TEXT,
            chave TEXT,
            cnpj_emitente TEXT,
            nome_emitente TEXT,                
            valorNfe TEXT,
            itemNota TEXT,
            cod TEXT,
            qntd TEXT,
            descricao TEXT,
            unidade_medida TEXT,
            valorProd TEXT,
            data_importacao TEXT,
            usuario TEXT,
            data_saida TEXT,


        
        PRIMARY KEY(Chave, Nfe, itemNota)                

            );

        """)

    def uptdate_estoque(self, data_saida, user, notas):
        try:
            cursor = self.connection.cursor()
            for nota in notas:
                cursor.execute(f"""UPDATE Notas SET Data_saida = '{data_saida}', 
                usuario ='{user}' WHERE Nfe =  '{nota}'""")
                self.connection.commit()

        except AttributeError:
            print("faça a conexão para alterar campos")

    def update_estorno(self, notas):

        try:
            cursor = self.connection.cursor()

            for nota in notas:
                cursor.execute(f"UPDATE Notas SET Data_saida = '' WHERE NFe = {nota}"                               )

                self.connection.commit()

        except AttributeError:
            print('faça a conexão para alterar campos.')           

if __name__ == "__main__":

    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.create_table_nfe()
    db.close_connection()
