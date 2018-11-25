"""New fields in User model

Revision ID: 445e52fb9613
Revises: b438a7373a0c
Create Date: 2018-11-25 14:23:36.876726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '445e52fb9613'
down_revision = 'b438a7373a0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###