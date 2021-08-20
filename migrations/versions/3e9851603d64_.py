"""empty message

Revision ID: 3e9851603d64
Revises: 
Create Date: 2021-08-19 19:54:52.771738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e9851603d64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('desafios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombreDesafio', sa.String(length=80), nullable=False),
    sa.Column('descripcionDesafio', sa.String(length=250), nullable=False),
    sa.Column('feat1', sa.String(length=120), nullable=False),
    sa.Column('feat2', sa.String(length=120), nullable=False),
    sa.Column('feat3', sa.String(length=120), nullable=False),
    sa.Column('photoURL', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripcionDesafio'),
    sa.UniqueConstraint('descripcionDesafio'),
    sa.UniqueConstraint('feat1'),
    sa.UniqueConstraint('feat1'),
    sa.UniqueConstraint('feat2'),
    sa.UniqueConstraint('feat2'),
    sa.UniqueConstraint('feat3'),
    sa.UniqueConstraint('feat3'),
    sa.UniqueConstraint('nombreDesafio'),
    sa.UniqueConstraint('nombreDesafio'),
    sa.UniqueConstraint('photoURL'),
    sa.UniqueConstraint('photoURL')
    )
    op.create_table('recetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.String(length=250), nullable=False),
    sa.Column('urlVideo', sa.String(length=250), nullable=False),
    sa.Column('urlFoto', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripcion'),
    sa.UniqueConstraint('descripcion'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('urlFoto'),
    sa.UniqueConstraint('urlFoto'),
    sa.UniqueConstraint('urlVideo'),
    sa.UniqueConstraint('urlVideo')
    )
    op.create_table('rutina',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.String(length=250), nullable=False),
    sa.Column('urlVideo', sa.String(length=250), nullable=False),
    sa.Column('urlFoto', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripcion'),
    sa.UniqueConstraint('descripcion'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nombre'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('dias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numeroDia', sa.Integer(), nullable=False),
    sa.Column('idDesafio', sa.Integer(), nullable=True),
    sa.Column('idReceta', sa.Integer(), nullable=True),
    sa.Column('idRutina', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idDesafio'], ['desafios.id'], ),
    sa.ForeignKeyConstraint(['idReceta'], ['recetas.id'], ),
    sa.ForeignKeyConstraint(['idRutina'], ['rutina.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todolog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('desafioID', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['desafioID'], ['desafios.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('templatetodo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('idDia', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idDia'], ['dias.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('templatetodo')
    op.drop_table('todolog')
    op.drop_table('dias')
    op.drop_table('user')
    op.drop_table('rutina')
    op.drop_table('recetas')
    op.drop_table('desafios')
    # ### end Alembic commands ###
