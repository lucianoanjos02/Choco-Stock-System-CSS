from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAÇÕES DE CONEXÃO COM O BANCO

engine = create_engine('mysql+pymysql://adm:impacta2019ads@localhost:3306/CSS',
                       echo=False,
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         expire_on_commit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()           

# METODO DE CRIAÇÃO DAS TABELAS MAPEADAS PELAS CLASSES NO BANCO

def init_db():
    from models.usuario import Usuario
    from models.permissao import Permissao
    from models.loja import Loja
    from models.usuario_loja import UsuarioLoja
    from models.estoque import Estoque
    from models.produto import Produto
    from models.estoque_produto import EstoqueProduto
    from models.tipo_produto import TipoProduto
    from models.kit import Kit
    from models.kit_produto import KitProduto
    from models.notificacao import Notificacao
    from models.tipo_notificacao import TipoNotificacao
    from models.notificacao_usuario import NotificacaoUsuario
    Base.metadata.create_all(bind=engine)
init_db()