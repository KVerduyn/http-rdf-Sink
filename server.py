from flask import Flask, request
import os

app = Flask(__name__)

SAVE_DIR = "/data/captured_rdf"  # Directory inside the container
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route("/", methods=["POST", "PUT"])
def capture():
    content_type = request.headers.get("Content-Type", "text/turtle")  # Default to Turtle
    ext = ".ttl" if "turtle" in content_type else ".jsonld" if "json" in content_type else ".rdf"

    filename = f"{SAVE_DIR}/rdf_data_{len(os.listdir(SAVE_DIR)) + 1}{ext}"
    
    with open(filename, "wb") as f:
        f.write(request.data)

    print(f"Saved RDF file: {filename}")
    return "RDF data saved\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

