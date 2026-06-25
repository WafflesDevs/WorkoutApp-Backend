"""Deleted Email off of Progress Table and other changes

Revision ID: 4e4176bd9c46
Revises: b9b9105d8204
Create Date: 2026-06-24 20:04:00.375220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e4176bd9c46'
down_revision: Union[str, Sequence[str], None] = 'b9b9105d8204'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Removing email from Progress table
    op.drop_column('Progress', 'email')

def downgrade() -> None:
    # Restore email if rolling back
    op.add_column('Progress', sa.Column('email', sa.String(), nullable=True))