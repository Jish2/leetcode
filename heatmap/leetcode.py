import requests
import json

submission_calendar_query = """#graphql
query submissionCalendarQuery($username: String!) {
    matchedUser(username: $username) {
       submissionCalendar 
    }
}
"""


def get_submission_calendar(username: str):
    try:
        response = requests.post(
            "https://leetcode.com/graphql",
            headers={
                "Content-Type": "application/json",
                "Referer": "https://leetcode.com",
            },
            data=json.dumps(
                {
                    "query": submission_calendar_query,
                    "variables": {
                        "username": username,
                    },
                }
            ),
        )

        result = response.json()

        return json.loads(result["data"]["matchedUser"]["submissionCalendar"])
    except Exception as err:
        print("Error:", err)
        return
