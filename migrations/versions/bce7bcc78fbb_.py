"""empty message

Revision ID: bce7bcc78fbb
Revises: 22d42a2b06da
Create Date: 2021-08-21 15:39:52.066642

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bce7bcc78fbb'
down_revision = '22d42a2b06da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todousuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('todoID', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['todoID'], ['templatetodo.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('todolog')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolog',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('userID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('done', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('todoID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['todoID'], ['templatetodo.id'], name='todolog_ibfk_3'),
    sa.ForeignKeyConstraint(['userID'], ['user.id'], name='todolog_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('todousuario')
    # ### end Alembic commands ###
