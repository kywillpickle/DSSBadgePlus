''' DSSBadge+
    by Kyle Pickle, Maggie Chen, and Michael Tsortos
    created for the HackDavis 2022 Hackathon

    badge.py
    Each Badge blueprint represents a specific badge instance. It contains an image generated for several input variables.
'''
from enum import Enum
from datetime import datetime as dt
from PIL import Image, ImageDraw, ImageFont


# An enumerator containing all possible Daily Symptom Survey results.
class SurveyResults(Enum):
    # Fully approved
    APPROVED = 0
    # Approved, but must wear mask indoors
    APPROVED_UNVACCINATED = 1
    # Approved to get tested but not to access campus facilities
    OVERDUE = 2
    # Approved to access designated healthcare facilities
    APPROVED_RESTRICTED = 3
    # Not approved
    NOT_APPROVED = 4

# Initialize a new Badge object
class Badge:
    def __init__(self, name="", datetime=dt.now(), surveyResults=SurveyResults.NOT_APPROVED, photo="", seal=None) -> None:
        ''' Initialize a new Badge object.
        
            :param name: A str representing a user's preferred full name on Health E-Messaging
            :param datetime: A datetime object containing the date and time a user's survey was completed
            :param surveyResults: A SurveyResults enum corresponding to the user's survey results (see below)
            :param photo: A str containing the file path of a user's photo
            :param seal: PIL.Image object with the generated seal to put over the badge
            :return: a new Badge object
            '''
        self.name = name # A user's preferred full name
        self.datetime = datetime # The date and time a user's survey was completed
        self.surveyResults = surveyResults # A SurveyResults enum corresponding to the user's survey results
        self.photo = photo # The file path of a user's photo
        self.seal = seal # The generated seal to put over the badge
        self.img = self.generate()
    
    # Generate an image given this badge's instance variables
    def generate(self):
        ''' Generate a PIL.Image object representing this specific Badge given its instance variables.

            :return: a PIL.Image object
        '''
        # Make a blank template
        img = Image.new("RGBA", (750, 1000), "WHITE")
        # Add the seal
        img.paste(self.seal, (0, 0), self.seal)
        img.alpha_composite(Image.open(self.photo),(247,120))
        # Draw the survey results
        draw = ImageDraw.Draw(img, "RGBA")
        font = ImageFont.truetype("DSSBadgePlus/assets/Calibri.ttf", 110)
        w, h = draw.textsize(self.name, font=font)
        draw.text(((750-w)/2,495-h), self.name, (0, 0, 0), font, align='center', stroke_width=2)
        font = ImageFont.truetype("DSSBadgePlus/assets/Calibri.ttf", 140)
        w, h = draw.textsize("APPROVED", font=font)
        if self.surveyResults == SurveyResults.APPROVED:
            img.alpha_composite(Image.new("RGBA", (680, 200), (0, 255, 0, 160)),(35,515))
            draw.text(((750-w)/2, 555), "APPROVED", (0, 0, 0), font, align='center', stroke_width=2)
        elif self.surveyResults == SurveyResults.APPROVED_UNVACCINATED:
            img.alpha_composite(Image.new("RGBA", (680, 200), (120, 0, 180, 160)),(35,515))
            draw.text(((750-w)/2, 555), "APPROVED", (0, 0, 0), font, align='center', stroke_width=2)
        elif self.surveyResults == SurveyResults.OVERDUE:
            img.alpha_composite(Image.new("RGBA", (680, 200), (200, 200, 0, 160)),(35,515))
            w, h = draw.textsize("OVERDUE", font=font)
            draw.text(((750-w)/2, 555), "OVERDUE", (0, 0, 0), font, align='center', stroke_width=2)
        elif self.surveyResults == SurveyResults.APPROVED_RESTRICTED:
            img.alpha_composite(Image.new("RGBA", (680, 200), (200, 100, 0, 160)),(35,515))
            draw.text(((750-w)/2, 555), "APPROVED", (0, 0, 0), font, align='center', stroke_width=2)
        elif self.surveyResults == SurveyResults.NOT_APPROVED:
            img.alpha_composite(Image.new("RGBA", (720, 200), (150, 0, 0, 160)),(15,515))
            font = ImageFont.truetype("DSSBadgePlus/assets/Calibri.ttf", 106)
            w, h = draw.textsize("NOT APPROVED", font=font)
            draw.text(((750-w)/2, 568), "NOT APPROVED", (0, 0, 0), font, align='center', stroke_width=2)
        font = ImageFont.truetype("DSSBadgePlus/assets/Calibri.ttf", 80)
        datestr = self.datetime.strftime("%A, %B %d\n%I:%M%p")
        w, h = draw.textsize(datestr, font=font)
        draw.text(((750-w)/2,735), datestr, (0, 0, 0), font, align='center', stroke_width=2,spacing=15)
        return img