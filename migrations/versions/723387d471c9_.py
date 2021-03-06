"""empty message

Revision ID: 723387d471c9
Revises: 15791a4b1d49
Create Date: 2021-12-12 18:30:42.888381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '723387d471c9'
down_revision = '15791a4b1d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todo_name', sa.String(length=220), nullable=False),
    sa.Column('ended', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###
