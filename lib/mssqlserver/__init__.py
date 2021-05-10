import pymssql
import logging


class ConnectionManager:
    __server = ''
    __user = ''
    __password = ''
    __db_name = ''
    __conn = None

    def __init__(self, server, user, password, dbname):
        self.__server = server
        self.__user = user
        self.__password = password
        self.__db_name = dbname

    def connect_to_database(self):
        """ Initializes connection object """
        try:
            logging.debug('connecting... to database "%s" on server "%s"' % (self.__db_name, self.__server))
            self.__conn = pymssql.connect(self.__server, self.__user, self.__password, self.__db_name)
            logging.debug('connected to database "%s" on server "%s"' % (self.__db_name, self.__server))
        except Exception as e:
            logging.debug('Error while connecting to database "%s" on server "%s"' % (self.__db_name, self.__server))
            print('Error while connecting to database "%s" on server "%s"' % (self.__db_name, self.__server))

    def execute_query(self, query, commit=False):
        """ Executes a SQL query and returns a list of rows. Each row is a dict.
        :param String query: The sql query passed as string.
        :param String commit: The boolean flag to commit if the query is DDL or DML.
        :return: List of rows. Each row is a dictionary.
        """
        cursor = self.__conn.cursor(as_dict=True)
        return_list = []
        logging.info("Query: "+query)
        cursor.execute(query)
        if commit:
            self.__conn.commit()
            return return_list

        for row in cursor:
            return_list.append(row)
        return return_list

    def execute_storedproc(self):
        """ Future implementation for executing stored procedures """
        raise NotImplementedError

    def disconnect_from_database(self):
        """ closes database connection """
        self.__conn.close()
        logging.info("Disconnecting from Database")


if __name__ == '__main__':
    c = ConnectionManager('http://127.0.0.1:1433', 'aniruddha', 'aniruddha', 'msdb')
    c.connect_to_database()
    c.execute_query('''SELECT * FROM [ngaddata].[dbo].[SYS_SYSTEM_TAB] ''')