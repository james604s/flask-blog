"""update column breed

Revision ID: 669ab3d3db05
Revises: 
Create Date: 2021-05-15 21:19:05.182513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '669ab3d3db05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('breed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'breed')
    # ### end Alembic commands ###
