# test.py

Example class that generates a badge for a user.
The result is saved in `results/result.png`.

```py
iBadgeCreator = badgeCreator.BadgeCreator()
    iBadge = iBadgeCreator.generateBadge("John Doe", badge, SurveyResults.APPROVED, None)
    iBadge.generate().save("result.png")
```