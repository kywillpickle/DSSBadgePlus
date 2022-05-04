# test.py

Example class that generates a badge for a user.
The result is saved in `results/result.png`.

Essentially, all you have to do is make a new BadgeGenerator and call `.generate()`:
```py
iBadgeCreator = badgeCreator.BadgeCreator()
iBadge = iBadgeCreator.generateBadge("Bunny McGee", badge.SurveyResults.APPROVED, "test/photos/bunny.png")
iBadge.generate().save("test/results/result_bunny.png")
```