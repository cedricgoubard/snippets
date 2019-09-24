class DAOSQL:
    def __init__(self, engine):
        self.engine = engine
        
    def ls_tables(self, system_tables=False):
        tables = self.engine.execute(
            "SELECT table_schema,table_name FROM information_schema.tables ORDER BY table_schema,table_name;"
        ).fetchall()
        if not system_tables:
            return [x[1] for x in tables if x[0] not in ['pg_catalog', 'information_schema']]
        return [x[1] for x in tables]
    
    def ls_columns(self, table_name):
        columns = self.engine.execute(
            "SELECT * FROM information_schema.columns WHERE table_name = '{}' ;".format(table_name)
        ).fetchall()
        return [(c[3], c[7]) for c in columns]
    
    def create_table(self, table_name, schema):
        """Creates a table.
        Schema example: (id serial PRIMARY KEY, num integer, data varchar)
        """
        self.engine.execute("CREATE TABLE {} ({});".format(table_name, schema))
        
    def empty_table(self, table_name):
        self.engine.execute("TRUNCATE " + table_name)
