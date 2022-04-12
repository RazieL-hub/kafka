import sqlalchemy

metadata = sqlalchemy.MetaData()

reports = sqlalchemy.Table(
    'reports',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=256)),
    sqlalchemy.Column('status', sqlalchemy.Boolean, default=False),
)
