#services/data_manager.py

class DataManager:
    """
    Classe para simular um banco de dados em memória.
    Os dados são armazenados em um dicionário e são perdidos ao reiniciar o servidor.

    COMO USAR:
    1. Instancie esta classe (ou use uma instância singleton) onde precisar gerenciar dados.
    2. Adicione métodos para manipular coleções de dados (ex: 'usuarios', 'projetos').
       - Exemplo de método para adicionar um item:
         def add_item(self, collection_name, item_data):
             if collection_name not in self._data:
                 self._data[collection_name] = []
             self._data[collection_name].append(item_data)
             return item_data
    3. Chame esses métodos a partir das suas rotas no Flask.
    """
    def __init__(self):
        """Inicializa o armazenamento de dados em memória."""
        self._data = {}
        print("DataManager inicializado. Dados serão armazenados em memória.")

    def get_all_data(self):
        """Retorna uma cópia de todos os dados para depuração ou visualização."""
        return self._data.copy()

# Instância única (Singleton pattern) para ser importada em outras partes da aplicação.
db_manager = DataManager()