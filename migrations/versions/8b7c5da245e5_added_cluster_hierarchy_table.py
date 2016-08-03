"""Added cluster hierarchy table

Revision ID: 8b7c5da245e5
Revises: a6acf65c378d
Create Date: 2016-08-01 17:06:51.457852

"""

# revision identifiers, used by Alembic.
revision = '8b7c5da245e5'
down_revision = 'a6acf65c378d'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cluster_hierarchy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.String(), nullable=False),
    sa.Column('parent', sa.Integer(), nullable=True),
    sa.Column('children', postgresql.ARRAY(sa.Integer()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('parent')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cluster_hierarchy')
    ### end Alembic commands ###