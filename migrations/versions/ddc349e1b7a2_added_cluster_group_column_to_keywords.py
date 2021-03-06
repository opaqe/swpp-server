"""added cluster/group column to keywords

Revision ID: ddc349e1b7a2
Revises: be96ce05edda
Create Date: 2016-06-28 16:11:04.206843

"""

# revision identifiers, used by Alembic.
revision = 'ddc349e1b7a2'
down_revision = 'be96ce05edda'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('keywords', sa.Column('group', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'keywords', ['url'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'keywords', type_='unique')
    op.drop_column('keywords', 'group')
    ### end Alembic commands ###
