import os
import argparse
from utilities import url_utilities, db_utilities


def main(database: str, url_list_file: str):
    big_word_list = []
    print("we are going to work with " + database)
    print("we are going to scan with " + url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("Reading " + url)
        page_content = url_utilities.load_page(url=url)
        word = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(word)

    # Database code
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "words.db")
    db_utilities.create_database(database_path=path)
    db_utilities.save_words_to_database(database_path=path, words_list=big_word_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File Containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
