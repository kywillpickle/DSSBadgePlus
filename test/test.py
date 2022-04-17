import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from DSSBadgePlus import badge, badgeCreator
import numpy as np

def main():
    iBadgeCreator = badgeCreator.BadgeCreator()
    iBadge = iBadgeCreator.generateBadge("Bunny McGee", badge.SurveyResults.APPROVED, "test/photos/bunny.png")
    iBadge.generate().save("test/results/result_bunny.png")

    iBadge = iBadgeCreator.generateBadge("Chick McClain", badge.SurveyResults.OVERDUE, "test/photos/chick.png")
    iBadge.generate().save("test/results/result_chick.png")

    iBadge = iBadgeCreator.generateBadge("Cow Shamow", badge.SurveyResults.NOT_APPROVED, "test/photos/cow.png")
    iBadge.generate().save("test/results/result_cow.png")

    iBadge = iBadgeCreator.generateBadge("Frog Francois", badge.SurveyResults.APPROVED_UNVACCINATED, "test/photos/frog.png")
    iBadge.generate().save("test/results/result_frog.png")

if __name__=="__main__":
    main()