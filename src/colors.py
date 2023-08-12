import sys
import json
import os
import http.client

WLED_IP = os.environ.get("WLED_IP")
COLORS_FILE = "colors.json"


# Function to get the list of colors from the JSON file
def get_colors():
    with open(COLORS_FILE) as f:
        colors_dict = json.load(f)
    return colors_dict


# Function to convert color name to RGB
def color_to_rgb(color, colors_dict):
    try:
        return colors_dict[color].split()
    except KeyError:
        print(f"Invalid color name: {color}")
        sys.exit(1)


# Function to check if the provided argument is a valid hex color
def hex_to_rgb_color(color_str):
    # Remove the # character
    color_str = color_str[1:]
    try:
        red = int(color_str[:2], 16)
        green = int(color_str[2:4], 16)
        blue = int(color_str[4:6], 16)
        return red, green, blue
    except ValueError:
        return None


# Function to send the color to WLED
def send_color(red, green, blue, query):
    url = "/json/state"
    data = {"seg": [{"col": [[red, green, blue], [0, 0, 0], [0, 0, 0]]}], "on": True}
    payload = json.dumps(data)
    headers = {
        "Content-Type": "application/json",
        "Content-Length": len(payload),
    }

    try:
        conn = http.client.HTTPConnection(WLED_IP)
        conn.request("POST", url, body=payload, headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            print(f"Color changed to: {query}")
        else:
            print(f"Failed to change color. Status code: {response.status}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def main():
    # Get the list of colors and the user query
    colors_dict = get_colors()
    query = sys.argv[1].lower().strip()

    # Check if the query is a hex color
    if query.startswith("#"):
        if rgb_color := hex_to_rgb_color(query):
            red, green, blue = rgb_color
        else:
            print("Invalid hex color format.")
            sys.exit(1)
    else:
        red, green, blue = color_to_rgb(query, colors_dict)

    # Send the color to WLED
    send_color(red, green, blue, query)


if __name__ == "__main__":
    main()
