"""Added keywords table

Revision ID: be96ce05edda
Revises: 490cf9604239
Create Date: 2016-06-28 08:47:05.651323

"""

# revision identifiers, used by Alembic.
revision = 'be96ce05edda'
down_revision = '490cf9604239'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keywords',
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('keywords', postgresql.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('url'),
    sa.UniqueConstraint('url')
    )
    op.create_unique_constraint(None, 'graphs', ['userid'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'graphs', type_='unique')
    op.drop_table('keywords')
    ### end Alembic commands ###
