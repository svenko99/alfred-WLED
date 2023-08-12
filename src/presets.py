import sys
import json
import os
import http.client

WLED_IP = os.environ.get("WLED_IP")


# Function to create an Alfred item
def create_alfred_item(title, arg):
    return {"title": title, "arg": arg}


# Function to get the list of presets from WLED
def get_presets():
    try:
        conn = http.client.HTTPConnection(WLED_IP)
        conn.request("GET", "/presets.json")
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            return json.loads(data)
        else:
            print(f"Failed to fetch presets. Status code: {response.status}")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        conn.close()


def main():
    # Get the list of presets
    presets_data = get_presets()
    search_query = sys.argv[1].lower() if len(sys.argv) > 1 else None

    if search_query is None:
        # If no search query is provided, then display the list of presets
        presets_list = [
            create_alfred_item(preset_data.get("n"), preset_id)
            for preset_id, preset_data in presets_data.items()
            if preset_id.isdigit()
            and preset_id != "0"  # skip the first preset as it is empty
        ]
    else:
        # If search query is provided, then filter the presets based on the query
        presets_list = [
            create_alfred_item(preset_data.get("n"), preset_id)
            for preset_id, preset_data in presets_data.items()
            if preset_id.isdigit()
            and preset_id != "0"
            and search_query in preset_data.get("n").lower()
        ]

    # Display the list of presets
    output = json.dumps({"items": presets_list})
    print(output)


if __name__ == "__main__":
    main()
