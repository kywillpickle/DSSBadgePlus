# BadgeCreator

A **BadgeCreator** generates unique badges given a user's info, survey results, and the current date.
By design, all symptom survey results from the same date will have the same randomly-generated seal for that day.

## BadgeCreator.\_\_init__(self)

Initializes a new **BadgeCreator** object.

## BadgeCreator.generateBadge(self, name, surveyResults, photo)

An enumerator containing all possible Daily Symptom Survey results.

- `name`: A `str` representing a user's preferred full name on Health E-Messaging
- `surveyResults`: A `SurveyResults` enum corresponding to the user's survey results (see below)
- `photo`: A `str` containing the file path of a user's photo

As stated before, the generated badge's `datetime` variable is set to `datetime.now()`, and the `seal` is randomly generated based on its date.

## BadgeCreator.generateSeal(self)

Generate a `PIL.Image` object representing today's seal to put on the **Badge**. Combines a random *Color* with a random *Seal* image located in *DSSBadgePlus/assets/seals*, each from a pre-chosen set of 10.