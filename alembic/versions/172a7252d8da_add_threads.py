"""add threads

Revision ID: 172a7252d8da
Revises: b29e181f46c2
Create Date: 2020-04-25 23:08:33.956806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import Index

revision = '172a7252d8da'
down_revision = 'b29e181f46c2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'threads',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
    )

    with op.batch_alter_table('posts') as batch_op:
        batch_op.add_column(sa.Column('thread_id', sa.Integer(), nullable=False, index=Index('post_thread_index')))
        batch_op.create_foreign_key('post_thread_constraint_fk', 'threads', ['thread_id'], ['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('post_thread_constraint_fk', 'posts', type_='foreignkey')
    op.drop_table('threads')
