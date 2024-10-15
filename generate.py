import pathlib

from jinja2 import Environment, FileSystemLoader 

jinja_env = Environment(
    loader=FileSystemLoader("templates")
)

templates_path = pathlib.Path("templates")

if __name__ == "__main__":
    pages = [
      {"url": "index.html", "title": "Home"},
      {"url": "folio.html", "title": "FOLIO Library Services Platform" },
      {"url": "compound-ai.html", "title": "Compound AI Systems"},
      {"url": "challenges.html", "title": "Challenges using LLMs"},
      {"url": "prompt-cataloging.html", "title": "Prompt Cataloging Example"},
      {"url": "upload-cataloging.html", "title": "Upload Image Cataloging Example"},
      {"url": "function-calling.html", "title": "FOLIO and Edge-AI Function Calling"},
      {"url": "dynamic-dags.html", "title": "Dynamic Airflow DAGs with Edge-AI"},
      {"url": "conclusion.html", "title": "Conclusion"},
      {"url": "resources.html", "title": "Resources" }
    ]

    for i,page in enumerate(pages):
        page_url = page['url']
        template_path = templates_path / page_url
        if template_path.exists():
            page_template = jinja_env.get_template(page_url)
            page_html = page_template.render(current_page=i, pages=pages)
            with pathlib.Path(page_url).open("w+") as fo:
                fo.write(page_html)
            print(f"Finished writing {page_url}")

        
