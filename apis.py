import requests
import json
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()
# 从环境变量中获取 COOKIE
COOKIE = os.getenv("COOKIE")


class Leetcode:
    def __init__(self):
        self.prefix = "https://leetcode.cn"
        self.url = f"{self.prefix}/graphql/"
        self.headers = {
            "Content-Type": "application/json",
        }
        self.headers_cookies = {"Content-Type": "application/json", "Cookie": COOKIE}

    # 获取LeetCode 热题 100题库
    # https://leetcode.cn/studyplan/top-100-liked/
    def get_top_100_liked_questions(self):

        payload = {
            "query": """
                query studyPlanPastSolved($slug: String!) {
                    studyPlanV2Detail(planSlug: $slug) {
                        planSubGroups {
                            slug
                            questions {
                                titleSlug
                                status
                            }
                        }
                    }
                }
            """,
            "variables": {"slug": "top-100-liked"},
            "operationName": "studyPlanPastSolved",
        }
        try:
            response = requests.post(
                self.url,
                headers=self.headers_cookies,
                data=json.dumps(payload),
            )
            response.raise_for_status()
            data = response.json()
            return data["data"]["studyPlanV2Detail"]["planSubGroups"]
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    # 获取题目详情
    def get_question_detail(self, slug):
        config = {
            "method": "post",
            "url": self.url,
            "body": json.dumps(
                {
                    "operationName": "questionData",
                    "variables": {"titleSlug": slug},
                    "query": """
                    query questionData($titleSlug: String!) {
                        question(titleSlug: $titleSlug) {
                            questionId
                            questionFrontendId
                            categoryTitle
                            boundTopicId
                            title
                            titleSlug
                            content
                            translatedTitle
                            translatedContent
                            isPaidOnly
                            difficulty
                            likes
                            dislikes
                            isLiked
                            similarQuestions
                            contributors {
                                username
                                profileUrl
                                avatarUrl
                                __typename
                            }
                            langToValidPlayground
                            topicTags {
                                name
                                slug
                                translatedName
                                __typename
                            }
                            companyTagStats
                            codeSnippets {
                                lang
                                langSlug
                                code
                                __typename
                            }
                            stats
                            hints
                            solution {
                                id
                                canSeeDetail
                                __typename
                            }
                            status
                            sampleTestCase
                            metaData
                            judgerAvailable
                            judgeType
                            mysqlSchemas
                            enableRunCode
                            envInfo
                            book {
                                id
                                bookName
                                pressName
                                source
                                shortDescription
                                fullDescription
                                bookImgUrl
                                pressImgUrl
                                productUrl
                                __typename
                            }
                            isSubscribed
                            isDailyQuestion
                            dailyRecordStatus
                            editorType
                            ugcQuestionId
                            style
                            exampleTestcases
                            __typename
                        }
                    }
                """,
                }
            ),
        }
        try:
            response = requests.post(
                self.url, headers=self.headers_cookies, data=config["body"]
            )
            response.raise_for_status()
            data = response.json()
            return data["data"]["question"]
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    # 获取题目题解提交列表
    def get_question_submission_list(self, slug):
        payload = {
            "query": """
                query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!, $lang: String, $status: SubmissionStatusEnum) {
                    submissionList(
                        offset: $offset
                        limit: $limit
                        lastKey: $lastKey
                        questionSlug: $questionSlug
                        lang: $lang
                        status: $status
                    ) {
                        lastKey
                        hasNext
                        submissions {
                            id
                            title
                            status
                            statusDisplay
                            lang
                            langName: langVerboseName
                            runtime
                            timestamp
                            url
                            isPending
                            memory
                            frontendId
                            submissionComment {
                                comment
                                flagType
                            }
                        }
                    }
                }
            """,
            "variables": {
                "questionSlug": slug,
                "offset": 0,
                "limit": 20,
                "lastKey": None,
                "status": None,
            },
            "operationName": "submissionList",
        }
        try:
            response = requests.post(
                self.url,
                headers=self.headers_cookies,
                data=json.dumps(payload),
            )
            response.raise_for_status()
            data = response.json()
            return data["data"]["submissionList"]
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    # 获取题目题解
    def get_question_solution(self, submission_id):
        config = {
            "body": json.dumps(
                {
                    "query": """
                    query submissionDetails($submissionId: ID!) {
                        submissionDetail(submissionId: $submissionId) {
                            code
                            timestamp
                            statusDisplay
                            isMine
                            runtimeDisplay: runtime
                            memoryDisplay: memory
                            memory: rawMemory
                            lang
                            langVerboseName
                            question {
                                questionId
                                titleSlug
                                hasFrontendPreview
                            }
                            user {
                                realName
                                userAvatar
                                userSlug
                            }
                            runtimePercentile
                            memoryPercentile
                            submissionComment {
                                flagType
                            }
                            passedTestCaseCnt
                            totalTestCaseCnt
                            fullCodeOutput
                            testDescriptions
                            testInfo
                            testBodies
                            stdOutput
                            ... on GeneralSubmissionNode {
                                outputDetail {
                                    codeOutput
                                    expectedOutput
                                    input
                                    compileError
                                    runtimeError
                                    lastTestcase
                                }
                            }
                            ... on ContestSubmissionNode {
                                outputDetail {
                                    codeOutput
                                    expectedOutput
                                    input
                                    compileError
                                    runtimeError
                                    lastTestcase
                                }
                            }
                        }
                    }
                """,
                    "variables": {"submissionId": submission_id},
                    "operationName": "submissionDetails",
                }
            ),
        }
        try:
            response = requests.post(
                self.url, headers=self.headers_cookies, data=config["body"]
            )
            response.raise_for_status()
            data = response.json()
            return data["data"]["submissionDetail"]["code"]
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
