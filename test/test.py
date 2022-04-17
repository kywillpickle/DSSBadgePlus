import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from DSSBadgePlus import badge, badgeCreator
import numpy as np

def main():
    iBadgeCreator = badgeCreator.BadgeCreator()
    iBadge = iBadgeCreator.generateBadge("John Doe", badge.SurveyResults.APPROVED, None)
    iBadge.generate().save("result.png")

if __name__=="__main__":
    main()