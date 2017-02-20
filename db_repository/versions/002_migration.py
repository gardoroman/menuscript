from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
item = Table('item', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('item_name', String(length=64)),
    Column('description', String(length=80)),
    Column('section', String(length=30)),
    Column('menu_id', Integer),
)

menu = Table('menu', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('category', String(length=80)),
    Column('store_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['item'].create()
    post_meta.tables['menu'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['item'].drop()
    post_meta.tables['menu'].drop()
