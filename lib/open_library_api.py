import requests
import json

class Search:
    def get_search_results(self):
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1
        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        response = requests.get(URL)
        return response.content

    def get_search_results_json(self):
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1
        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        print(f"Request URL: {URL}")
        response = requests.get(URL)
        return response.json()

    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1
        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        response = requests.get(URL).json()

        if response['docs']:
            response_formatted = f"Title: {response['docs'][0]['title']}\nAuthor: {response['docs'][0]['author_name'][0]}"
        else:
            response_formatted = "No results found. Please try another search term."
        return response_formatted


# results = Search().get_search_results()
# print(results)

# results_json = Search().get_search_results_json()
# print(json.dumps(results_json, indent=1))

if __name__ == "__main__":
    search_term = input("Enter a book title: ")
    result = Search().get_user_search_results(search_term)
    print("Search Result:\n")
    print(result)
