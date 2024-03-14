"""add content column to posts table

Revision ID: c6d24f87e660
Revises: 263deb132edf
Create Date: 2024-03-13 18:58:44.475909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6d24f87e660'
down_revision: Union[str, None] = '263deb132edf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
