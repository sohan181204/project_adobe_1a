import fitz  # PyMuPDF
import json
import time

def extract_structure(pdf_path):
    start_time = time.time()
    doc = fitz.open(pdf_path)
    title = "Unknown"
    outline = []
    seen = set()

    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = " ".join(span["text"] for span in line["spans"]).strip()
                if not line_text or line_text in seen:
                    continue

                seen.add(line_text)

                if i == 0 and title == "Unknown" and len(line_text) > 5:
                    title = line_text

                font_size = max(span["size"] for span in line["spans"])
                if font_size > 18:
                    level = "H1"
                elif 14 < font_size <= 18:
                    level = "H2"
                elif 12 <= font_size <= 14:
                    level = "H3"
                else:
                    continue

                outline.append({
                    "level": level,
                    "text": line_text,
                    "page": i + 1
                })

    output = {"title": title, "outline": outline}
    print(f"⏱️ Time taken: {round(time.time() - start_time, 2)}s")
    return output

if __name__ == "__main__":
    result = extract_structure("data/sample_doc.pdf")
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print("✅ Output saved to output.json")
