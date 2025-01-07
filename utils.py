def format_data(raw):
    # Filter out the past solved questions
    return [
        question["titleSlug"]
        for group in raw
        for question in group["questions"]
        if question["status"] == "PAST_SOLVED"
    ]


def get_first_successful_submission(submission_list):
    submissions = submission_list.get("submissions", [])

    if not submissions:
        return None

    for submission in submissions:
        if submission.get("status") == "AC":
            return submission.get("id")

    return None
