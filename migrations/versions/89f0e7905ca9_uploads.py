"""uploads

Revision ID: 89f0e7905ca9
Revises: 86df810f284e
Create Date: 2018-06-07 10:42:40.640721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89f0e7905ca9'
down_revision = '86df810f284e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image_filename', sa.String(), nullable=True))
    op.add_column('post', sa.Column('image_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'image_url')
    op.drop_column('post', 'image_filename')
    # ### end Alembic commands ###