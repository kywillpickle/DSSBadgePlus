# DSSBadge+
**DSSBadge+** is a revamp of UC Davis Campus Ready's [Daily Symptom Survey](https://campusready.ucdavis.edu/symptom-survey), intended to be less prone to tampered survey results. It was submitted to [Devpost](https://devpost.com/software/dssbadge) as part of the HackDavis2022 hackathon.

![Slide 1](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/909/279/datas/gallery.jpg)

## Usage
**DSSBadge+** is a python package library made to be as simple as possible for developer use. We have provided extensive documentation on each class in the [docs/](https://github.com/kywillpickle/DSSBadgePlus/tree/develop/docs) folder. See the [test/](https://github.com/kywillpickle/DSSBadgePlus/tree/develop/test) folder for an example of where to start.

*Example:*
```py
iBadgeCreator = badgeCreator.BadgeCreator()
    iBadge = iBadgeCreator.generateBadge("John Doe", badge, SurveyResults.APPROVED, None)
    iBadge.generate().save("result.png")
```

## Background
_What is a **DSS**?_

The Daily Symptom Survey (DSS) is a minute-long survey that promotes a mindful check-in on a person's symptoms and evaluates whether or not they are approved to access campus facilities. The survey combats the spread of both COVID-19 and the Flu, while also acting as a tracker to ensure students, staff, and faculty are compliant with the campus testing requirements.

_**Why is** the spread of **COVID-19 worrisome** despite having access to masks and effective vaccinations?_

Unfortunately, the authorized vaccinations have shown to wane in efficacy over time, especially as the SARS-CoV-2 virus evolves and alters its structure. Any individual, healthy or at risk, is capable of developing long-term disease (commonly referred to as "Long COVID") that can have negative physical and mental health effects. The infection may also spread to vital parts of your body--especially the lungs.

_**How** can the **current pandemic come to an end** in **our community** specifically?_

Everyone must do their part in reducing the spread of COVID-19 by getting tested regularly, wearing highly effective masks (KN95, N95), completing the DSS, and quarantining when necessary. It is a **community effort**.

## Inspiration
Many students, faculty, and staff are non-compliant with the campus testing requirements and have found many creative ways to create counterfeit survey results--also known as DSS badges. This work-around threatens the health of the community as asymptomatic individuals may be unknowingly spreading COVID-19 or the Flu.

## What it does
This new DSS system uses DSS badges and adds alternating seals to survey results for tracking results made on different days. Each day has a different badge seal set to ensure a person's survey was filled on that specific day.

DSS is a simple package intended to be implemented into a website back-end to generate secure symptom survey results. It aims to prevent counterfeit DSS badges and contagious people from entering Davis facilities.

## How we built it
Our project was built using Python, and image editing programs like Pillow and Numpy. It is published on GitHub, and we worked on the code together using VSCode and VSLive.

## Challenges we ran into
Our group only had one programmer, so we were bottle-necked several times when he was stuck somewhere with the code. Our other two members are majoring in Biochemistry, creating an interdisciplinary team that required delegating tasks that matched the appropriate skill sets of each of our members.

## Accomplishments that we're proud of
As our project is a package intended to be implemented elsewhere, we spent a lot of time and detail writing docs and comments thoroughly explaining our package and how to use it. We are proud of this aspect, as well as our professional git and commenting practices.

## What we learned
Our group learned a lot about different aspects that go into making the Davis campus more secure and the effort Campus Ready has put into creating Daily Symptom Survey badges for everyone on campus. We have also all become much much more familiar with GitHub, markdown, and professional commenting practices.

## What's next for DSSBadge+
We hope that DSSBadge+ brings inspiration for improvements to the current daily symptom survey. It is strongly encouraged that these changes can be implemented to prevent further tampering with survey results and safer environments for the UC Davis community. It's a step in the right direction because frequent testing allows for the implementation of proper spread-preventative measures to eventually allow the UC Davis community to return to that sense of normalcy everyone has been eagerly seeking the entire duration of the pandemic.