import json
import sys
import webbrowser

if len(sys.argv) < 2:
    print("Missing file to open")
else:
    with open(sys.argv[1]) as file:
        json_data = file.read()
        data = json.loads(json_data)
        url = data["url"]
        webbrowser.open_new_tab(url)
