# Badge

Each **Badge** blueprint represents a specific badge instance.
It contains an image generated for several input variables.

## Badge.\_\_init__(self, name, datetime, surveyResults, photo, seal)

Initializes a new **Badge** object.

- `name`: A `str` representing a user's preferred full name on Health E-Messaging
- `datetime`: A `datetime` object containing the date and time a user's survey was completed
- `surveyResults`: A `SurveyResults` enum corresponding to the user's survey results (see below)
- `photo`: A `str` containing the file path of a user's photo
- `seal`: `PIL.Image` object with the generated seal to put over the badge

## SurveyResults

An enumerator containing all possible Daily Symptom Survey results.

0. `APPROVED` - Fully approved to access campus facilities
1. `APPROVED_UNVACCINATED` - Approved, but must wear mask indoors
2. `OVERDUE` - Approved to get tested but not to access campus facilities
3. `APPROVED_RESTRICTED` - Approved to access designated healthcare facilities
4. `NOT_APPROVED` - Not approved to access any facilities

## Badge.generate(self)

Generate a `PIL.Image` object representing this specific **Badge** given its instance variables.