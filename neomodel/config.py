AUTO_INSTALL_LABELS = False
DATABASE_URL = 'bolt://neo4j:neo4j@localhost:7687'
FORCE_TIMEZONE = False
ENCRYPTED_CONNECTION = True
MAX_POOL_SIZE = 50
# neo4j defaults 3600, 100
MAX_CONNECTION_LIFETIME = 3600  # 1h
MAX_CONNECTION_POOL_SIZE = 150
MAX_CONNECTION_RETRY = 3