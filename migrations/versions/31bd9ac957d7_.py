"""empty message

Revision ID: 31bd9ac957d7
Revises: bce7bcc78fbb
Create Date: 2021-08-21 21:32:38.445160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '31bd9ac957d7'
down_revision = 'bce7bcc78fbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('templatetodo', sa.Column('todoUsuario', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'templatetodo', 'todousuario', ['todoUsuario'], ['id'])
    op.drop_constraint('todousuario_ibfk_1', 'todousuario', type_='foreignkey')
    op.drop_column('todousuario', 'todoID')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todousuario', sa.Column('todoID', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('todousuario_ibfk_1', 'todousuario', 'templatetodo', ['todoID'], ['id'])
    op.drop_constraint(None, 'templatetodo', type_='foreignkey')
    op.drop_column('templatetodo', 'todoUsuario')
    # ### end Alembic commands ###
