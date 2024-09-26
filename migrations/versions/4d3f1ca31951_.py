"""empty message

Revision ID: 4d3f1ca31951
Revises: 15c10257224e
Create Date: 2024-09-26 12:51:37.703941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d3f1ca31951'
down_revision = '15c10257224e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('media_type', sa.Enum('image', 'video', 'podcast', name='media-type'), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('medias')
    op.drop_table('comments')
    # ### end Alembic commands ###