"""empty message

Revision ID: 831c8325db52
Revises: dc16d8df6bf5
Create Date: 2018-12-12 13:11:06.694518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '831c8325db52'
down_revision = 'dc16d8df6bf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
