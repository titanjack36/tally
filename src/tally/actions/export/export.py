from typing import List

from tally.models.activity import Activity
from tally.models.user import User
from tally.models.config import Config
from tally.actions.export.save_activity import save_activities


def export():
    config: Config | None = Config.select().first()
    if not config:
        print(
            "No active challenge found. Start a new challenge first. Cancelling operation."
        )
        return

    activities: List[Activity] = (
        Activity.select().join(User).order_by(User.name, Activity.start_time.asc())
    )
    save_activities(activities, config)
