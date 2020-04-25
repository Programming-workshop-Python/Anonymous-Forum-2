"""baseline

Revision ID: b29e181f46c2
Revises: 
Create Date: 2020-02-15 14:08:57.184241

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b29e181f46c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('created_on', sa.DateTime(), default=datetime.utcnow),
        sa.Column('updated_on', sa.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    )

def downgrade():
    op.drop_table('posts')
