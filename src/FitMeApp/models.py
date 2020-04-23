from django.db import models
from user.models import Trainee


class Task(models.Model):
    task_list = [
        ("beginner_day_1", "beginner_day_1"),
        ("beginner_day_2", "beginner_day_2"),
        ("beginner_day_3", "beginner_day_3"),
        ("beginner_day_4", "beginner_day_4"),
        ("beginner_day_5", "beginner_day_5"),
        ("beginner_day_6", "beginner_day_6"),
        ("beginner_day_7", "beginner_day_7"),
        ("beginner_day_8", "beginner_day_8"),
        ("beginner_day_9", "beginner_day_9"),
        ("beginner_day_10", "beginner_day_10"),
        ("beginner_day_10", "beginner_day_11"),
        ("beginner_day_10", "beginner_day_12"),
        ("beginner_day_10", "beginner_day_13"),
        ("beginner_day_10", "beginner_day_14"),
        ("beginner_day_10", "beginner_day_15"),
        ("beginner_day_10", "beginner_day_16"),
        ("beginner_day_10", "beginner_day_17"),
        ("beginner_day_10", "beginner_day_18"),
        ("beginner_day_10", "beginner_day_19"),
        ("beginner_day_10", "beginner_day_20"),
        ("beginner_day_10", "beginner_day_21"),
        ("beginner_day_10", "beginner_day_22"),
        ("beginner_day_10", "beginner_day_23"),
        ("beginner_day_10", "beginner_day_24"),
        ("beginner_day_10", "beginner_day_25"),
        ("beginner_day_10", "beginner_day_26"),
        ("beginner_day_10", "beginner_day_27"),
        ("beginner_day_10", "beginner_day_28"),
    ]
    person = models.ForeignKey(
        Trainee, on_delete=models.CASCADE, unique=False, default=""
    )
    task_complete = models.BooleanField(default=False)
    note = models.TextField()
    task_to_give = models.CharField(max_length=50, choices=task_list)

    def __str__(self):
        return f"{self.person}"
