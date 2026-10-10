from serpapi import GoogleSearch

my_key = "25b7c603dd6af3f2c48a0d0a71afe957ebb844adaba6edd1ac40ea4da4116be8"

# Ab google_jobs ki jagah google_search use kar rahe hain
params = {
  "engine": "google",
  "q": "Data Analyst Internship nagpur",
  "api_key": my_key
}

search = GoogleSearch(params)
results = search.get_dict()

# Bas title print karenge
if "organic_results" in results:
    for r in results["organic_results"][:5]:
        print(r["title"])
        print(r["link"])
        print("---")
else:
    print(results)