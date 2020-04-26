"""add boards

Revision ID: 62c0b608b32d
Revises: 172a7252d8da
Create Date: 2020-04-26 13:22:30.817344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import Index

revision = '62c0b608b32d'
down_revision = '172a7252d8da'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'boards',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
    )

    with op.batch_alter_table('threads') as batch_op:
        batch_op.add_column(sa.Column('board_id', sa.Integer(), nullable=False, index=Index('thread_board_index')))
        batch_op.create_foreign_key('thread_board_constraint_fk', 'boards', ['board_id'], ['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('thread_board_constraint_fk', 'threads', type_='foreignkey')
    op.drop_table('boards')
