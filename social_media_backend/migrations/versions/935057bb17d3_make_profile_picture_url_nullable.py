"""Make profile_picture_url nullable

Revision ID: 935057bb17d3
Revises: 
Create Date: 2025-04-14 16:17:31.440622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '935057bb17d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('profile_picture_url',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('profile_picture_url',
               existing_type=sa.TEXT(),
               nullable=False)

    # ### end Alembic commands ###
