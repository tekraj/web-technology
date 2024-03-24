"""empty message

Revision ID: 301d9bbc64a5
Revises: f74336db2e20
Create Date: 2024-03-24 22:49:46.233534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '301d9bbc64a5'
down_revision = 'f74336db2e20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('page', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.String(length=50), nullable=False))
        batch_op.create_unique_constraint(None, ['url'])

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['url'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('page', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('url')

    # ### end Alembic commands ###
