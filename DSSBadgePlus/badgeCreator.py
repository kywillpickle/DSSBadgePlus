''' DSSBadge+
    by Kyle Pickle, Maggie Chen, and Michael Tsortos
    created for the HackDavis 2022 Hackathon

    badgeCreator.py
    A BadgeCreator generates unique badges given a user's info, survey results, and the current date.
    By design, all symptom survey results from the same date will have the same randomly-generated seal for that day.
'''
from DSSBadgePlus.badge import Badge as badge, SurveyResults
from datetime import datetime, date
import random
from colour import Color
from PIL import Image
import numpy as np

class BadgeCreator:
    # Initialize a new BadgeCreator object
    def __init__(self) -> None:
        ''' Initialize a new BadgeCreator object.

            :return: a new BadgeCreator object
        '''
        pass
    # Generate a badge given a user's info, survey results, and today's date
    def generateBadge(self, name="", surveyResults=SurveyResults.NOT_APPROVED, photo=None):
        ''' An enumerator containing all possible Daily Symptom Survey results.

            :param name: A str representing a user's preferred full name on Health E-Messaging
            :param surveyResults: A SurveyResults enum corresponding to the user's survey results (see below)
            :param photo: A str containing the file path of a user's photo
            :return: A PIL.Image object representing the generated Badge
        '''
        ibadge = badge(name, datetime.now(), surveyResults, photo, self.generateSeal())
        return ibadge
    # Generates a unique seal given the date
    def generateSeal(self):
        ''' Generate a PIL.Image object representing today's seal to put on the Badge.
            Combines a random Color with a random Seal image located in DSSBadgePlus/assets/seals, each from a pre-chosen set of 10.

            :return: a PIL.Image object representing the generated seal
        '''
        seed = random.seed(str(date.today()))
        colorSwitch = {
            0: "coral",
            1: "cyan",
            2: "hotpink",
            3: "lightslategray",
            4: "lightskyblue",
            5: "aquamarine",
            6: "burlywood",
            7: "plum",
            8: "thistle",
            9: "yellowgreen"
        }
        sealColor = Color(colorSwitch.get(random.randint(0,9)))
        seed = random.seed(str(seed))
        patternSwitch = {
            0: "DSSBadgePlus/assets/seals/eye.png",
            1: "DSSBadgePlus/assets/seals/face-smile.png",
            2: "DSSBadgePlus/assets/seals/gem.png",
            3: "DSSBadgePlus/assets/seals/hand-peace.png",
            4: "DSSBadgePlus/assets/seals/heart.png",
            5: "DSSBadgePlus/assets/seals/hourglass.png",
            6: "DSSBadgePlus/assets/seals/moon.png",
            7: "DSSBadgePlus/assets/seals/snowflake.png",
            8: "DSSBadgePlus/assets/seals/star.png",
            9: "DSSBadgePlus/assets/seals/sun.png"
        }
        img = Image.open(patternSwitch.get(random.randint(0,9)))
        data = np.array(img)   # "data" is a height x width x 4 numpy array
        red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

        # Replace white with red... (leaves alpha values alone...)
        black_areas = (red == 0) & (blue == 0) & (green == 0)
        data[..., :-1][black_areas.T] = (int(sealColor.get_red()*255), int(sealColor.get_green()*255), int(sealColor.get_blue()*255)) # Transpose back needed

        img = Image.fromarray(data)
        return img

