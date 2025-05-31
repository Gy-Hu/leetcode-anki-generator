import genanki
import html
from constants import TEMPLATE_QFMT, TEMPLATE_AFMT, CSS_STYLE
import json
from apis import Leetcode
from utils import format_data, get_first_successful_submission


def create_anki_deck(cards):
    # 创建模型（定义卡片结构和样式）
    my_model = genanki.Model(
        1607392319,  # 模型唯一 ID（需为随机生成或固定整数）
        "Simple Model",  # 模型名称
        fields=[  # 定义字段
            {"name": "Front"},  # 正面字段
            {"name": "Header"},  # 正面字段
            {"name": "Back"},  # 背面字段
        ],
        templates=[  # 定义卡片模板
            {
                "name": "Card 1",  # 模板名称
                "qfmt": TEMPLATE_QFMT,  # 正面内容，{{Front}} 引用字段名称
                "afmt": TEMPLATE_AFMT,  # 背面内容
            },
        ],
        css=CSS_STYLE,  # 定义样式
    )

    # 创建一个卡组（Deck）
    my_deck = genanki.Deck(
        2059400110,  # 卡组唯一 ID
        "Leetcode My AC",  # 卡组名称
    )

    # 添加卡片到卡组
    for card in cards:
        note = genanki.Note(
            model=my_model,  # 使用定义的模型
            fields=[card["front"], card["header"], card["back"]],  # 填写正面和背面内容
        )
        my_deck.add_note(note)

    # 导出为 .apkg 文件
    genanki.Package(my_deck).write_to_file("leetcode_my_ac.apkg")

    print("Deck exported as 'leetcode_my_ac.apkg'")


def fetchData():
    # Create an instance of the Leetcode class
    leetcode = Leetcode()

    # Get the top 100 liked questions
    top_100_liked_questions = leetcode.get_top_100_liked_questions()
    # print(json.dumps(top_100_liked_questions, indent=2, ensure_ascii=False))
    title_slug_list = format_data(top_100_liked_questions)

    # Get the first 5 elements from titleSlugList
    test_slugs = title_slug_list

    # Initialize an array to collect the data
    collected_data = []
    # Counter for successful requests
    success_count = 0

    # Loop through each slug and get details and submission list
    for index, slug in enumerate(test_slugs, start=1):
        try:
            print(f"Processing {index}/{len(test_slugs)}: {slug}")

            # Get the details of the specific question
            question_detail = leetcode.get_question_detail(slug)
            # print(f"Question Detail for {slug}:")
            # print(json.dumps(question_detail, indent=2, ensure_ascii=False))

            # Get the submission list for the specific question
            submission_list = leetcode.get_question_submission_list(slug)
            # print(f"Submission List for {slug}:")
            # print(json.dumps(submission_list, indent=2, ensure_ascii=False))

            # Find the first successful submission
            # submission_id = "591348764"
            submission_id = get_first_successful_submission(submission_list)

            if submission_id:
                success_count += 1
                # print(f"First Successful Submission for {slug}:")
                # print(json.dumps(submission_id, indent=2, ensure_ascii=False))
                question_solution = leetcode.get_question_solution(submission_id)
                # print(json.dumps(question_solution, indent=2, ensure_ascii=False))
                # Collect the data in the object array
                collected_data.append(
                    {
                        "front": question_detail["translatedContent"],
                        "header": question_detail["translatedTitle"],
                        "back": f"""<pre>```python\n{html.escape(question_solution)}```</pre>""",
                    }
                )
            # else:
            #     print(f"No successful submissions found for {slug}")
        except Exception as e:
            print(f"An error occurred for slug {slug}: {e}")
    print(f"Number of successful requests: {success_count}")
    return collected_data


# 调用函数创建卡组
create_anki_deck(fetchData())
